class Student:
    def __init__(self,name,roll,maths,english,science):
        self.name = str(name.strip().title())
        self.roll_no = str(roll)
        self.maths = int(maths)
        self.eng = int(english)
        self.sci = int(science)
    
    def show_details(self):
        print(f"Student's name : {self.name}")
        print(f"Roll no. : {self.roll_no}")
        print(f"Marks (Maths, English, Science) : {self.maths}, {self.eng}, {self.sci}")

    def update_marks(self,subject,new_marks):
        subject = subject.lower().strip() #dont add the self.'something' to prevent it from becoming a Global scope/variable
        new_marks = int(new_marks)
        #Validating marks
        if not (new_marks >= 0 and new_marks <= 100):
            raise Exception('Range Error: enter a number in the range 0-100')
        #Updating specific subjects
        if subject == 'maths':
            self.maths = new_marks
            print(f"Subject marks updated to {new_marks}")
        elif subject == 'english':
            self.eng = new_marks
            print(f"Subject marks updated to {new_marks}")
        elif subject == 'science':
            self.sci = new_marks
            print(f"Subject marks updated to {new_marks}")
        else:
            raise Exception('Invalid subject')
        
    def marks_summary(self):
        #total marks
        total = self.maths + self.eng + self.sci
        #calculating avg
        avg = total / 3
        #Grades according to marks
        if avg >= 90:
            Grade = 'A'
        elif avg >= 75:
            Grade = 'B'
        elif avg >= 50:
            Grade = 'C'
        else:
            Grade = 'D'
        #Final result
        summary = {'name' : self.name,
                'roll no' : self.roll_no,
                'total' : total,
                'average' : round(avg,2),
                'grade' : Grade
                }
        # Optional: print in a nice format
        print(f"\n--- Marks Summary for {self.name} ---")
        print(f"Total: {total}")
        print(f"Average: {round(avg,2)}")
        print(f"Grade: {Grade}")
        
        return summary


s1 = Student("husam", "101", 90, 85, 88)




