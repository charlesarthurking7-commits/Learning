import random

def word_generator(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    word = word
    answer = ''
    count = 0
    while answer != word:
        if len(answer) < len(word):
            for i in  range(len(word)):
                position = random.randint(0, (len(letters)-1))
                answer += letters[position]
            count += 1
        else:
            answer  = ''
    
    times = []

    return print(word, answer, count)


word_generator("hello")








