# 🧠 My GenAI Learning Journey: Python & LangChain

> My personal code, notes, and projects while learning **Generative AI with Python, LangChain, LangGraph, AWS Bedrock, and MCP Servers**, following the *GenAI with Python & LangChain | Complete GEN-AI Course 2026* by **TechSimPlus Learnings**.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-learning-1C3C3C)
![LangGraph](https://img.shields.io/badge/LangGraph-learning-orange)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📖 About This Repository

This repo documents my hands-on progress through the GenAI course. For each video I:

1. Watch the lesson
2. Write and run the code myself
3. Add my own notes, experiments, and fixes
4. Push it here

The goal is to build real understanding and a portfolio of working GenAI projects: chatbots, RAG systems, agents, and MCP-connected tools.

> 📺 **Course followed:** [GenAI with Python & LangChain | Complete GEN-AI Course 2026](https://www.youtube.com/playlist?list=PLUhY5ME1VdItcTMnzYakPdYJWorU6IdKk) by TechSimPlus Learnings.
>
> ⚠️ This is an independent learning repo. I am **not affiliated** with the course creator. All credit for the curriculum goes to them; the code here is my own practice work.

---

## 🎯 Learning Goals

- [ ] Understand how LLMs work and how to call them from Python
- [ ] Master prompt engineering and LangChain chains (LCEL)
- [ ] Build RAG applications over my own documents
- [ ] Create stateful agents with LangGraph
- [ ] Use foundation models through AWS Bedrock
- [ ] Build and connect MCP servers
- [ ] Complete 10+ end-to-end projects

---

## 📈 Progress Tracker

| # | Topic | Status | Notes |
|---|-------|--------|-------|
| 1 | Python & environment setup | ⬜ Not started | |
| 2 | LLM basics & first API calls | ⬜ Not started | |
| 3 | Prompt engineering | ⬜ Not started | |
| 4 | LangChain fundamentals | ⬜ Not started | |
| 5 | RAG & vector stores | ⬜ Not started | |
| 6 | LangGraph & agents | ⬜ Not started | |
| 7 | AWS Bedrock | ⬜ Not started | |
| 8 | MCP servers | ⬜ Not started | |
| 9 | Projects | ⬜ Not started | |

Status key: ⬜ Not started · 🟨 In progress · ✅ Done

> Update this table as you go, and replace the rows with the real video titles from the playlist.

---

## 🗂️ Repository Structure

```
genai-learning-journey/
├── 01-python-basics/
├── 02-llm-basics/
├── 03-langchain/
├── 04-rag/
├── 05-langgraph/
├── 06-aws-bedrock/
├── 07-mcp/
├── projects/
├── notes/                 # My own summaries and takeaways
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

> Adjust folder names to match how you organize your code (e.g., `video-01-intro`, `video-02-...`).

---

## ⚙️ Setup

**1. Clone this repo**

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

**2. Create a virtual environment**

```bash
# macOS / Linux
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Add your API keys**

```bash
cp .env.example .env
```

```env
OPENAI_API_KEY=your_key_here
GOOGLE_API_KEY=your_key_here
AWS_ACCESS_KEY_ID=your_key_here
AWS_SECRET_ACCESS_KEY=your_key_here
AWS_DEFAULT_REGION=us-east-1
```

> 🔒 **Never commit your `.env` file or API keys.** Add `.env` to `.gitignore` before your first push.

---

## ▶️ Running the Code

```bash
python path/to/script.py
```

For notebooks:

```bash
pip install jupyter
jupyter notebook
```

---

## 🧰 Tech Stack

- **Language:** Python
- **Frameworks:** LangChain, LangGraph
- **LLM providers:** OpenAI, AWS Bedrock (and others as covered in the course)
- **Vector stores:** as used in the lessons (e.g., Chroma, FAISS)
- **Protocol:** Model Context Protocol (MCP)
- **Tools:** Jupyter, python-dotenv, Git & GitHub

---

## 📝 What I've Learned

*Add short takeaways here as you progress, for example:*

- LCEL lets me compose prompt → model → parser in one readable pipeline.
- RAG reduces hallucination by grounding answers in retrieved documents.

---

## 🚀 Projects

| Project | Description | Tech | Status |
|---------|-------------|------|--------|
| _Chatbot_ | Conversational bot with memory | LangChain | ⬜ |
| _RAG Q&A_ | Ask questions over my documents | LangChain, vector DB | ⬜ |
| _Agent_ | Tool-using agent | LangGraph | ⬜ |
| _MCP Server_ | Custom tools exposed via MCP | MCP | ⬜ |

*(Replace with the actual projects from the course.)*

---

## 🙏 Credits

- **[TechSimPlus Learnings](https://www.youtube.com/playlist?list=PLUhY5ME1VdItcTMnzYakPdYJWorU6IdKk)** for the course this repo follows
- [LangChain](https://www.langchain.com/) & [LangGraph](https://www.langchain.com/langgraph) documentation
- [Model Context Protocol](https://modelcontextprotocol.io/)

---

## 📜 License

My original code is released under the [MIT License](LICENSE). Course content, ideas, and materials belong to their respective creators.

---

<p align="center">⭐ Learning in public: follow along or star the repo! ⭐</p>