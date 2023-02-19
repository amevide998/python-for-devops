from random import choices


def fruit():
    fruits = ["apple", "orange", "kiwi", "grape", "durian", "banana"]
    return choices(fruits)[0]
