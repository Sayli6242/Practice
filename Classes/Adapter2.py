"""


"""


class French_Person1:
    def __init__(self):
        self.talk = []

    def gettalk(self, talk):
        self.talk = talk

    def print(self):
        print(self.talk)


class Translator(French_Person1):
    def __init__(self, listen):
        self.listen = listen

    def gettalk(self, talk):
        self.listen.gettalk([])

    def getlisten(self, listen):
        self.listen = listen


class French_to_English_Translator(Translator):
    def __init__(self, talk):
        self.talk = talk

    def listen(self):
        self.talk.gettalk(["hi, good morning"])


class American_Person2:
    def __init__(self):
        pass

    def settranslator(self, translator):
        self.translator = translator

    def gettalk(self):
        return self.translator.listen()


def main():
    Fp = French_Person1()
    T = Translator()
    AP = American_Person2()
    AP = French_to_English_Translator(T)

    main()
