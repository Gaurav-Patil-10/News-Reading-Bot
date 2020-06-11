# Akbar padhke sunao ( Newspaper reading)
# install pywin32
import requests



def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.Spvoice")
    speak.Speak(str)

def news_content(n):
    url = "http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=82f6b367c0974043a0e7f01d0155fca1"
    news_json = requests.get(url).json()
    headlines = news_json['articles']
    line1 = headlines[n]['title']
    line2 = headlines[n]['description']
    speak(line1)
    speak(line2)





if __name__ == '__main__':
    speak("Hello How are you , I am going to give you top 10 news updates ")
    i = 0
    for x in range(10):
        speak(f"news number {i+1} is")
        news_content(i)
        i +=1
    speak("Thank You Have a Nice Day !!")


