"""


"""


class French_Person1:
    def talk_french(self):
        return "hola"


class EnglishPerson:
    def __init__(self):
        self.words = "speaking english"

    def talk(self):
        print(self.words)


class FrenchToEnglishTranslator(French_Person1, EnglishPerson):
    def talk(self):
        words = self.talk_french()
        # converting french words to english
        words = "hello"
        print(words)


def client_code(Ap2: EnglishPerson):
    Ap2.talk()


def main():
    ap = EnglishPerson()
    client_code(ap)

    fp = French_Person1()
    # client_code(fp)

    t = FrenchToEnglishTranslator()
    client_code(t)


main()
