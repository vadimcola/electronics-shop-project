from src.item import Item


class MixinLang:
    def __init__(self, language="EN"):
        self.__language = language

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
            return self
        elif self.__language == "RU":
            self.__language = "EN"
            return self

    @property
    def language(self):
        return self.__language


class KeyBoard(Item, MixinLang):
    def __init__(self, name, price, quantity, language="EN"):
        super().__init__(name, price, quantity)
        self.__language = language

