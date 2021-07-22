# дебильный калькулятор v2
from colorama import init
from colorama import Fore, Back, Style

init()

print( Fore.GREEN )

what = input ("что делаем (+,-,/,*,**,)")

print( Fore.CYAN )

a = float( input("Веди первое число: ") )
b = float( input ("Введи второе число: ") )

print( Fore.YELLOW )

if what == "+":
	c = a + b
	print("Результат: " + str(c))
elif what == "-":
	c = a - b	
	print("Результат: " + str(c))
#elif what == "/"
#	c = a / b
#	print("Результат: " + str(c))
#elif what == "*":
#	c = a * b
#	print("Результат: " + str(c))
#eliif what == "**":
#	c = a ** b
#	print("Результат: " + str(c))
#else:
	print(" Выбрана неверная операция! ")
	
