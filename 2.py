OpenText = input('Введите открытый текст: ')
FirstAlphabet = ['жщнюр', 'итьцб', 'яме.с', 'выпч ', '-дуок', 'зэфгш', 'ха,лъ']
SecondAlphabet = ['ичгят', ',жьмо', 'зюрвщ', 'ц-пел', 'ъан.х', 'эксшд', 'бфуы ']

if len(OpenText) % 2 != 0:
    OpenText += 'ъ'
OpenText = OpenText.replace('й', 'и')

BigramArray = []
for i in range(0, len(OpenText), 2):
    BigramArray.append(OpenText[i] + OpenText[i + 1])
print(BigramArray)

bi_izm = ''
for IndBigram in BigramArray:
    for i in range(0,7):
        for j in range(0,5):
            if IndBigram[0] == FirstAlphabet[i][j]:
                x1 = i
                y1 = j
            if IndBigram[1] == SecondAlphabet[i][j]:
                x2 = i
                y2 = j
    if x1 != x2:
        y1,y2 = y2,y1
    bi_izm += SecondAlphabet[x1][y1] + FirstAlphabet[x2][y2]
print('Шифртекст: ',bi_izm)

# оптимист - это человек, который еще не читал утренних газет