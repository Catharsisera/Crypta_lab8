FirstAlphabet = list('жщнюритьцбяме.свыпч -дуокзэфгшха,лъ')
SecondAlphabet = list('ичгят,жьмозюрвщц-пелъан.хэксшдбфуы ')
OpenText = list(input('Введите текст: '))
ChoiceAction = int(input('Выберете: зашифровать - 0, расшифровать - 1: '))

def Encrypt():
    if len(OpenText) % 2 != 0:
        OpenText.append('ъ')

    for i in range(len(OpenText)):
        if OpenText[i] == 'й':
            OpenText[i] = 'и'
    print(OpenText)

    BigramArray = []
    for i in range(0, len(OpenText), 2):
        BigramArray.append(OpenText[i] + OpenText[i + 1])
    print(BigramArray)

    for i in range(0, len(OpenText), 2):        #разбиение на биграммы
        IndFirstSymbolOfBigram = FirstAlphabet.index(OpenText[i])
        IndSecondSymbolOfBigram = SecondAlphabet.index(OpenText[i + 1])

        if int(IndFirstSymbolOfBigram / 5) == int(IndSecondSymbolOfBigram / 5):     #обе буквы биграммы лежат в одной строке
            OpenText[i] = SecondAlphabet[IndFirstSymbolOfBigram]
            OpenText[i + 1] = FirstAlphabet[IndSecondSymbolOfBigram]
        else:
            OpenText[i] = SecondAlphabet[IndSecondSymbolOfBigram - ((int(IndSecondSymbolOfBigram / 5) - int(IndFirstSymbolOfBigram / 5)) * 5)]
            OpenText[i + 1] = FirstAlphabet[IndFirstSymbolOfBigram + ((int(IndSecondSymbolOfBigram / 5) - int(IndFirstSymbolOfBigram / 5)) * 5)]
    print('Шифртекст: ', ''.join(OpenText).replace(' ', ''))

def Decrypt():
    for i in range(0, len(OpenText), 2):  #разбиение на биграммы
        z = SecondAlphabet.index(OpenText[i])
        x = FirstAlphabet.index(OpenText[i + 1])
        if int(z / 5) == int(x / 5):
            OpenText[i] = FirstAlphabet[z]
            OpenText[i + 1] =  SecondAlphabet[x]
        else:
            OpenText[i] = FirstAlphabet[x - ((int(x / 5) - int(z / 5)) * 5)]
            OpenText[i + 1] = SecondAlphabet[z + ((int(x / 5) - int(z / 5)) * 5)]

    if OpenText[-1] == 'ъ':
        OpenText.pop(-1)

    print('Открытый текст: ', ''.join(OpenText).replace(' ', ''))

if ChoiceAction == 0:
    Encrypt()
elif ChoiceAction == 1:
    Decrypt()

# оптимист - это человек, который еще не читал утренних газет