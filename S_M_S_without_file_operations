SYSTEM_INFO = ("LMS Student Portal","v1.0","Edify University",2025)
ADMIN_INFO = ("ADMIN@gmail.com","91+9876543210","202")

print("*"*50)
print(f"Wlecome to {SYSTEM_INFO[0]} {SYSTEM_INFO[1]}")
print(f"Developred By {SYSTEM_INFO[3]} In The Year{SYSTEM_INFO[2]}")
print("*"*50)

students={}

def add_student():
    student_id = input("Enter Student ID: " )
    if student_id in students:
        print("ENTER STUDENT ALREADY EXISTS!!")
    else:
        name = input("ENTER STUDENT NAME: ").strip().title()
        scores = []
        while True:
            score_input = input("ENTER YOUR SCORE OR DONE TO STOP: ")
            if score_input =="done" or score_input=="DONE":
                break
            if score_input.isdigit():
                score = int(score_input)
                if 0<=score <=100:
                    scores.append(score)
                else:
                    print("ENTER ONLY BETWEEN 1-100")
            else:
                print("ENTER ONLY NUMBERS")
        skills = set()
        while True:
            skill_input = input("ENTER YOUR SKILLS OR TYPE DONE TO STOP: ")
            if skill_input =="DONE" or skill_input=="done":
                break
            else:
                skills.add(skill_input.strip().title())
        students[student_id]={
            "name":name,
            "scores":scores,
            "skills":skills
        }

        print("STUDENT ADDED SUCCESSFULLY!!")
        print(students)

def modify_student():
    student_id = input("ENTER STUDENT ID: ")
    if student_id in students:
        new_name = input("ENTER NAME TO UPDATE").strip().title()
        students[student_id]["name"] = new_name
        print("Student Updated Successfully")
        print(students)
    else:
        print("ENTER id that exists!!")

def delete_student():
    student_id =input("ENTER STUDENT ID: ")
    if student_id in students:
        removed = students.pop(student_id,None)
        print(removed)
        print("REMOVED SUCCESSFULLY!!!!")
        print(students)
    else:
        print("ENTER A VALID STUDENT ID: ")

def list_students():
    if not students:
        print("NO STUDENT AVAILABLE")
    else:
        print("*"*50)
        for sid,data in students.items():
            name = data["name"]
            scores = data["scores"]
            skills = data["skills"]

            average_score = sum(scores)/len(scores)
            top_score = max(scores)
            
            print(f"Student ID: {sid} ")
            print(f"NAME: {name}")
            print(f"SCORES: {scores}")
            print(f"Average score: {average_score}")
            print(f"Top SCore: {top_score}")
            print(f"Skills: {skills}")
            print(f"Skills: {len(skills)}")
        print("*"*50)

def search_by_skill():
    skill = input("ENTER SKILL TO SEARCH STUDENT: ")
    found = list(filter(lambda item: skill in [s.lower() for s in item[1]["skills"]],students.items()))

    if not found:
        print("NO STUDENT FOUND WITH THIS SKILL")
    for sid,data in found:
        print(f"{sid},{data["name"]},{data["scores"]},{data["skills"]}")

def exit():
    print("*"*50)
    print("Contact admin for help")
    print(f"mobile number{ADMIN_INFO[2]}")
    print(f"Email {ADMIN_INFO[0]}")
    print("*"*50)


while True:
    print("1-Add Student")
    print("2-Modify student")
    print("3-Delete Student")
    print("4-List all students")
    print("5-search students by skills")
    print("6-Exit")

    choice = input("ENTER YOUR CHOICE [1-5]: ")
    if choice =="1":
        print("choice 1")
        add_student()
    elif choice == "2":
        print("choice 2")
        modify_student()
    elif choice == "3":
        print("choice 3")
        delete_student()
    elif choice == "4":
        print("choice 4")
        list_students()
    elif choice == "5":
        print("choice 5")
        search_by_skill()
    elif choice == "6":
        print("choice 6")
        exit()    
