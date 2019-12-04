import pyttsx3
import speech_recognition as sr
import pyaudio
import webbrowser
import os
Text=''

responses=["Welcome to the interface of DummyAI\n***** I am Ram *****","MY name is Ram","Thanks for using me","Sorry , Its beyond my reach"]
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
            break
        l+=1
def Hcf(a,b):
    while(a):
        a,b=b,a%b
        print(a)
def things():
    print("I can Open Google,facebook account,Gmail,search on google ,do Calculation and Explain mysel")
def Add(*a):
    s=0
    for v in a:
        s+=v
    print(s)
def Sub(a,b):
    s=a-b if a>b else b-a
    print(s)
def Mul(*a):
    s=1
    for v in a:
        s*=v
    print(s)
def Div(a,b):
    if b==0:
        raise ZeroDivisionError("Invalid attempt ,Try again")
    else:
        print(a/b)
def end():
    print(responses[2])
    input("Press enter key to Exit")
    exit()
def name():
    print(responses[1])
def sorry():
    print(responses[3])
def yourself():
    print("I am Dummy AI.Artificial intelligence (AI) is the simulation of human intelligence processes by machines")
operations={"plus":Add,"add":Add,"addition":Add,"sum":Add,"minus":Sub,"subtraction":Sub,"sub":Sub,"subtract":Sub,
            "multiplication":Mul,"multiply":Mul,"mul":Mul,"div":Div,"divide":Div,"division":Div,"lcm":Lcm,"hcf":Hcf}
commands={"name":name,"sorry":sorry,"end":end,"exit":end,"work":things,"things":things,"capable":things,"yourself":yourself}
open={"facebook":"www.facebook.com","google":"www.google.com","gmail":"www.gmail.com","search":"https://www.google.co.in/search?client=opera&q="}

print(responses[0])
engine = pyttsx3.init()
engine.say(responses[0])
engine.say("You can ask me to .......Open Google.....,Search on google.....,About me......, Calculation.......,open facebook account...,to Open Gmail")
engine.say("******Plz give me voice command *****")
engine.runAndWait()
engine.stop()
print("Plz give me voice command  ")
r = sr.Recognizer()
with sr.Microphone() as source:                # use the default microphone as the audio source
   try:
      print("Listenning........")
      audio = r.listen(source)  # listen for the first phrase and extract it into audio data
      Text= r.recognize_google(audio)    # recognize speech using Google Speech Recognition
      print("you Said.........")
      print(Text)
   except  LookupError:                            # speech is unintelligible
        print("Could not understand audio")


for word in Text.split(" "):
        if word.lower() in operations.keys():
            try:
                l=extractNofromText(Text)
                r=operations[word.lower()](l[0],l[1])
                print(r)

            except :
                print("Something is Wrong ,plz Try Again")
                break
        elif word.lower() in commands.keys():
                commands[word.lower()]()
                break
        elif word.lower() in open.keys():
               webbrowser.open(open[word.lower()]+Text)

