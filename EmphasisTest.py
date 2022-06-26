import os, time, random


class color:
    ResetAll = "\033[0m"
    Bold = "\033[1m"
    Underlined = "\033[4m"
    Default = "\033[39m"
    Black = "\033[30m"
    Red = "\033[31m"
    Green = "\033[32m"
    Yellow = "\033[33m"
    Blue = "\033[34m"
    Magenta = "\033[35m"
    Cyan = "\033[36m"
    LightGray = "\033[37m"
    DarkGray = "\033[90m"
    LightRed = "\033[91m"
    LightGreen = "\033[92m"
    LightYellow = "\033[93m"
    LightBlue = "\033[94m"
    LightMagenta = "\033[95m"
    LightCyan = "\033[96m"
    White = "\033[97m"


FILE_PATH = "EmphasisList.txt"
COLORS = color()
VOWELS = ["а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е"]
random.seed(time.time())
WA = set()
ANS_TIME = []
REPLACE_YO_TO_E = True

"""
EmphasisList.txt --- файл, содержащий список слов с ударениями
Например:
...
дефИс
дешевИзна
...
"""
assert os.path.isfile(FILE_PATH), "[ERROR] File not found!"
with open(FILE_PATH, "r", encoding="utf-8") as empFile:
    wordsList = empFile.readlines()
    wordsList = list(map(lambda x: x.strip().rstrip("\n"), wordsList))
    wordsList = list(set(wordsList))

random.shuffle(wordsList)


def main():
    for number, word in enumerate(wordsList):
        print(color.DarkGray + "############################" + color.ResetAll)
        MAX_WIDTH = os.get_terminal_size().columns
        print(
            f"{color.Underlined}Вопрос #{number + 1}/{len(wordsList)}:{color.ResetAll}"
        )
        if REPLACE_YO_TO_E:
            word = word.replace("Ё", "Е")

        lowerWord = word.lower()

        vowelInds = []
        for i in range(len(lowerWord)):
            if lowerWord[i] == "(":
                break
            if lowerWord[i] in VOWELS:
                vowelInds.append(i)
        random.shuffle(vowelInds)

        correctAns = 1
        for ansNumber, ind in enumerate(vowelInds):
            ansWord = (
                lowerWord[:ind] + lowerWord[ind].capitalize() + lowerWord[ind + 1 :]
            )
            if ansWord == word:
                correctAns = ansNumber + 1
            if ansNumber % 2 == 0:
                print(color.LightYellow + f"({ansNumber + 1})" + color.ResetAll, end="")
            else:
                print(f"({ansNumber + 1})", end="")
            print(
                f" {lowerWord[:ind] + color.Blue + color.Bold + lowerWord[ind].capitalize() + color.ResetAll + lowerWord[ind + 1:]}"
            )

        startTime = time.time()

        while True:
            ans = input(color.Underlined + "Ваш ответ:" + color.ResetAll + " ")
            try:
                int(ans)
            except ValueError:
                print(color.Red + "Некорректный ответ!" + color.ResetAll)
            else:
                if 0 < int(ans) <= len(vowelInds):
                    if int(ans) == correctAns:
                        print(color.Green + "Правильно!" + color.ResetAll)
                        break
                    else:
                        print(color.Red + "Неправильный ответ!" + color.ResetAll)
                        WA.add(word)
                else:
                    print(color.Red + "Некорректный ответ!" + color.ResetAll)

        endTime = time.time()
        ANS_TIME.append(endTime - startTime)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()

    print(color.DarkGray + "############################" + color.ResetAll)

    if len(WA) > 0:
        print("Неправильно отвеченные вопросы:")
        for word in list(sorted(WA, key=str.lower)):
            print(word)
        print(color.DarkGray + "############################" + color.ResetAll)

    if len(ANS_TIME):
        print(f"Тест пройден за {round(sum(ANS_TIME) / 60, 2)} минут!")
        print(
            f"Потрачено примерно по {round(sum(ANS_TIME) / len(ANS_TIME), 2)} секунд на вопрос"
        )

    print(color.ResetAll)
