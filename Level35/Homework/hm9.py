#  9) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება ასაკს თუ მისი ასაკი მეტია 18 ზე უთხრას რომ სრულწლოვანია თუარადა არარის
    

def age():
    age = int(input("Enter your age"))
    if age >= 18:
        print("srulclovani")
    else:
        print("ar xaar srulclovani")

age()