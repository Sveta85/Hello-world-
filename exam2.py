#1----------------------
a=[14,5,1,8,6,66,22,1,22,66]
for i in range(len(a)):
        s=a.count(a[i])
        if s==1:
            print(a[i])

#2-----------------------
k = 0
a = [14,5,1,4,8,6,66,1,22,66]
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            k += 1
print(k)
#3-------------------
C_1 = (35, 78,21,37, 2,98, 6, 100, 231)
C_2 = (45, 21,124,76,5,23,91,234)
sumC_1=sum(C_1)
sumC_2=sum(C_2)
if sumC_1>sumC_2:
    print("Сумма больше в кортеже-C_1")
else:
    print("Сумма больше в кортеже-C_2")
print('min',min(C_1),'min',min(C_2))
print('max',max(C_1),'max',max(C_2))

#4-------------------
s = 'An apple a day keeps the doctor away'
s1 = ''.join(s.split())
my_dict = {i: s1.count(i) for i in s1}
print(my_dict)

#5-----------------------
products={"cake":[['suger', 'butter', 'eggs','cream'],5,500],
         "maffin":[['suger', 'butter', 'eggs','jam'],6,600],
         "chocolate_cake":[['chocolate','suger', 'butter', 'eggs','cream'],10,1000]}
for key,value in products.items():
    print(key,'-',value[0])
    cont=0
for key,value in products.items():
    print(key,'-',value[1])
    cont=0
for key,value in products.items():
    print(key,'-',value[2])
    cont=0
for key,value in products.items():
    print(key,'-',value[0],'-',value[1],'-',value[2])
    cont=0
cost=0
while True:
    product=input("What?(n-nothing)")
    if product=='n' or product not in products.keys():
        break
    qty=int(input("How much?"))
    if qty>products[product][2]:
        print("We don't have so much.")
        continue
    cost=products[product][1]*qty
    products[product][2]-=qty
print("Price:",cost)

for key, value in products.items():
    print(key,'-',value[1],'-',value[2])


#6-----------------------
a=[1,2,7,1,4,5,4,1]
b=[2,5,1,4,5,8,8,9]
result = [elem for elem in a if elem in b]
print(result)

#7-----------------
try:
    a=int(input("Введите первое число:"))
    b=int(input("Введите второе число:"))
    c=a/b
except ZeroDivisionError:
    print("Что-то пошло не так.")
else:
    print("Результат в квадрате:",c**2)
finally:
    print("Конец.")

#8---------------------------
with open("klass1.txt",'r',encoding="utf=8") as file:
    counter = summa = 0
    for line in file:
        counter += 1
        length_line = len(line)
        for i in range(length_line):
            if line[i].isdigit():
                num = int(line[i])
                summa += num
                if num < 3:
                    print("Ученик(ца) у которого средний балл по классу меньше 3-х:", line)
                break

    sred = counter / summa
    print("\nСредний балл по классу:", sred)




