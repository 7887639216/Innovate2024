import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to user's voice input
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print("User said:", query)
        return query
    except Exception as e:
        print(e)
        return ""

# Main function to interact with the chatbot
def main():
    speak("Hello! I am your voice-based chatbot. How can I assist you today?")
    
    while True:
        user_input = listen().lower()

        if "hello" in user_input:
            speak("Hello there!")
        elif "how are you" in user_input:
            speak("I'm just a computer program, so I don't have feelings, but thank you for asking!")
        elif "what is your name" in user_input:
            speak("I'm a voice-based chatbot.")
        elif "exit" in user_input:
            speak("Goodbye!")
            break
        else:
            speak("I'm sorry, I didn't understand that. Can you please repeat?")
        
if __name__ == "__main__":
    main()
