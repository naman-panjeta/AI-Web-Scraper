# AI Web Scraper

## 📌 Overview
This project is an **AI-powered web scraper** that extracts and processes structured data from websites. It utilizes **Selenium, BeautifulSoup, and LangChain with Llama 3.1** to intelligently parse and filter content based on user input.

## 🚀 Features
- 🌐 **Automated Web Scraping** using Selenium & BeautifulSoup  
- 🤖 **AI-Powered Parsing** with Llama 3.1 & LangChain  
- 🖥️ **User-Friendly UI** built with Streamlit  
- 🔍 **Customizable Content Extraction** based on user input  
- 📜 **Efficient Text Processing** with chunking & cleaning  
- 🔐 **Secure API Integration** with environment variables  

## 🛠️ Tech Stack
- **Python**
- **Streamlit** (UI)
- **Selenium & BeautifulSoup** (Scraping)
- **LangChain & Llama 3.1** (AI-powered parsing)
- **HTML Parsing** (lxml, html5lib)
- **WebDriver Manager**
- **Python-dotenv** (API key management)

## 📂 Project Structure
```
📂 AI-Web-Scraper
├── main.py          # Streamlit UI for input & output
├── scrape.py        # Web scraping logic using Selenium & BeautifulSoup
├── parse.py         # AI-powered parsing with Llama 3.1 & LangChain
├── requirements.txt # Dependencies
└── README.md        # Project documentation
```

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ai-web-scraper.git
   cd ai-web-scraper
   ```

2. **Set up a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Create a `.env` file in the project root and add your API key:
     ```
     LLAMA_API_KEY=your_llama_api_key
     ```

## ▶️ Usage

1. **Run the Streamlit app**
   ```bash
   streamlit run main.py
   ```
2. **Enter a website URL** in the input field.
3. **Click "Scrape Site"** to extract and display website content.
4. **Describe what you want to parse** and click "Parse Content."
5. **View extracted information** processed by Llama 3.1.

## 📝 Notes
- Ensure **ChromeDriver** is installed for Selenium.
- The parsing model uses **Llama 3.1** instead of OpenAI.
- Some sites may block scraping—consider adding **headers & proxies** if needed.

## 🏗️ Future Improvements
- ✅ Add proxy support to bypass restrictions.
- ✅ Implement a database to store parsed data.
- ✅ Expand support for more AI models.

---

💡 *Feel free to contribute or suggest improvements!*
