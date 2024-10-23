import pyttsx3
import speech_recognition as sr

def Speech():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        r.adjust_for_ambient_noise(source)  # Adjust for ambient noise to improve accuracy
        print("Say something")
        audio= r.listen(source)
        print("done")

    try:
        text= r.recognize_google(audio)
        print("You say: ",text)
    except Exception as e:
        print(e)
Speech()





