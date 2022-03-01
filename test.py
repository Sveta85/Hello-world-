#2---------------------
word =input("Введите текст:")
vowels = 0
consonants = 0
for i in word:
    letter = i.lower()
    if letter == "a" or letter == "e" or\
       letter == "i" or letter == "o" or\
       letter == "u" or letter == "y":
        vowels += 1
    else:
        consonants += 1
print("Vowels %i\nConsonants %i" % (vowels, consonants))

#3------------------
import random
sum=0
number1: int = int(input('number1 = '))
number2: int = int(input('number2 = '))
for _ in range(7):
    number3: int = random.randint(1, 20)
    number4: int = random.randint(1, 20)
    print(number3,number4)
    if number1>number2 and number3>number4:
      sum+=1
    print(sum)

#4---------------------------
n = int(input("Сколько будет чисел? "))
d = int(input("Какую цифру считать? "))
count = 0
for i in range(1,n+1):
    m = int(input("Число " + str(i) + ": "))
    while m > 0:
        if m%10 == d:
            count += 1
        m = m // 10

print("Было введено %d цифр %d" % (count, d))

#5-----------------------
str="het 385 @&6 4&&v 4 "
str_number=''
str_digit=''
str_other=''

for i in str:
    if i.isalpha():
        str_number+=i
    elif i.isdigit():
        str_digit+=i
    else:
        str_other+=i
print(f"{str_digit}")

#6-----------------------------
text = 'HjkLM'

pair_lower = 0
pair_upper = 0

for i in range(1, len(text)):
    print(text[i - 1], text[i])
    if text[i - 1].islower() and text[i].islower():
        pair_lower += 1
    if text[i - 1].isupper() and text[i].isupper():
        pair_upper += 1
print('сколько пар (стоят рядом) верхнего регистра:', pair_upper)
print('сколько пар (стоят рядом) нижнего регистра:', pair_lower)
print(text,"Длина:",len(text))
vowels = 0
consonants = 0
for i in text:
    letter = i.lower()
    if letter == "a" or letter == "e" or\
       letter == "i" or letter == "o" or\
       letter == "u" or letter == "y":
        vowels += 1
    else:
        consonants += 1
print("Vowels %i\nConsonants %i" % (vowels, consonants))