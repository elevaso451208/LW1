import time
import os

def flag():
    white = "\u001b[47m"
    blue = "\u001b[44m"
    red = "\u001b[41m"
    reset = "\u001b[0m"
    print(red + ' '*20 + reset)
    print(white + ' '*20 + reset)
    print(blue + ' '*20 + reset)
    print(blue + ' '*20 + reset)
    print(white + ' '*20 + reset)
    print(red + ' '*20 + reset)

def anim(k):
    kadr_3 = " Ʌ _ Ʌ\n(> o <)  meow~"
    kadr_2 = " Ʌ _ Ʌ\n(> . <)       "
    kadr_1 = " Ʌ _ Ʌ\n(^ w ^)       "
    for i in range(k):
        print(kadr_1)
        time.sleep(1)
        os.system('cls')
        print(kadr_2)
        time.sleep(1)
        os.system('cls')
        print(kadr_3)
        time.sleep(1)
        os.system('cls')
    
def pattern(width, length):
    #print('人')
    w = '\u001b[47m '
    b = '\u001b[0m '
    s = [
        "0000000011100000000",
        "0000000110110000000",
        "0000001100011000000",
        "0001111000001111000",
        "1111000000000001111"
    ]
    for _ in range(length):
        for line in s:
            line *= width
            for sym in line:
                if sym == '0':
                    print(b, end='')
                else:
                    print(w, end ='')
            print(b[:-1])

def ratio():
    f = open(r"C:\Users\Lena\Desktop\Программирование на Питон\sequence.txt").read().split('\n')
    f = [float(i) for i in f]
    all_d = 0; big = 0; small = 0
    for x in f:
        if x >= 0 and x != 5:
            all_d += 1
            if x > 5: big += 1
            else: small += 1
    big_p = round(big*100/all_d)
    small_p = round(small*100/all_d)
    print("Больше 5: \u001b[44m  \u001b[0m \n")
    print("Меньше 5: \u001b[41m  \u001b[0m \n")
    print("\u001b[44m" + big_p*' ' + "\u001b[0m", big_p, '%')
    print("\u001b[41m" + small_p*' ' + "\u001b[0m", small_p, '%')
    print("Примечание: в соответствии с заданием ")
    print("отброшены отрицательные числа и 5")
    print("так как в задании строгое сравнение")

flag()
time.sleep(5)
os.system('cls')
pattern(2,2)
time.sleep(5)
os.system('cls')
anim(3)
time.sleep(5)
os.system('cls')
ratio()
