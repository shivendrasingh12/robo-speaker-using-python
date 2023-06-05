import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. created by Shivendra ")

    engine = pyttsx3.init()
    while True:
        x = input("Enter what you want me to speak:")
        if x == "q":
            break
        engine.say(x)
        engine.runAndWait()


