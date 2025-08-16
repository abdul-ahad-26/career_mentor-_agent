# Career Mentor Agent

The **Career Mentor Agent** is a multi-agent system built with **Chainlit** and **OpenAI Agents SDK**. It helps students explore potential career paths based on their skills and interests. The agents collaborate through **handoffs** to provide personalized guidance.

---

## 🚀 Features

* Guides students in exploring career options.
* Uses multiple agents with orchestrated handoffs.
* Simple Chainlit interface for interaction.
* Built with Python, UV, and Gemini API.

---

## 🛠️ Getting Started

### 1️⃣ Install UV

First, install **UV** (if not already installed):

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

For Windows:

```sh
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verify installation:

```sh
uv --version
```

---

### 2️⃣ Create and Initialize the Project

```sh
uv init career_mentor_agent
cd career_mentor_agent
```

---

### 3️⃣ Install Dependencies

```sh
uv add openai-agents python-dotenv chainlit
```

---

### 4️⃣ Activate Virtual Environment

**Windows:**

```sh
.venv\Scripts\activate
```

**Linux/macOS:**

```sh
source .venv/bin/activate
```

---

### 5️⃣ Setup Environment Variables

Create a `.env` file in the project root:

```sh
GEMINI_API_KEY=your_gemini_api_key
```

👉 Get your Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

---

### 6️⃣ Run the Career Mentor Agent

```sh
chainlit run main.py --watch
```

* `--watch` automatically reloads when files change.
* Interact by typing messages like `hi` or `bye` in the Chainlit UI.

---

## 📂 Project Structure

```
├─ my_agent/
│  ├─ career_agent.py
│  ├─ job_agent.py
│  └─ skill_agent.py
├─ my_config/
│  └─ gemini_config.py
├─ tools/
│  └─ skill_road_map.py
├─ main.py
├─ chainlit.md
├─ README.md
├─ pyproject.toml
├─ requirements.txt
└─ .env
```

I’d love to hear your feedback. Any collaboration is welcomed.  
