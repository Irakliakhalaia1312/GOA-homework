#2) შექმენით ლისტი სადაც გექნებათ 1-10 ჩათვლით რიცხვები და დაპრინტეტ მოლოდ კენტი რიცხვები

my_number=[1,2,3,4,5,6,7,8,9,10]


for i in range(len(my_number)):
    if my_number[i] % 3 ==0:
        print(my_number[i])