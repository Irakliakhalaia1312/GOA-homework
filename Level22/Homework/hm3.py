#3 მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი ერთიდან ამ რიცხვამდე დაბეჭდეთ ყველა რიცხვის კვადრატის ჯამი

num = int(input("enter number :"))

sum = 0

for i in range(num):
    sum += (i * i)

print(sum)                