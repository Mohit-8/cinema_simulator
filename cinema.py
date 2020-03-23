films={
    "finding Dory":[3,5],
    "Bourne":[18,5],
    "Tarzan":[15,5],
    "Ghost Busters":[12,5]
    }
while True:

    choice=input("What film will you like to watch?").strip().title()

    if choice in films:
        age=int(input("How old are you: ").strip())

        if age>=films[choice][0]:
            seats=films[choice][1]

            if seats>0:
                 print("Enjoy the film!")
                 films[choice][1]=films[choice][1]-1
            else:
                print("sorry we are sold out!")
        else:
            print("You dont have the required age.")
    else:
        print("We dont have that film")
            

                 
        
    
