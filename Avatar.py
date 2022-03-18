import pyttsx3
import speech_recognition as sr


class Avatar:

    def __init__(self, name="Elsa"):  # constructor method
        self.name = name
        self.initVoice()
        self.initSR()

    def initSR(self):
        self.sample_rate = 48000
        self.chunk_size = 2048
        self.r = sr.Recognizer()
        self.useSR = False

    def initVoice(self):
        self.__engine = pyttsx3.init()
        self.__voices = self.__engine.getProperty('voices')
        self.__vix = 0
        self.__voice = self.__voices[self.__vix].id
        self.__engine.setProperty('voice', self.__voice)
        self.__engine.setProperty('rate', 200)
        self.__engine.setProperty('volume', 1.0)

    def say(self, words):
        self.__engine.say(words, self.name)
        self.__engine.runAndWait()

    def listen(self, prompt="I am listening, please speak:"):
        words = ""
        if self.useSR:
            try:
                with sr.Microphone(sample_rate=self.sample_rate, chunk_size=self.chunk_size) as source:

                    self.r.adjust_for_ambient_noise(source)
                    self.say(prompt)
                    audio = self.r.listen(source)
                try:

                    words = self.r.recognize_google(audio)
                except sr.UnknownValueError:
                    self.say("Could not understand what you said.")
                    words = False
                except sr.RequestError as e:
                    self.say("Could not request results; {0}".format(e))
                    words = False
                    self.useSR = False
            except:
                self.say(prompt)
                words = input(f"{prompt}")
        else:
            self.say(prompt)
            words = input(prompt)
        return words

    def introduce(self):
        self.say(
            f"Hello. My name is {self.name} and i'll be serving you today")


def main():
    teacher = Avatar("Barb")
    teacher.say("How are you today?")

    word = "hello"
    for letter in word:
        teacher.say(letter)

    words = teacher.listen()
    teacher.say(words)


if __name__ == "__main__":
    main()
