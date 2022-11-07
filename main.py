import pyttsx3
import speech_recognition as sr
import tkinter as tk
#from tkinter import ttk as tkk
#from tkinter import filedialog, Text
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
engine.setProperty('rate', 140)

#s = tkk.Style()
#s.configure('black', background='black')
#s.configure('yellow', background='yellow')
def speak(text):
    engine.say(text)
    engine.runAndWait()

def printAndSpeak(text):
    text_box.insert(tk.END, text+"\n")
    text_box.update()
    speak(text)


def getCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        printAndSpeak("Podaj komendę.....")
        #print("Podaj komendę.....")
        audio=r.listen(source)
        try:
            printAndSpeak("Trwa rozpoznawanie.....")
            query=r.recognize_google(audio, language='pl')
        except Exception as e:
            printAndSpeak("Spróbuj ponownie...")
            #print("Spróbuj ponownie...")
            return "None"
        return query

def makeCommand():
    while True:
        text_box.delete('1.0', tk.END)
        query = getCommand().lower()
        print(query)
        if 'włącz światło' in query:
            printAndSpeak("Włączono światła")
            frame1.configure(bg="yellow")
            frame2.configure(bg="yellow")
            frame3.configure(bg="yellow")
            frame4.configure(bg="yellow")
        elif 'wyłącz światło' in query:
            printAndSpeak("Wyłączono światła...")
            frame1.configure(bg="black")
        else:
            printAndSpeak("Spróbuj ponownie...")
        #    takeCommand()
        return

root = tk.Tk()
canvas  = tk.Canvas(root, height=550, width=400, bg="lightblue")
canvas.grid(columnspan=3)

frame1 = tk.Frame(root, bg='black')
frame1.place(width=120, height=120, x=60, y=60)


frame2 = tk.Frame(root, bg='black')
frame2.place(width=120, height=120, x=240, y=60)

frame3 = tk.Frame(root, bg='black')
frame3.place(width=120, height=120, x=60, y=240)

frame4 = tk.Frame(root, bg='black')
frame4.place(width=120, height=120, x=240, y=240)

text_box=tk.Text(root, height=100, width=100)
text_box.insert(1.0, "Witaj!\nKliknij przycisk aby rozpocząć nasłuchiwanie")
text_box.place(x=0, y=400)
#text_box.grid(column=1, row=2)

recognize_txt=tk.StringVar()
recognize_btn=tk.Button(root, textvariable=recognize_txt, bg="purple", command=lambda:makeCommand())
recognize_txt.set("Nasłuchuj")
recognize_btn.place(x=180, y=370)
#recognize_btn.grid(column=1,row=3)

#finish_txt=tk.StringVar()
#finish_btn=tk.Button(root, textvariable=finish_txt, bg="purple")
#finish_txt.set("Zakończ")
#finish_btn.grid(column=2,row=3)


#instructions = tk.Label(root, text="Siema")
#instructions.grid(columnspan=3, column=0, row=3)

root.mainloop()

#if __name__ == '__main__':
