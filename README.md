# Project README

## AI Email Summarizer Automation

A simple low-code automation project built using **n8n** and a small **Python Cloud Function**.  
The workflow fetches data from a public API, sends it to a Python microservice for processing, generates an AI summary using an LLM API, and stores the result in Google Sheets (or sends via email).

This project demonstrates:
- Low-code automation (n8n)
- Python scripting for API processing
- Connecting automation tools with cloud functions
- Using LLM APIs for text summarization
- Clean documentation and a small, functional project structure

---

## 📌 Architecture Overview

n8n (Scheduler) → Fetch API Data → Python Cloud Function → LLM Summary → Email/Sheets

---

## 📁 Folder Structure

```
/cloud-function
main.py # Python microservice for summarization
requirements.txt # Libraries needed

/workflow
n8n_workflow.json # n8n workflow export

README.md # Project documentation
```

---

## 🚀 How It Works

1. **n8n Trigger**  
   A Cron node runs daily or weekly.

2. **Fetch Data**  
   n8n makes a GET request to a public API (News API example).

3. **Send to Python Cloud Function**  
   The raw data is passed to `main.py`, which:
   - Extracts key text from the API response  
   - Calls an LLM API to summarize the content  
   - Returns a clean summary

4. **Store or Send Summary**  
   n8n saves the summary to Google Sheets or emails it to a chosen address.

---


## 🧠 AI Interaction Example

The Python function sends a prompt such as:

"Summarize the following data in clear bullet points..."

And returns a concise summary used in reporting.

---

## 🛠️ Tools Used

- **n8n** (workflow automation)
- **Python (Cloud Function)**  
- **LLM API** (OpenAI / Gemini)
- **Google Sheets or Email node**

---

## 📌 Why This Project?

This demonstrates exactly the kind of automation, experimentation, and AI-first thinking expected in modern growth marketing and operations teams.  
It’s simple, clear, and shows real technical ability.

---

## 📬 Contact

If you'd like to know more about this automation or my other technical projects, feel free to reach out.
