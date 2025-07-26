#Greeting the user
print(f"Welcome to Student Management System!")
print("---------")
student = [{'Name': 'abc', 'Roll no.': '1', 'Maths': 100, 'English': 100, 'Science': 100}, 
           {'Name': 'xyz', 'Roll no.': '2', 'Maths': 88, 'English': 99, 'Science': 80}]

#Making an infinite loop menu
while True:

    print("1.Add a new student")
    print("2.View the present student data")
    print("3.Search for a certain student's info")
    print("4.Update existing details")
    print("5.Delete user data")
    print("6.Exit")
    
    print("---------")

    user_input = int(input("Please select an option from 1-6 : "))
    
    print("---------")

    if user_input == 1:
        #creating a list to store data inside
        student_data = {}
        student_name = input("Enter the name of the student : ")
        student_name = student_name.strip().title()
        student_rollnum = input(f"Enter the Roll Number of the student : ")
        marks_in_maths = int(input(f"Enter marks obtained by {student_name} in Maths : "))
        marks_in_english = int(input(f"Enter marks obtained by {student_name} in English : "))
        marks_in_science = int(input(f"Enter marks obtained by {student_name} in Science : "))
        #Assigining pairs inside of the dict
        student_data["Name"] = student_name
        student_data["Roll no."] = student_rollnum
        student_data["Maths"] = marks_in_maths
        student_data["English"] = marks_in_english
        student_data["Science"] = marks_in_science 
        #Adding the data to the Main list
        student.append(student_data)
        print(f"{student_name}'s data has been added") #Displaying the final result to the user
        
        print("---------")
        

    elif user_input == 2:
        #incase of no date present
        if len(student) == 0:
            print("No student data added!\nEnter the data then view the details again. ")

            print("----------")
        else:
            for details in student:
                
                maths = details["Maths"]
                english = details["English"]
                science = details["Science"]
                #Calculation for Average and total Marks

                total = maths+english+science
                average_marks = round(total/3,2)
                print(f'''The student "{details["Name"]}" has obtained a total of {total} marks in all subjects\nand an average of {average_marks}''')
                
                print("--- ---")
                
                #Remarks
                
                if average_marks >= 90:
                    print(f"Remark : Excellent marks")
                elif average_marks <90 and average_marks >=75:
                    print(f"Remark : Good marks")
                elif average_marks <75 and average_marks >=50:
                    print(f"Remark : Average marks")
                else:
                    print(f"Remark : Need Improvement")

                print("--- ---")

    elif user_input == 3:
        
        inp_find = input("Enter the full name of the students : ").strip().title()
        
        print("----------")
        
        #Setting a flag
        found = False
        
        for details in student:
            
            if details['Name'].lower() == inp_find.lower():
                found = True
                #Defining variables for Total and average
                maths = details["Maths"]
                english = details["English"]
                science = details["Science"]
                
                #Total And Average
                total = maths+english+science
                average_marks = round(total/3,2)
                print(f"Name : {details['Name']}\nRoll Number : {details["Roll no."]}\nMarks in each subject\n**********\nMaths : {details["Maths"]}\nEnglish : {details["English"]}\nScience : {details["Science"]}\n**********\nTotal = {total}\nAverage = {average_marks}\n----------")
                
        
        if not found:
            print("Student not found! Check the name or try again.")

    elif user_input == 4:
        inp_roll = input("Enter the Students Roll no to update : ")
        print("----------")
        #flag
        found1 = False
        for students in student:
            if students["Roll no."] == inp_roll:
                found1 = True
                maths = students["Maths"]
                english = students["English"]
                science = students["Science"]
                print(f"Current Marks\n \nMaths = {maths}\nEnglish = {english}\nScience = {science}")
                print("----------")

                #taking the update
                maths_update = input(f"Maths ({maths}) New Marks or press Enter to keep : ").strip()
                english_update = input(f"English ({english}) New Marks or press Enter to keep : ").strip()
                science_update = input(f"Science ({science}) New Marks or press Enter to keep : ").strip()
                print("----------")

                #Updating

                if maths_update != "":
                    maths_update = int(maths_update)
                    students.update({"Maths": maths_update})
                if english_update != "":
                    english_update = int(english_update)
                    students.update({"English": english_update})
                if science_update != "":
                    science_update = int(science_update)
                    students.update({"Science": science_update})

                print("Marks updated successfully!")
                
                print("----------")
                
        if not found1:
            print("Roll no is invalid.\nPlease check the Student Details and try again!")
            print("----------")
    
    elif user_input == 5:
        pass
    elif user_input == 6:
        break
    else:
        print("Invalid Input;\tPlease enter a correct number")

        print("---------")
     
