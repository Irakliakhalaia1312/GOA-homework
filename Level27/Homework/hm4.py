#4) შექმენით სია, სადაც გექნებათ 1-იდან 30-ის ჩათვლით რიცხვები. თქენი დავალებაა რომ ამ სიიდან აირჩიოთ ერთი ინდექსი, მომხმარებელმა კი უნდა შეიყვანოს ის ინდექსი რომელიც თქვენ აირჩიეთ. გამოიყანეთ while loop-ი იმისთვის რომ თუ მომხმარებელმა არ შეიყვანა ის ინდექსი რომელიც თქვენ აირჩიეთ, დაბეჭდოთ მესიჯი "Incorrect, Please try again" და ახლიდან მოსთხოვოს რიცხვის შეყვანა. სხვა შემთხვევაში თუ მომხმარებელმა შეიყვანა ინდექსი რომელიც თქვენ აირჩიეთ,  დაბეჭდეთ "You guessed the number!". სხვა შემთხვევაში თუ მომხმარებლის შეყვანილი რიცხვი არის მეტი 30-ზე, ამოუგდოს მესიჯი "Incorrect, You must enter a number from 1 to 30"


number = list(range(1,31))

while true : 
    user_num = int(input("enter number:"))
    if user_num == 5: 
        print("you guessed the number")

    elif user_num > 30:
        print("incorrect number, try againg")
    else:
        print("you must enter a number from 1 to 10")
