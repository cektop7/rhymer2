class Word:
    __VOLWELS = frozenset('аеёиоуыэюя')

    word = None # Слово
    sylCount = None # Количество слогов
    emphasis = set() # Номера ударных слогов
    tail = None # Рифмующиеся окончание
    nextWords = set() # Слова которые могут следовать за данным

    def __init__(self, word):
        self.word = self.__clearWord(word)
        self.sylCount = self.__getSylCount(self.word)
        self.tail = self.__getTail(self.word)

    def __getSylCount(self, word):
        syls = 0
        for letter in word:
            if letter in self.__VOLWELS:
                syls += 1
        return syls

    def __clearWord(self, word):
        return word.strip(' ,.!?;-').lower()

    def __getTail(self, word):
        tail = ''
        for i in range(-1, -len(word)-1, -1):
            tail = word[i] + tail
            if word[i] in self.__VOLWELS:
                if len(tail) > 1:
                    return tail
                elif i > -len(word)-1 and \
                        not word[i-1] in self.__VOLWELS \
                        and not word[i-1] in frozenset('ьъ'):
                    return word[i-1] + tail
                else:
                    return tail

    def groupKey(self):
        return  str(self.sylCount) + '_' + self.tail

    def addNextWord(self, word):
        self.nextWords.add(self.__clearWord(word))

#Tests
w = Word('А тоща, как полвесла! варить')
print(w.word)
print(w.sylCount)
print(w.tail)
w.addNextWord('Первое')
w.addNextWord('Next')
w.addNextWord(' ГдеЖе')
print(w.nextWords)
print(w.groupKey())
