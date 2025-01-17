# Video-AI-Summarizer-Agent 🎥

## Description
The Video AI Summarizer Agent analyzes video content using AI algorithms to extract key information such as scene changes, important events, and relevant dialogue. It then compiles this data into a summary, providing a detailed overview of the video's content. It also capable of providing answers to the user's questions.

## Features 🚀
- Video content analysis and summarization
- Question-answering about video content
- Support for multiple video formats (MP4, MOV, AVI)
- Web research integration via DuckDuckGo
- Powered by Google's Gemini 2.0 model
- User-friendly Streamlit interface

## Demo 📺
[![Project Demo](https://img.youtube.com/vi/EqFJbIXWviE/0.jpg)](https://www.youtube.com/watch?v=EqFJbIXWviE)

## Tech Stack 💻
- Python 3.7+
- Streamlit
- Google Generative AI (Gemini)
- Phi Agent Framework
- DuckDuckGo API
- Python-dotenv

## Installation 🛠️

### Prerequisites
- Python 3.7 or higher
- Google API key for Gemini

### Steps

1. Clone the repository
```bash
git clone https://github.com/yourusername/Video-AI-Summarizer-Agent.git
cd Video-AI-Summarizer-Agent
```

2. Create and activate virtual environment
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables Create a .env file in the root directory:
```bash
GOOGLE_API_KEY=your_google_api_key_here
```

## Usage 📝

1. Start the application
```bash
streamlit run app.py
```

2. Open your browser and navigate to http://localhost:8501

3. Upload a video file (MP4, MOV, or AVI format)

4. Enter your question or analysis request

5. Click "Analyze Video" to get insights

## Project Structure 📁

```bash
Video-AI-Summarizer-Agent/
├── app.py              # Main Streamlit application
├── requirements.txt    # Project dependencies
├── .env               # Environment variables
└── README.md          # Project documentation
```

## Requirements 📋
See requirements.txt for full list of dependencies:

- streamlit
- phi
- google-generativeai
- python-dotenv
- pathlib

## Contributing 🤝
1. Fork the repository
2. Create a new branch (git checkout -b feature/improvement)
3. Make changes and commit (git commit -am 'Add new feature')
4. Push to the branch (git push origin feature/improvement)
5. Create a Pull Request

## License 📄
This project is licensed under the MIT License - see the LICENSE file for details.

## Author ✨
Sujal

## Acknowledgments 🙏
- Google Gemini Team
- Streamlit Community
- Phi Framework Developers


```Made with ❤️ using Gemini and Streamlit ```