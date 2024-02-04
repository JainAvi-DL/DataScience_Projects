import streamlit as st
from dotenv import load_dotenv # load all environment variables
load_dotenv()
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key= os.getenv('GOOGLE_API_KEY'))

#Backend
prompts = '''You are youtube video summarizer.You are expert of this.You will be taking transcript of youtube video and summarize the entire video 
and provide the important summary in points within 500 words.Please provide the beautiful summary :
'''


# getting transcript videos from yt videos
def extract_transcript_details(yt_url):
    try:
        video_id = yt_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = ""
        for i in transcript_text:
            transcript += i['text'] + " "
        return transcript
    except Exception as e:
        raise e
        

# getting summary based on prompt from gemini using transcript
def generate_gemini_content(transcript, prompts):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompts+transcript)
    return  response.text


#Frontend
st.title("Youtube Video Summarizer")
YoutubeLink = st.text_input("Enter Youtube Link: ")

if YoutubeLink:
    video_id = YoutubeLink.split("=")[1]
    st.image(f"https://img.youtube.com/vi/{video_id}/0.jpg",use_column_width=True)
if st.button("Summarize"):
    transcript = extract_transcript_details(YoutubeLink)
    
    if transcript:
        # st.write(transcript)
        summary = generate_gemini_content(transcript, prompts)
        st.markdown(summary, unsafe_allow_html=True)
        st.write(summary)
    else:
        st.write("No Transcript Found")
        
