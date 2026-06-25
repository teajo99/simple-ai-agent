# Simple AI Agent 

A lightweight Python-based AI agent built to simulate a basic tool-using assistant.
This project demonstrates how an AI-style agent can route user input to tools like a calculator, time function, memory system, and logging system.

It was built while learning **Python, Git, debugging, and real development workflows**.

---

## Features

*  Calculator tool (supports basic math like `12 * 4`)
*  Current time tool
*  Memory system (tracks conversation/session data)
*  Logging system (stores interactions)
*  Branch-based development using Git
*  Versioned release (`v1.0.0`)

---

##  Project Structure

```
simple-ai-agent/
│
├── agent.py        # Main AI agent (input + routing logic)
├── tools.py        # Calculator + time tools
├── memory.py       # Stores conversation history
├── logger.py       # Logs every interaction
├── README.md       # Documentation
```

---

##  How It Works

1. User types input (e.g. `calc 50 * 7`)
2. `agent.py` processes the input
3. It routes the request to a tool in `tools.py`
4. The tool returns a result
5. Memory + logger store the interaction

---

##  How to Run

### 1. Clone the repository

```bash
git clone https://github.com/teajo99/simple-ai-agent.git
cd simple-ai-agent
```

### 2. Run the agent

```bash
python agent.py
```

---

##  Example Usage

```
You: calc 12 * 4
Agent: 12 * 4 = 48

You: what time is it
Agent: It is currently 14:32:10 on Monday, 26 June 2026.

You: help
Agent: Available commands:
  exit / quit   end the session
```

---

##  Learning Notes & Debug History

This project was built while actively learning Python and Git. Many real-world errors were encountered and fixed.

---

###  Common Errors Faced

#### 1. Python not found / typo issue

```
phyton agent.py 
python agent.py 
```

Lesson:

* Small spelling mistakes break everything

---

#### 2. Invalid code inside tools.py

```
NameError: name 'tools' is not defined
```

Cause:

* Accidentally wrote `tools.py` inside the file

Fix:

* Removed invalid line

---

#### 3. Git log stuck in viewer

```
(END)
```

Fix:

```
Press q to exit
```

---

#### 4. Git branch workflow confusion

Commands used:

```bash
git checkout -b feature/tools
git merge feature/tools
git branch -d feature/tools
```

Lesson:

* Feature branches must be merged before deletion

---

#### 5. Windows line ending warning

```
LF will be replaced by CRLF
```

Meaning:

* Linux vs Windows formatting difference
* Safe to ignore

---

## Questions Asked During Development

* How to install Python
* How to fix Git errors
* How to move from master to main
* How to use vi editor
* How Git branches work
* How to push to GitHub
* How to exit git log
* Meaning of CRLF/LF warnings
* How to debug Python errors

---

##  Final Result

This project evolved into a working AI agent with:

* ✔ Tool-based architecture
* ✔ Calculator + time tools
* ✔ Memory system
* ✔ Logging system
* ✔ Git branching workflow
* ✔ GitHub deployment
* ✔ Versioned release (`v1.0.0`)

---

## Key Takeaway

> Mistakes and debugging are part of building real software. Every error improved understanding of Python, Git, and system design.

---

##  Author

Built as a learning project to understand:

* AI agent architecture
* Python modular design
* Git workflows
* Debugging real-world issues

