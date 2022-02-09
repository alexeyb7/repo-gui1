nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
from random import choice

def get_jokes(count: int) -> list:
#    from random import choice
    """Возвращает список шуток в количестве count"""
    """ с разрешенным повтором случайно выбирает значения из списков """
    list_out = [choice(nouns) + ' ' + choice(adverbs) + ' ' + choice(adjectives)
                for i in range(count)]
    return list_out


#print(get_jokes(2))
#print(get_jokes(10))


# Раскомментируйте для реализации подзаданий: документирование, флаг и именованные аргументы
    """ unicum - флаг уникальности """


def get_jokes_adv (count, unicum) -> list:
    """Возвращает список шуток в количестве count"""
    if  unicum:
        list_out = [nouns.pop() + ' ' + adverbs.pop() + ' ' + adjectives.pop()
                for i in range(count)
                if len(nouns) and len(adverbs) and len(adjectives)]
    else:
        list_out = [choice(nouns) + ' ' + choice(adverbs) + ' ' + choice(adjectives)
                for i in range(count)]
    return list_out


#print(get_jokes_adv(count = 6, unicum = True))
print(get_jokes_adv(count = 4, unicum = True))