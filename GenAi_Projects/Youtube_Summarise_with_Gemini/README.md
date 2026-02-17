# 📺 AI YouTube Video Summarizer

**Overview**

This project is an End-to-End LLM Application designed to save users hours of watch time. By leveraging Google’s Gemini-Pro and the YouTube Transcript API, the app extracts spoken content from any YouTube video and generates a concise, point-wise summary within 500 words.

**The Problem**

In an era of "information overload," many educational videos and podcasts are 1-3 hours long. Users often need the core insights without watching the entire video.

**The Solution**

I built a seamless pipeline that:

Extracts raw transcript data directly from YouTube.

Processes the text using Prompt Engineering to define an "Expert Summarizer" persona.

Generates a high-quality summary using Generative AI (LLM).

Deploys a user-friendly interface using Streamlit.

**🏗️ Technical Architecture**

Data Acquisition: Utilizes youtube-transcript-api to fetch timestamped subtitles.

Generative AI: Integrates Google Gemini-Pro via the google-generativeai SDK for natural language understanding.

Frontend: Developed with Streamlit for a responsive, web-based UI.

Environment Management: Uses python-dotenv to securely manage API credentials, following industry best practices for security.

**🚀 Key Features**

Instant Summarization: Get the "gist" of a 30-minute video in seconds.

Visual Feedback: Automatically fetches and displays the video thumbnail using the YouTube Data API logic.

Markdown Support: Delivers "Beautiful Summaries" formatted with bold text and bullet points for high readability.
