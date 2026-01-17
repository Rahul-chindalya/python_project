# Importing Liberary Module Whcich contains All Classes and Methods
from library import LibrarySystem 
#using Abstraction method For Roles Admin and Users
from abc import ABC,abstractmethod

#using Abstraction 
class user(ABC):
    def __init__(self,system):
        self.system =system

    @abstractmethod
    def show_menu():
        pass

class Admin(user):
    def show_menu(self):
        while True:
            print("-----Admin Menu-----")
            print("1-Add Book")
            print("2-View Book")
            print("3-Register user")
            print("4-View User")
            print("5-View Users")
            print("6-Issue Books")
            print("7-Return Book")
            print("8-Issued Books Report")
            print("9-Logout")

            admin_no = input("Enter Choice: ")

            if admin_no == "1":
                print(self.system.add_book(
                    input(" Book ID: "),
                    input("Title: "),
                    input("Author Name:"),
                    input("Copies: ")
                ))
            elif admin_no == "2":
                self.system.view_books()
            elif admin_no == "3":
                print(self.system.add_user(
                    input("User Id: "),
                    input("Name: "),
                    input("Department: ")
                ))        
            elif admin_no == "4":
                print(self.system.view_user(
                    input("USer Id: ")
                ))
            elif admin_no == "5":
                self.system.view_users()
            elif admin_no == "6":
                print(self.system.issued_book(
                    input("User ID: "),
                    input("Book Id: ")
                ))
            elif admin_no == "7":
                print(self.system.return_book(
                    input("User ID: "),
                    input("Book Id: ")
                ))
            elif admin_no == "8":
                self.system.issued_report()
            elif admin_no == "9":
                break
            else:
                print("Plese Enter Choice Between (1-8)")


class StudentMenu(user):
    def show_menu(self):
        while True:
            print("-----Student Menu-----")
            print("1-View Available Books")
            print("2-Borrow Book")
            print("3-Return Book")
            print("4-My Books")
            print("5-Logout")
            
            std_choice= input("ENTER Choice: ")   
            if std_choice =="1":
                self.system.view_available_books()
            elif std_choice =="2":
                print(self.system.issue_book(
                    input("User Id: "),
                    input("Book Id: ")
                ))
            elif std_choice =="3":
                print(self.system.return_book(
                    input("User Id: "),
                    input("Book Id: ")
                ))
            elif std_choice =="4":
                print(self.system.my_books(
                    input("User Id: ")
                ))
            elif std_choice =="5":
                break
            else:
                print("Plese Enter Choice Between (1-5)")


print("="*50)
print("PUBLIC LIBRARY MANAGEMENT SYSTEM")
print("="*50)

system=LibrarySystem() 

# selecting Role and performing task according to it
while True:
    print("------LIBRARY MANAGEMENT SYSTEM------")
    print("1- Admin Login")
    print("2- Student Login")
    print("3- Exit")

    role= input("Select Role: ")
    if role=="1":
        Admin(system).show_menu()
    elif role=="2":
        StudentMenu(system).show_menu()
    elif role=="3":
        break
    else:
        print("Plese Enter Choice Between (1-3)")