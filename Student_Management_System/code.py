# ###############################################################################
############################### "Student Management System"######################
#################################################################################

import json

filename = "Student_Management_System/student.json"
students={}

#####################################
# Loading student data
######################################
def load_students():
    global students
    try:
        with open(filename,"r") as file:
            students = json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        students={}
        save_data()
##################################################################
# if the file is in txt format
# ##################################################################
# def load_students():
#     try:
#         with open(filename,'r') as file:
#             for line in file:
#                 sid,name,course,marks = line.strip().split(",")
#                 students[sid]={
#                     "name":name,
#                     "course":course,
#                     "marks":marks
#                 }
#     except FileNotFoundError:
#         open(filename,'w').close

####################################
# save data into file
#####################################
def save_data():
    with open(filename,'w') as file:
        json.dump(students,file,indent=4)


##################################
#adding the student
#################################
def add():
    sid = input("ENTER YOUR ID: ")
    if sid in students:
        print("Student Already Exists!!!")
    else:
        name=input("ENTER YOUR NAME: ").strip().title()
        courses=[]
        while True:
            c=input("ENTER YOUR COURSE OR DONE TO STOP:")
            if c=="done":
                break
            else:
                courses.append(c)
        marks=[]
        while True:
            m = input("ENTER YOYR MARKS: ")
            if m =="done":
                break
            if m.isdigit():
                mark=int(m)
                if 0<=mark <=100:
                    marks.append(mark) 
            else:
                print("ENTER ONLY DIGITS!!!")
        students [sid]={
            "name":name,
            "courses":courses,
            "marks":marks
        }

        save_data()
        print("STUDENT ADDED!!!")


###############################
#View students
################################
def view_all():
    if not students:
        print("NO STUDENT DATA AVAILABLE")
    else:
        print("*"*50)
        for sid,data in students.items():
            name = data["name"]
            courses =data["courses"]
            marks = data["marks"]

            average_score= sum(marks)/len(marks)
            top_score = max(marks)

            print("Student ID: ", sid)
            print("Student Name: ", name)
            print("Courses: ",courses)
            print("Student Marks: ", marks)
            print(" Average: ", average_score)
            print("Higest Score: ", top_score)
        print("*"*50)

###################################
# Student  data
###################################

def view():
    sid = input("ENTER SID: ")
    if sid in students:
        data = students[sid]
        print("Student ID: ",data["name"])
        for courses,marks in zip(data["courses"],data["marks"]):
            print(courses,"->",marks)
    else:
        print("ID does not exist")

#############################################
# Update Student
#############################################
def update():
    sid = input("ENTER SID: ")
    courses=[]
    marks = []
    if sid in students:
        new_name=input("Enter Name To Update:")
        students[sid]["name"]=new_name
        print("NAME UPDATED SUCCESSFULLY!!!")

        ### asking if the user also want to update the course and marks########
        choice = input("Do You Also want to Update Course Name then type (Yes/NO): ").lower()
        if choice=="yes":
            data = students[sid]
            print("Courses",data["courses"])
            old_course=input("Enter Old Course Name: ")
            if old_course not in data["courses"]:
                print("corse  not found")
            else:
                index = data["courses"].index(old_course)

                new_course=input("ENTER COURSE NAME TO ADD: ")
                new_marks= int(input("Enter MARKS TO ADD: "))
                data["courses"][index] = new_course
                data["marks"][index] = new_marks
        elif choice=="no":
            pass
        save_data()
        print("UPDATE SUCCESS!!")
    else:
        print("NO ID EXISTS!!")

######################################
# Delete Course
######################################
def delete():
    sid = input("Enter SID: ")
    if sid in students:
        remove = students.pop(sid,None)
        print(remove)
        print("Removed !!!!")
    else:
        print("NO STUDENT WITH ID ")
####################################
# Exit
#####################################
def exit():
    print("*"*50)
    print("Contact Admin For Help")
    print("*"*50)

#############################################################################

load_students()
while True:
    print("============Student Management System============")
    print("1-ADD Student")
    print("2-View One student")
    print("3-View All student")
    print("4-Update student")
    print("5-Delete student")
    print("6-Exit")
    
    choice = input("Enter Your Choice: ")

    if choice=="1":
        add()
    elif choice=="2":
        view()
    elif choice=="3":
        view_all()
    elif choice=="4":
        update()
    elif choice=="5":
        delete()
    elif choice=="6":
        exit()
        break
    else:
        print("CHOICE 1-6 only")