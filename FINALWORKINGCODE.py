import sqlite3



conn = sqlite3.connect('TimmyTutorFinal.db')
c = conn.cursor()    
print('''Welcome to Timmy's Tutors, what would you like to do?''')

loop=1
choice=0


while loop==1:
    choice =input("1: Add student\n2: Record Attendance\n3: Record completion\n4: Search Details\n5: Exit\n")
    if choice=='1':
        fName=input('''first name?''')
        lName=input('''last name?''')
        dob=input('''DOB''')
        
        c.execute('''INSERT INTO Students (firstname,lastname,dob) VALUES (?, ?, ?)''',(fName,lName,dob,))
        conn.commit()
        
    elif choice=='2':
        print('Weekend Intesives')
        studentId=input('StudentID?')
        week=input('Week 1 true/false?')
        week2=input('Week 2 true/false?')
        week3=input('Week 3 true/false?')
        weekN=input('Week N true/false?')
        
        c.execute('''UPDATE WeekendIntensives SET week1 = ?, week2 = ?, week3 = ?, weekN = ? WHERE studentid = ? ;''',(week,week2,week3,weekN,studentId,))
        conn.commit()
        
        print('Weekly Meetings')
        week=input('Week 1 true/false?')
        week2=input('Week 2 true/false?')
        week3=input('Week 3 true/false?')
        weekN=input('Week N true/false?')
        
        c.execute('''UPDATE WeeklyMeetings SET week1 = ?, week2 = ?, week3 = ?, weekN = ? WHERE studentid = ? ;''',(week,week2,week3,weekN,studentId,))
        conn.commit()
        
    elif choice=='3':
        studentId=input('Student Id?')
        print('Test Completed?')
        complete1=input('True or False')
        testId=input('Test Id?')
        
        c.execute('''UPDATE Test SET completionStatus = ? WHERE studentID = ? AND testID = ?;''',(complete1,studentId,testId,))
        conn.commit()

        print('Topic completed?')
        complete1=input('True or False')
        topicId=input('Topic Id?')
        
        c.execute('''UPDATE Topic SET completionstatus = ? WHERE studentID = ? AND testid = ?;''',(complete1,studentId,topicId,))
        conn.commit()

        print('Part completed?')
        complete1=input('True or False')
        partId=input('Part Id?')
        
        c.execute('''UPDATE Part SET completionstatus = ? WHERE studentID = ? AND partID = ?;''',(complete1,studentId,partId,))
        conn.commit()
        
    elif choice=='4':
        lastName=input('Last Name?')
        
        c.execute("SELECT *  FROM Students, Badges WHERE Students.lastName LIKE '"+lastName+"' AND Students.studentID = Badges.StudentID;")
        print(c.fetchall())
        conn.commit()
        
    elif choice=='5':
        loop=0
        
conn.close()
