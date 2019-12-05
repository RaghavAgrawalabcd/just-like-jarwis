import pyttsx3
import speech_recognition as sr
import pyaudio
import time
import webbrowser
import os
Text=''
Continue=True

responses=["Welcome to the interface of DummyAI\n***** I am Ram *****","MY name is Ram","Thanks for using me","Sorry , Its beyond my reach","Mention Not"]
def extractNofromText(text):
    a=[]
    for t in text.split(" "):
        try:
            a.append(float(t))
        except ValueError:
            pass
    return(a)
def Lcm(a,b):
    l=a if a>b else b
    while(1):
        if l%a==0 and l%b==0:
            print(l)
            return l
        l+=1
def Hcf(a,b):
    while(b):
        a,b=b,a%b
    print(a)
    return a
def things():
    print("I can Open Google,facebook account,Gmail,search on google ,do Calculation and Explain mysel")
    return "I can Open Google,facebook account,Gmail,search on google ,do Calculation and Explain mysel"
def Add(*a):
    s=0
    for v in a:
        s+=v
    print(s)
    return s
def Sub(a,b):
    s=a-b if a>b else b-a
    print(s)
    return s
def Mul(*a):
    s=1
    for v in a:
        s*=v
    print(s)
    return s
def Div(a,b):
    if b==0:
        raise ZeroDivisionError("Invalid attempt ,Try again" )
    else:
        print(a/b)
        return a/b
def name():
    print(responses[1])
    return responses[1]
def sorry():
    print(responses[3])
    return responses[3]
def yourself():
    print("I am Dummy AI.Artificial intelligence (AI) is the simulation of human intelligence processes by machines")
    return "I am Dummy AI.Artificial intelligence (AI) is the simulation of human intelligence processes by machines"
def Hi():
    return "Hi....How are you Raghav",
def good():
    return "Hurray"
def thank():
    return "Mention Not"
operations={"plus":Add,"add":Add,"addition":Add,"sum":Add,"minus":Sub,"subtraction":Sub,"sub":Sub,"subtract":Sub,
            "multiplication":Mul,"multiply":Mul,"mul":Mul,"div":Div,"divide":Div,"division":Div,"divided":Div,"lcm":Lcm,"hcf":Hcf}
commands={"name":name,"work":things,"things":things,"capable":things,"yourself":yourself,"hi":Hi,"hey":Hi,"good":good,"fine":good,"thank":thank,"thankyou":thank,"thanks":thank}
open={"facebook":"www.facebook.com","google":"www.google.com","gmail":"www.gmail.com"}
search={"search":"https://www.google.co.in/search?client=opera&q="}
print(responses[0] + "\n You can ask me for...\n 1.Open google,facebook,Gmail,to Search Anything(Ex. Search  AI) \n 2. I can perform mathematical calculations \n 3.Can Answer personal question also" )
engine = pyttsx3.init()
engine.say(responses[0])
engine.say("You can ask me to .......Open Google.....,Search on google.....,About me......, Calculation.......,open facebook account...,to Open Gmail")
engine.say("******Plz give me voice command *****")
engine.runAndWait()
engine.stop()
def answer(Txt):
    engine=pyttsx3.init()
    engine.say(Txt)
    engine.runAndWait()
    engine.stop()
print("Plz give me voice command  ")
while Continue:
 r = sr.Recognizer()
 with sr.Microphone() as source:  # use the default microphone as the audio source
   try:
      print("Listening...")
      time.sleep(1)
      audio = r.listen(source)  # listen for the first phrase and extract it into audio data
      Text= r.recognize_google(audio)    # recognize speech using Google Speech Recognition
      print("you Said...")
      print(Text)
      if Text.lower()=='stop':
          exit()
      for word in Text.split(" "):
        if word.lower() in operations.keys():
            try:
                l=extractNofromText(Text)
                r=operations[word.lower()](l[0],l[1])
                answer("Answer Is" +f" {r}")
                time.sleep(1)
                print(r)
                break
            except :
                print("Something is Wrong ,plz Try Again")
                answer("Something is Wrong ,plz Try Again")
                time.sleep(1)
                break
        elif word.lower() in commands.keys():
                answer(commands[word.lower()]())
                time.sleep(1)
                break
        elif word.lower() in open.keys():
               answer(word.lower()+ "Opening")
               webbrowser.open(open[word.lower()])
               time.sleep(1)
               break
        elif word.lower() in search.keys():
               answer(word.lower() + "Opening")
               webbrowser.open(search[word.lower()]+ Text)
               time.sleep(1)
               break
   except sr.UnknownValueError :
       print("Not recognizing")
   except  LookupError:  # speech is unintelligible
       print("Could not understand audio")
 print("Say STOP to pause...")
