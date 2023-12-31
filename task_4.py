import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    """Function to convert text to speech"""
    engine.say(text)
    engine.runAndWait()


def take_command():
    """Function to listen for commands"""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"User said: {command}")
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return ""

    return command.lower()


def run_voice_assistant():
    """Function to run the voice assistant"""
    speak("Hello! I'm your voice assistant. How can I help you?")

    while True:
        command = take_command()

        if "hello" in command:
            speak("Hello! How can I assist you?")
        elif "what is your name" in command:
            speak("I am a voice assistant.")
        elif "exit" in command or "bye" in command:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I didn't get that. Could you please repeat?")


if __name__ == "__main__":
    run_voice_assistant()
