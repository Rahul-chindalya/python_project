# Importing Liberary Module Whcich contains All Classes and Methods
import library

def admin_menu():
    while True:
        print("-----Admin Menu-----")
        print("1-Add Book")###
        print("2-View Book")###
        print("3-Register user")##
        print("4-View User")##
        print("5-View Users")##
        print("6-Issued Books")
        print("7-Return Book")#
        print("8-Issued Books Report")
        print("9-Logout")#

        admin_no = input("Enter Choice: ")

        if admin_no == "1":
            pass
        elif admin_no == "2":
            pass
        elif admin_no == "3":
            pass        
        elif admin_no == "4":
            pass
        elif admin_no == "5":
            pass
        elif admin_no == "6":
            pass
        elif admin_no == "7":
            pass
        elif admin_no == "8":
            pass
        elif admin_no == "9":
            break
        else:
            print("Plese Enter Choice Between (1-8)")


def student_menu():
    while True:
        print("-----Student Menu-----")
        print("1-View Available Books")#####
        print("2-Borrow Book")#
        print("3-Return Book")#
        print("4-My Books")
        print("5-Logout")#
        
        std_choice= input("ENTER Choice: ")   
        if std_choice =="1":
            pass
        elif std_choice =="2":
            pass
        elif std_choice =="3":
            pass
        elif std_choice =="4":
            pass
        elif std_choice =="5":
            break
        else:
            print("Plese Enter Choice Between (1-5)")


print("="*50)
print("PUBLIC LIBRARY MANAGEMENT SYSTEM")
print("="*50)

# selecting Role and performing task according to it
while True:
    print("------LIBRARY MANAGEMENT SYSTEM------")
    print("1- Admin Login")
    print("2- Student Login")
    print("3- Exit")

    role= input("Select Role: ")
    if role=="1":
        admin_menu()
    elif role=="2":
        student_menu()
    elif role=="3":
        break
    else:
        print("Plese Enter Choice Between (1-3)")