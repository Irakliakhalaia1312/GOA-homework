# 13) შექმენით ფუნქცია რომელშიც იქნება რიცხვებით სავსე სია შემდეგ კი დაბეჭდავს ამ სიაში არსებული რიცხვების ჯამს


def num():
    list = [25 , 456, 78, 56, 23, 36, 49, 67, 157, 652, 781,]
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    print(sum)

num()