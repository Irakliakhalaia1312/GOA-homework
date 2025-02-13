#7) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს შემდეგ კი დაბეჭდავს ეს რიცხვი ლუწია თუ კენტი

def nums():
    x = int(input("Enter your number"))
    if x % 2 ==0:
        print("luci")
    else:
        print("kenti")

nums()            