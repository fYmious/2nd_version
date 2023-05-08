import  random

char_input = lambda char: char.lower() if len(char) == len(start_word) or len(char) == 1 else char_input(input('введите одну букву или всё слово: '))
def guess(start_word, final_word):
    while True:
        char = char_input(input('\n' + 'введите букву или всё слово: '))
        if char == start_word:
            break
        elif char in start_word:
            for i in range(len(start_word)):
                if start_word[i] == char:
                    final_word[i] = char
            slovo = ' '.join(final_word)
            print(f'вы угадали букву "{char}"' + '\n' + f'текущее состояние слова: {slovo}')
            final_word = final_word
        elif not(char in start_word):
            slovo = ' '.join(final_word)
            print(f'буквы "{char}" нет в слове' + '\n' +  f'текущее состояние слова: {slovo}')
            final_word = final_word
        if final_word == list(start_word):
            break

while True:
    start_word = ((random.choice([i[:-1] for i in open('sowpods.txt', 'r')])).lower())
    final_word = list('*' * len(start_word))
    guess(start_word, final_word)
    print(f'поздравляем, вы угадали слово "{start_word}"!!!')
    if (input('продолжить c другим словом? (да/нет): ')).lower() in ['нет', 'no', 'не', 'н', 'nope']:
        break 
