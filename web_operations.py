import webbrowser as wb

def open_site(query):
    query = query.lower()

    sites = {
        "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "facebook": "https://www.facebook.com",
    "twitter (x)": "https://twitter.com",
    "instagram": "https://www.instagram.com",
    "linkedin": "https://www.linkedin.com",
    "wikipedia": "https://www.wikipedia.org",
    "amazon": "https://www.amazon.com",
    "flipkart": "https://www.flipkart.com",
    "netflix": "https://www.netflix.com",
    "spotify": "https://www.spotify.com",
    "gmail": "https://mail.google.com",
    "yahoo mail": "https://mail.yahoo.com",
    "outlook": "https://outlook.live.com",
    "reddit": "https://www.reddit.com",
    "quora": "https://www.quora.com",
    "github": "https://github.com",
    "stack overflow": "https://stackoverflow.com",
    "python official": "https://www.python.org",
    "openai": "https://openai.com",
    "bbc news": "https://www.bbc.com",
    "cnn": "https://www.cnn.com",
    "ndtv": "https://www.ndtv.com",
    "times of india": "https://timesofindia.indiatimes.com",
    "hacker news": "https://news.ycombinator.com",
    "twitch": "https://www.twitch.tv",
    "discord": "https://discord.com",
    "whatsapp web": "https://web.whatsapp.com",
    "telegram web": "https://web.telegram.org",
    "microsoft": "https://www.microsoft.com",
    "apple": "https://www.apple.com",
    "samsung": "https://www.samsung.com",
    "flipboard": "https://flipboard.com",
    "coursera": "https://www.coursera.org",
    "udemy": "https://www.udemy.com",
    "khan academy": "https://www.khanacademy.org",
    "imdb": "https://www.imdb.com",
    "hotstar": "https://www.hotstar.com",
    "prime video": "https://www.primevideo.com",
    "disney+": "https://www.disneyplus.com",
    "chat gpt":"https://chatgpt.com/"
    }

    for site in sites:
        if site in query:
            wb.open(sites[site])
            return f"Opening {site}, Ma'am..."

    return ""

