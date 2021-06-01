
while True:
    highSchoolGrade=float(input("Please enter your highschool grade : "))
    QudaratGrade= float(input("Please enter your Qudarat grade : "))
    TahsiliGrade= float(input("Please enter your Tahsili grade : "))



    if (highSchoolGrade > 100 or QudaratGrade > 100 or TahsiliGrade > 100):
        print('grades cannot exceed 100 please re-enter your grades')
        break

    if (highSchoolGrade < 0 or QudaratGrade < 0 or TahsiliGrade < 0):
        print('grades cannot be less than 0 please re-enter your grades')
        break

    cumulativeGPA = (0.4*highSchoolGrade+0.3*QudaratGrade+0.3*TahsiliGrade)
    print("Your Cumulative GPA is: "+ str(cumulativeGPA))

    if (cumulativeGPA > 90):
        print("You can register in College of Engineering, College of Computer Science, and College of Business Management")
        break

    elif (cumulativeGPA > 80):
        print("You can register in College of Computer Science and College of Business Management")
        break

    elif (cumulativeGPA > 70):
        print("You can only register in College of Business Management")
        break

    else:
        print("Sorry, your GPA does not allow you to register in any of our programs")
        break

print("Thank you for using our tool!")
