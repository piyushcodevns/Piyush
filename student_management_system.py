student=[]
def add_student(roll,name,age,grade):
    student.append({'roll':roll,'name':name,'age':age,'grade':grade})
    print("student added sucessfully")
def view_students():
    for i in student:
        print(i)
def search_student(roll):
    for i in student:
        if i['roll']==roll:
            print(i)
            return
    print("student not found")
def update_student(roll,name=None,age=None,grade=None):
        for i in student:
            if i[student]==roll:
                if name:
                    i[name]=name
                    if age:
                        i[age]=age
                        if grade:
                            i[grade]=grade
                            print("student upgrade sucessfully")
                            return
                        print("Student not found")
def delete_student(roll):
                            for i in student:
                                if i['roll']==roll:
                                    student.remove(i)
                                    print("Student deleted sucessfully")
                                    return
                                print("Student not found")
def exit():
                            print("Exiting the system")
                            exit()
print("=======student management system=======")
print("1.Add student")
print("2.View students")
print("3.Search student")
print("4.Update student")
print("5.Delete student")
print("6.Exit")
while True:
    choice=int(input("enter ur choice"))
    if choice==1:
        roll=int(input("enter roll number"))
        name=input("enter name")
        age=int(input("enter age"))
        grade=input("enter grade")
        add_student(roll,name,age,grade)
    elif choice==2:
        view_students()
    elif choice==3:
        roll=int(input("enter roll number to search"))
        search_student(roll)
    elif choice==4:
        roll=int(input("enter roll number to update"))
        name=input("enter new name (press enter to skip)")
        age=input("enter new age (press enter to skip)")
        grade=input("enter new grade (press enter to skip)")
        update_student(roll,name if name else None,age if age else None,grade if grade else None)
    elif choice==5:
        roll=int(input("enter roll number to delete"))
        delete_student(roll)
    elif choice==6:
        exit()