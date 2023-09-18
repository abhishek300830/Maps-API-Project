import pyttsx3
engine = pyttsx3.init()
engine.setProperty("rate", 150)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def convert_text_to_speech(text):
    engine.say(text)
    engine.runAndWait()


