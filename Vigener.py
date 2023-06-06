Alphabet = list('абвгдежзийклмнопрстуфхцчшщъыьэюя')
OpenText = input('Введите текст: ')
OpenText = list(OpenText.lower())
KeyWord = list(input('Введите ключевое слово: '))
NewAlphabet = []
h = 0

def FormingNewAlphabet():
    for i in range(len(OpenText)):
        if OpenText[i] in Alphabet:
            NewAlphabet.append(KeyWord[(i - h) % len(KeyWord)])
        else:
            NewAlphabet.append(OpenText[i])
            h += 1
    print(NewAlphabet)

ChoiceAction = int(input ('Выберете: зашифровать - 0, расшифровать - 1: '))

def Encrypt():
    for i in range(len(OpenText)):
        if OpenText[i] in Alphabet:
            z = Alphabet.index(OpenText[i])
            x = Alphabet.index(NewAlphabet[i])
            OpenText[i] = Alphabet[(z + x + 1) % 32]
    print('Шифртекст: ', ''.join(OpenText).replace(' ', ''))

def Decrypt():
    for i in range(len(OpenText)):
        if OpenText[i] in Alphabet:
            z = Alphabet.index(OpenText[i])
            x = Alphabet.index(NewAlphabet[i])
            OpenText[i] = Alphabet[z - x - 1]
    print('Открытый текст: ', ''.join(OpenText).replace(' ', ''))

FormingNewAlphabet()
if ChoiceAction == 0:
    Encrypt()
elif ChoiceAction == 1:
    Decrypt()

# оптимист - это человек, который еще не читал утренних газет