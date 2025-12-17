# 🐞 Intel Bug Detection & Fixing Project

**Team Name:** Intel Bug Busters
**Author:** Pritam Chakrabortty

---

## 📌 Overview

The **Intel Bug Detection & Fixing Project** is an AI-powered web application designed to **detect, explain, and fix programming bugs** automatically.
Users can input buggy code in multiple programming languages, and the system analyzes errors **line-by-line**, explains them clearly, and provides a **fully corrected version of the code** that is ready to run.

The application is built using **Flask (Python)** with an interactive frontend using **HTML, CSS, and JavaScript**.

---

## 🚀 Features

* ✅ Automatic bug detection
* 🤖 AI-powered bug explanation and fixing
* 🧠 Line-wise error explanation in simple language
* 🖥️ Clean and user-friendly web interface
* 📋 Copy-ready fixed code (no extra text)
* ⚡ Fast and real-time responses

---

## 🛠 Tech Stack

### 🔹 Frontend

* HTML
* CSS
* JavaScript
* Flask (Template Rendering)

### 🔹 Backend

* Python
* Flask (API handling)
* AI Model (Groq / Gemini-based LLM)

### 🔹 Deployment

* Google Colab (development & testing)
* Render (cloud deployment)

---

## 🌍 Live Demo

🔗 **[Intel Bug Detection & Fixing Project](https://openai-bug-fixer-main-1.onrender.com/)**


---

## 📁 Project Structure

```
INTEL-BUG-DETECTION---FIXING-PROJECT-PC/
│── __pycache__/                         # Compiled Python files
│── static/                              # Static assets
│   └── images/
│── templates/
│   └── index.html                       # Frontend UI
│── app.py                               # Flask application
│── requirements.txt                     # Dependencies
│── .env                                 # Environment variables
│── README.md                            # Project documentation
│── demo.mp4                             # Demo video
│── Bug_Detection_and_Fixing.docx        # Project report
│── Intel_Bug_Detection_Fixing.pptx      # Presentation slides
│── .gitignore                           # Git ignored files
│── LICENSE                              # MIT License
```

---

## ⚡ Installation & Setup

### 🔹 Prerequisites

Make sure you have:

* Python 3.10+
* VS Code
* Pip

---

### 🔹 Clone Repository

```bash
git clone https://github.com/Pritam-Chakrabortty/openai_bug_fixer-main

```

---

### 🔹 Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 🔹 Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_api_key_here
```

---

### 🔹 Run the Application

```bash
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

## 🎯 How to Use

1. Select a programming language (Python, Java, C, C++)
2. Paste buggy code into the input box
3. Click **Explain Errors** → See line-wise error explanation
4. Click **Fix Code** → Get clean, corrected code
5. Copy and run the fixed code anywhere

---

## 🔗 API Endpoints

| Method | Endpoint   | Description                      |
| ------ | ---------- | -------------------------------- |
| POST   | `/explain` | Explains all errors line-by-line |
| POST   | `/fix`     | Returns fully corrected code     |

---

## 📹 Demo Video

🎥 **[Watch Demo:](https://github.com/Pritam-Chakrabortty/openai_bug_fixer-main/releases/download/v0.1-demo/DEMO.mp4)** 

---

## 📄 Documentation

📘 **Project Report:** `Bug_Detection_and_Fixing.docx`

---

## 🎤 Presentation

📊 **[Slides:](https://github.com/Pritam-Chakrabortty/openai_bug_fixer-main/blob/main/Intel%C2%AEUnnati%20Industrial%20Training%20Program%202025.pptx)** `Intel_Bug_Detection_Fixing.pptx`

---

## 📈 Future Enhancements

* CI/CD pipeline integration
* Unit testing automation
* More language support
* Improved AI accuracy

---

## 🤝 Contributing

Contributions are welcome!
Please fork the repository and create a pull request.

---

## 📝 License

This project is licensed under the **MIT License**.

---

## 📞 Contact

**Author:** Pritam Chakrabortty
**GitHub:** [https://github.com/Pritam-Chakrabortty](https://github.com/Pritam-Chakrabortty)
**Email:** [bwubta22388@brainwareuniversity.ac.in](mailto:bwubta22388@brainwareuniversity.ac.in)
