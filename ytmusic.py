import pywhatkit as kit

def play_youtube_music(song_name):
    try:
        kit.playonyt(song_name)
        return f"Playing {song_name} on YouTube!"
    except Exception as e:
        return f"Error: {str(e)}" 
