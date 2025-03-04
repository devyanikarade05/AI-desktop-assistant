import speech_recognition as sr
import streamlit as st
from text_to_speech import speak

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            st.write("🎤 Listening...")
            audio = r.listen(source)  # , timeout=5, phrase_time_limit=8
            st.write("🔍 Recognizing...")
            query = r.recognize_google(audio, language='en-IN')
            st.success(f"✅ You said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            st.error("⚠️ Couldn't understand. Say that again...")
            speak("Couldn't understand. Say that again...") # after this it doesnt go to fireworkai instead start listening
            return ""
        except sr.RequestError:
            st.error("⚠️ Google Speech API error!")
            return ""
