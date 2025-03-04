import streamlit as st
from text_to_speech import speak
from speech_to_text import takeCommand
from web_operations import open_site
from tell_time import tell_time
from fireworksAI import firework_chat
import streamlit.components.v1 as components
from weather import get_weather
from ytmusic import play_youtube_music
from control import control_pc
import time


st.set_page_config(page_title="Ashoka - AI Assistant", layout="wide")

st.sidebar.title("🤖 My capabilities / What can I do?")
st.sidebar.write("🎤 **Voice-controlled AI (No need to type, just speak!)**")
st.sidebar.write("❓ **Answer any question**")
st.sidebar.write("💬 **chat with you on any topic**")
st.sidebar.write("🎵 **Play Music on YouTube**")
st.sidebar.write("🌦️ **Tell the Weather**")
st.sidebar.write("🕰️ **Give Current Time**")
st.sidebar.write("🌍 **Open Websites**")
st.sidebar.write("💻 **Controls pc: Shutdown/Restart**")
st.sidebar.write("📝 **Open notepad**")
st.sidebar.write("🧮 **Open calculator**")



animation_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            margin: 0;
            background-color: black;
            overflow: hidden;
        }
        #particles-js {
            position: fixed;
            width: 100%;
            height: 100%;
            z-index: -1;
        }
        .content{
            position: relative;
            text-align: center;
            color: white;
            font-size: 32px;
            font-weight: bold;
            padding-top: 100px;
        }
        .listening {
            position: relative;
            text-align: center;
            color: white;
            font-size: 32px;
            padding-top: 100px;
        }
        .mic {
            position: relative;
            text-align: center;
            color: white;
            font-size: 50px;
            padding-top: 30px;
        }
    </style>
</head>
<body>
    <div id="particles-js"></div>
    <div class="content">Ashoka - Your AI Assistant</div>
        <div class="listening">Ashoka is continuously listening....</div>
       <div class="mic">🎤</div>
</div>
    
    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <script>
        particlesJS("particles-js", {
            "particles": {
                "number": {"value": 100},
                "size": {"value": 5},
                "color": {"value": "#0015ff"},
                "move": {"speed": 2}
            }
        });
    </script>
</body>
</html>
"""

components.html(animation_code, height=500)


if __name__ == "__main__":
    st.text("Starting...")
    speak("Hi, I am Ashoka")

    while True:
        query = takeCommand().strip()

        if query.lower().startswith("ashoka"):
            query = query[6:].strip()


        if not query or query in ["ok ashoka"]:  # Ignore
            continue

        if "exit" in query or "stop" in query or "quit" in query:
            speak("Goodbye!")
            break

        elif "play music" in query or "play song" in query or "open music" in query or "open song" in query:
            speak("Which song would you like to play?")
            song_name = takeCommand()
            youtube_result = play_youtube_music(song_name)
            st.write(youtube_result)
            speak(youtube_result)
            time.sleep(10)

        elif "weather" in query:
            while True:
                speak("Which city do you want the weather for?")
                city = takeCommand()
                if city:
                    weather_info = get_weather(city)
                    st.write(weather_info)
                    speak(weather_info)
                    break
                else:
                    st.write("I couldn't understand the city name. Please try again.")
                    speak("I couldn't understand the city name. Please try again.")

        else:
            response = open_site(query) or tell_time(query) or control_pc(query)
            if response:
                st.write(response)
                speak(response)
            elif query:  # Check if query is not empty before calling Fireworks AI
                generated_text = firework_chat(query)
                st.write(generated_text)
                speak(generated_text)



