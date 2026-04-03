# ✉️ AI Email Generator

An AI-powered web application that generates professional emails based on a given situation and recipient — built with Python (Flask) and the Gemini / OpenAI API.

---

## 🚀 Demo

> Enter a situation → Select recipient → Get a ready-to-send email in seconds.

---

## 📁 Project Structure

```
ai-email-generator/
│
├── app.py                  # Flask backend — routes & AI API call
├── requirements.txt        # Python dependencies
│
├── templates/
│   ├── input.html          # User input page
│   └── output.html         # Generated email display page
│
└── README.md
```

---

## ⚙️ Features

- 🤖 AI-generated emails tailored to the situation and recipient
- 🎨 Clean, professional dark-themed UI with animations
- 📋 One-click copy to clipboard on the output page
- 🔁 Instantly generate a new email without leaving the app
- ⚡ Lightweight Flask backend — easy to deploy anywhere

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| AI | Google Gemini API / OpenAI API |
| Frontend | HTML, CSS, Vanilla JS |
| Fonts | Google Fonts (Playfair Display, DM Sans) |

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-email-generator.git
cd ai-email-generator
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set your API key

Create a `.env` file in the root directory:

```env
API_KEY=your_api_key_here
```

Or export it directly in your terminal:

```bash
export API_KEY="your_api_key_here"
```

### 5. Run the app

```bash
python app.py
```

Open your browser and go to: **http://127.0.0.1:5000**

---

## 🔑 Getting an API Key

- **Google Gemini:** https://aistudio.google.com/app/apikey
- **OpenAI:** https://platform.openai.com/api-keys

---

## 📄 requirements.txt

```
flask
google-generativeai   # or openai, depending on your API choice
python-dotenv
```

---

## 🧠 How It Works

1. User fills in the **situation** (e.g., *"Request for leave"*) and the **recipient** (e.g., *"Manager"*)
2. Flask receives the form data via `POST /`
3. The input is sent as a prompt to the AI API
4. The generated email is returned and rendered on the output page
5. User can copy the email or generate a new one

---



> ⭐ If you found this project useful, consider giving it a star!
