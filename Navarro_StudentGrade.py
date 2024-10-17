#Computing a student grade
name = input("Please enter your name: ")
section = input("Please enter your section: ")
PrelimGrade= float(input("Enter your Prelim Grade (40-100): "))
if PrelimGrade <40 or PrelimGrade > 100:
    print("Invalid input. Your grade must remain between 40 and 100")
else:
    MidtermGrade= float(input("Enter your Midterm Grade (40-100): "))
if MidtermGrade < 40 or MidtermGrade > 100:
    print("Invalid input. Your grade must remain between 40 and 100")
else:
    FinalGrade = float(input("Enter your Final Grade (40-100): "))
if FinalGrade <40 or FinalGrade >= 100:
    print("Invalid input. Your grade must remain between 40 and 100")
else:
    PrelimGrade = PrelimGrade * 0.3333
    MidtermGrade = MidtermGrade * 0.3333
    FinalGrade = FinalGrade * 0.3333
    GPA = PrelimGrade + MidtermGrade + FinalGrade
    GPA = round(GPA)
    
    print()
    print("Hello,", name + "!" )
    print("Section: " + section)
    

#Ratings
if 99 <= GPA <= 100:
    print (" Your GPA is 1.00 = Excellent Student")
elif 96 <= GPA <= 98:
    print ("Your GPA is 1.25 = Oustanding Student")
elif 93 <= GPA <= 95:
    print ("Your GPA is 1.50 = Superior Student")
elif 90 <= GPA <= 92:
    print("Your GPA is 1.75 = Very Good Student")
elif 87 <= GPA <= 89:
    print("Your GPA is 2.00 = Good Student")
elif 84 <= GPA <= 86:
    print ("Your GPA is 2.25 = Satisfactory Student")
elif 81 <= GPA <= 83:
    print ("Your GPA is 2.50 = Fairly Satisfactory")
elif 78 <= GPA <= 80:
    print ("Your GPA is 2.75 = Fair")
elif 75 <= GPA <= 77:
    print ("Your GPA is 3.00 = Passed")
else:
    print("Your GPA is 5.0 = Failed")