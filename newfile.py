print('1st program')
print(9**0.5*5)#15.0
print('2nd program')
print(9.99>9.98 and 1000!=1000.1)#True
print('3rd program')
print(2*2+2)#6
print((2+2)*2)#8
a=2*2+2#6
b=(2+2)*2#8
print(a==b)#False
print('4th program')
#1 символ после запятой получить
s='123.456' #берем строку
f=float(s)#преобразуем в тип float
f=f*10 #1234.56
f=int(f) #обрезаем дробную часть 1234
f=f%10#остаток от деления на 10
print(f)#выводим 4

#хотел так решить)))
s='123.456'
f=float(s)#переводим во float
f=f-int(f)#получаем дробную часть
s=str(f)#переводим в строку
print(s[2])#наш символ 


#решил бы так
s='123.456'
print(s[s.find('.')+1])#лучший вариант


