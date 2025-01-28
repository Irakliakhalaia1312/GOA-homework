#5) შექმენით ლისტი სადაც გექნებათ 1-10 ჩათვლით რიცხვები, შეამოწმეთ რიცხვი ლუწია თუ კენტი და თუ კენტია დაამატეთ ახალ ლისტში 

my_list=[1,2,3,4,5,6,7,8,9,10]

new_list= []

for num in my_list:
    if num % 3 ==0:
        new_list.append(num)
    print("kenti ricxvebi", new_list)

