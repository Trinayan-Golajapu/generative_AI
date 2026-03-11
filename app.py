import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import os
from youtube_transcript_api import YouTubeTranscriptApi

# configure API key

genai.configure(api_key="AIzaSyDu4bbpxyBTJn3XTGXj6YsIRNX-DfUDtnw")

# Prompt

prompt = """
please summarize this video transcript into 250 words or less, highlighting keypoints
"""

# Function to get Transcript from YouTube Video URL

def extract_transcript(video_url):
    try:
        video_id = video_url.split("=")[1]
        ytt=YouTubeTranscriptApi()
        fetched_transcript =  ytt.fetch(video_id)
        transcript = " ".join([snippet.text for snippet in fetched_transcript])
        return transcript
    except Exception as e:
        raise e

# Function to generate detailed summary using Google Gemini Pro

def generate_gemini_content(transcript_text,prompt):
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt + transcript_text)
    return response.text 


url_input = "https://www.youtube.com/watch?v=qML4Tvf1P1s"

text = extract_transcript(url_input)
response = generate_gemini_content(text,prompt)
print(response)

# for model in genai.list_models():
#     print(model.name)



