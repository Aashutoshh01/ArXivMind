from __future__ import annotations
import os
import asyncio
from typing import AsyncGenerator, Dict, List
import arxiv
from autogen_core.tools import FunctionTool
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import (
    TextMessage
)
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv
load_dotenv()

def arxiv_search(query: str, max_results: int=5) -> List[Dict]:
    client=arxiv.Client()
    search=arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance,
    )
    papers:List[Dict]=[]
    for result in client.results(search):
        papers.append(
            {
                "title":result.title,
                "authors":[a.name for a in result.authors],
                "published":result.published.strftime("%Y-%m-%d"),
                "summary":result.summary,
                "pdf_url":result.pdf_url,
            }
        )
    return papers

arxiv_tool=FunctionTool(
    arxiv_search,
    description=(
        "Search arXiv and return upto *max_resultd* papers, each containing"
        "title,authors,publication date,abstract,and pdf_url."
    ),
)

def build_team(model: str="gpt-4o-mini")->RoundRobinGroupChat:
    """Create and return a two-agent *RoundRobinGroupChat* team."""
    llm_client=OpenAIChatCompletionClient(model=model,api_key=os.getenv('OPENAI_API_KEY'))
    # Below is the agent that calls only the arXiv tool and forward top-N papers
    search_agent=AssistantAgent(
        name="search_agent",
        description="Crafts arXiv queries and retrieves top candidate papers.",
        system_message=(
            "Given a user topic, think of the best arXix query and call the"
            "provided tool. Always fetch five-times the papers requested so"
            "that you can down-select the most relevant one which has the maximum citation."
            "When the tool returns, choose exactly the number of papers requestedand pass them as concise JSON to the summarizer."
        ),
        tools=[arxiv_tool],
        model_client=llm_client,
        reflect_on_tool_use=True,
    )

    summarizer=AssistantAgent(
        name="summarizer",
        description="Produces a short markdown review from provided papers.",
        system_message=(
            "You are an expert researcher. When you receive the JSON list of"
            "papers, write a literature review style report in markdown:\n"\
            "1. Start with 2-3 sentence introduction of the topic.\n"\
            "2. Then include one bullet per paper with: title (as markdown"
            "link), authors,the specific problem tackled, its key"
            "contribution, and future scope of research.\n"\
            "3. Close with a single-sentence takeaway."
        ),
        model_client=llm_client,
    )

    return RoundRobinGroupChat(
        participants=[search_agent,summarizer],
        max_turns=2,
    )

async def run_litrev(
        topic:str,
        num_papers:int=5,
        model:str="gpt-4o-mini",
)-> AsyncGenerator[str,None]:
    """Yield strings representing the conversation in real-time"""
    team=build_team(model=model)
    task_prompt=(
        f"Conduct a literature review on **{topic}** and return exactly {num_papers} papers."
    )
    async for msg in team.run_stream(task=task_prompt):
        if isinstance(msg,TextMessage):
            yield f"{msg.source}: {msg.content}"

if __name__=="__main__":
    async def _demo()->None:
        async for line in run_litrev("Artificial Intelligence",num_papers=5):
            print (line)

    asyncio.run(_demo())