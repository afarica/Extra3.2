# Напишите функцию который будет конвертировать Фаренгейт в Цельсии и наоборот.
a=float(input("Enter the degrees:"))
b=input("What to translate?(enter with F or C):")
if b=="C": 
	d=5/9*(a-32)
	print("In °C it will be equated ",d)
elif b=="F":
	s=9/5*a+32
	print("In °F it will be equated ",s)

