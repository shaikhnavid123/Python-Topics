# Akhabaar padke sunao
import json
import requests
def speak(str):
    from win32com.client import Dispatch

    speak = Dispatch("SAPI.SpVoice")

    speak.Speak(str)

if __name__ == '__main__':
    speak("News for today... Let's begin")
    url = "https://newsapi.org/v2/everything?domains=wsj.com&apiKey=a2921f16f0874b19a2582950b366b86b"
    news = requests.get(url).text
    # print(news)
    news_dict = json.loads(news)
    print(news_dict["articles"])
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        speak("Moving on to the next news... Listen Carefully")
