#12 მომხმარბელს შემოატანინეთ რიცხვი შემდეგ კი მომხმარებლის შემოტანილ რიცხვამდე დაბეჭდეთ რიცხვები და გვერძე მიუწერეთ ლუწია თუ კენტი



num = int(input("enter number: "))




for i in range(1, num ):
    if i % 2 == 0:
        print(f"{i} - luwia")
    else:
        print(f"{i} - kentia")