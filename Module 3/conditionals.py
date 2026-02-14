age = 18

if age>=18:
    print("you can vote")
else:
    print("you can not vote")

temperatura=28

if temperatura>30:
    print("Its hot")

elif temperatura>=20 or temperatura <=30:
    print("the weather is good")

else:
    print("its a cold day")

student_gpa = 4.5
student_score = 75

if student_gpa >= 3.5:
    if 50 <= student_score <= 65:
        print("you get partial scholarship")
    elif student_score > 65:
        print("you get full scholarship")
    else:
        print("you dont get scholarship")
else:
    print("student gpa and score are not good")
