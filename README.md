# ArXivMind 📚

ArXivMind is an intelligent, multi-agent system designed to accelerate academic research. Built with Microsoft's `AutoGen` framework, it automates the process of finding and summarizing scholarly articles from arXiv. The system deploys two specialized AI agents that collaborate to conduct a literature review on any given topic, delivering a concise and structured report directly to the user.

This project offers two modes of operation:
1.  A command-line interface (`backend.py`) for running a predefined search query.
2.  An interactive web application (`streamlit.py`) built with Streamlit for a dynamic, user-friendly experience.

---
## ✨ Key Features

* **Multi-Agent Collaboration:** Utilizes a `search_agent` to craft optimal queries and retrieve papers from arXiv, and a `summarizer` agent to analyze the findings and generate a high-quality literature review.
* **Automated Literature Review:** Generates a markdown-formatted report that includes an introduction, detailed summaries of each paper (with links, authors, contributions, and future scope), and a final takeaway.
* **Interactive Web UI:** Features a clean and simple interface built with Streamlit, allowing users to input their research topic and select the number of papers to review.
* **Powered by OpenAI:** Leverages the `gpt-4o-mini` model for intelligent query generation and sophisticated text summarization.
* **Real-time Streaming:** Streams the agents' conversation and final report in real-time, providing transparency into the research process.

---
## 🎬 Demo

See ArXivMind in action! The demo shows how to use the interactive Streamlit web application to generate a literature review. Click the image below to watch the video.

[![ArXivMind Demo Video](https://drive.google.com/uc?export=view&id=1KwoFdNzR1Btu4lctAwfc98njUsfmLFXU)](https://drive.google.com/file/d/1H2PCgE9AdzVANzXuhRfnMMGW6QCNAECT/view?usp=sharing)

---
## 🛠️ Getting Started

Follow these instructions to set up and run ArXivMind on your local machine.

### Prerequisites

* [Anaconda](https://www.anaconda.com/products/distribution) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) installed.
* An [OpenAI API key](https://platform.openai.com/api-keys).

### 1. Clone the Repository

First, clone the project repository from GitHub.

```bash
git clone [https://github.com/YOUR_GITHUB_USERNAME/ArXivMind.git](https://github.com/YOUR_GITHUB_USERNAME/ArXivMind.git)
cd ArXivMind
```
**Note:** Remember to replace `YOUR_GITHUB_USERNAME` with your actual GitHub username.

### 2. Create and Activate Conda Environment

Create a dedicated Conda environment for the project using Python 3.12.

```bash
conda create -n arxivmind python=3.12 -y
conda activate arxivmind
```

### 3. Install Dependencies

Install all the required Python packages from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

You need to provide your OpenAI API key for the agents to function.

1.  Create a file named `.env` in the root directory of the project.
2.  Add your OpenAI API key to the file as shown below:

```env
OPENAI_API_KEY="sk-..."
```

---
## 🚀 Usage

ArXivMind can be run in two different modes.

### 1. Terminal Mode (`backend.py`)

This mode runs a hardcoded literature review task directly in your terminal. It's useful for testing the backend logic. By default, it searches for 5 papers on "Artificial Intelligence".

To run it, execute the `backend.py` script:

```bash
python backend.py
```

The script will stream the conversation between the `search_agent` and the `summarizer`, followed by the final literature review.

### 2. Interactive Web App (`streamlit.py`)

This is the primary mode for using ArXivMind. It launches a local web server with a user-friendly Streamlit interface.

To start the web application, run the following command in your terminal:

```bash
streamlit run streamlit.py
```

This will open a new tab in your web browser at **http://localhost:8501**. You can then enter a research topic, select the number of papers, and click "Search" to begin.

---
## 📂 Project Structure

```
.
├── backend.py            # Script for terminal-based agent interaction
├── streamlit.py          # Script to launch the interactive Streamlit web UI
├── requirements.txt      # Python dependencies
├── .env                  # File for API keys (you need to create this)
└── README.md             # This file
