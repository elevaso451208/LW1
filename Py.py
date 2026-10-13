import time
import os

def flag(height,width):
    color = ["\u001b[41m", "\u001b[47m", "\u001b[44m", "\u001b[44m", "\u001b[47m", "\u001b[41m"]
    reset = "\u001b[0m"
    for i in range(len(color)):
        for j in range (height):
            print(color[i] + ' '*20*width + reset)

def anim(k):
    color = ['\u001b[36m', '\u001b[35m', '\u001b[31m']
    kadr = [" Ʌ _ Ʌ\n(> o <)  meow~",
            " Ʌ _ Ʌ\n(> . <)       ",
            " Ʌ _ Ʌ\n(^ w ^)       "
    ]
    os.system('cls')
    for i in range(k*3):
        print(color[i%3]+kadr[i%3])
        time.sleep(1)
        os.system('cls')
    print('\u001b[39m')

def pattern(size, height, width):
    shablon = [['  ']*2*size for _ in range(size)]
    xx = 1
    for y in range(1,size):
        x = size//(size-y)
        for i in range(xx+size-1, x+size):
            shablon[y][i] = '\u001b[47m' + '  ' + '\u001b[0m'
        for i in range(size-x, size+1-xx):
            shablon[y][i] = '\u001b[47m' + '  ' + '\u001b[0m'
        xx = x
    shablon = [shablon[i]*width for i in range(len(shablon))]
    for i in range(height):
        for line in shablon:
            print(*line, sep='')


def ratio():
    file_1 = open(r"C:\Users\Lena\Desktop\Программирование на Питон\sequence.txt")
    file = file_1.read().split('\n')
    file_1.close()
    file = [float(i) for i in file]
    all_d = 0
    big = 0
    small = 0
    for elem in file:
        if elem >= 0 and elem != 5:
            all_d += 1
            if elem > 5: big += 1
            else: small += 1
    big_p = round(big*100/all_d)
    small_p = round(small*100/all_d)
    print("Больше 5: \u001b[44m  \u001b[0m", end = ' '*5)
    print("Меньше 5: \u001b[41m  \u001b[0m \n")
    print("\u001b[44m" + big_p*' ' + "\u001b[0m", big_p, '%')
    print("\u001b[41m" + small_p*' ' + "\u001b[0m", small_p, '%')

def func():
    oxy = [[' ']*100 for _ in range(25)]
    xx = 0
    for y in range(2, 25):
        x = 100//y 
        for i in range(x, xx+1):
            oxy[25-y][i] = '\u001b[47m' + ' ' + '\u001b[0m'
        xx = x
    for line in oxy:
        print(*line, sep = '')


anim(3)
flag(2,3)
pattern(10,2,3)
ratio()
func()
