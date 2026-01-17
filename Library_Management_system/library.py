# importing Json to Read and Write Json Files
import json
# importing Date and Time From Builtin Module 
from datetime import datetime
#using Abstraction method For Roles Admin and Users
from abc import ABC,abstractmethod

class LibrarySystem:
    def __init__(self):
        #i have assigned the file name so that if file name changes in future 
        # i can easily change here with out changing multiple places
        self.__book_file ="Library_Management_system/books.json"
        self.__user_file ="Library_Management_system/users.json"
        self.__issued_file="Library_Management_system/issued_books.json"

        #loaded the file before so it can run smoothly and privately 
        # to restrict access  
        self.__books = self.__load(self.__book_file)
        self.__users = self.__load(self.__user_file)
        self.__issued = self.__load(self.__issued_file)

    def __load(self,filename):
        try:
            with open(filename,"r") as file:
                return json.load(file)
        except:
            return{}
        
    def __save(self,filename,data):
        with open(filename,data) as file:
            json.dump(file,data,indent=4)

#----------------About Books--------------#
    def add_book(self,bid,title,author,copies):
        if bid in self.__books:
            return("Book already Exists")
        else:
            self.__books[bid]={
                "title":title,
                "author":author,
                "copies":copies
            }
            self.__save(self.__book_file,self.__books)
            return "Book Added Successfully"
        
    def view_book(self):
        if not self.__books:
            return "No Book Available"
        for bid,data in self.__books.items():
            issued_count = 0
            for b in self.__issued:
                if b ==bid:
                    issued_count +=1
            available = data["copies"]-issued_count 
            print(bid,data["title"],data["author"],"Available",available)
    
    def view_available_books(self):
        for bid,data in self.__books.items():
            issued_count= 0
            for b in self.__issued:
                if b ==bid:
                    issued_count+=1
            if data["copies"]>issued_count:
                print(bid,data["title"],data["author"])
    
    ############## user   ##############

    def add_user(self,uid,name,department):
        if uid in self.__users:
            return "Alredy Registered!!!!!"

        else:
            self.__users[uid]={
                "name":name,
                "department":department
            }
            self.__save(self.__user_file,self.__users)
            return "Registered Student!!!!"
        
    def view_user(self,uid):
        if uid not in self.__users:
            return "NO USER AVAILABLE"
        else:
            data=self.__users[uid]
            return f"uid:{uid},Name:{data["name"]},Department:{data["department"]}"
        
    def view_users(self):
        for uid,data in self.__users.items():
            print(uid,data["name"],data["department"])

    ############ issue and return books  #############

    def issue_book(self,uid,bid):
        ## check the user and book is available or not
        if uid not in self.__users:
            return "User Not Registerd"
        if bid not in self.__books:
            return "Book Not Found"
        ## checks if the asked book is alredy issued or not
        if bid in self.__issued:
            return "Book already Issued"
        
        # checking the book is available or not         
        issued_count = 0
        for b in self.__issued:
            if b ==bid:
                issued_count+=1
        #if the book is not available  in library
        data= self.__books
        if issued_count>= data[bid]["copies"]:
            return "No copies available"
        # if the book is available 
        else:
            self.__issued[bid]={
                "user_id": uid,
                "issue_date": datetime.today().date()
            }
            self.__save(self.__issued_file,self.__issued)
            return"Book issued!!!"
        
    def return_book(self,uid,bid):
        # checks the book in isssued data to confirm
        if bid not in self.__issued:
            return"Book Not Issued"
        # checks the book and user in isssued data to confirm if
        #the user not taken this book throws error
        if self.__issued[bid]!=uid:
            return "This user has not taken this book"
        
        del self.__issued[bid]
        self.__save(self.__issued_file,self.__issued)
        return "Book Returned"
    
    def my_books(self,uid):
        found = False
        ## Check the used id in issued_ data and if available in list printing the book details
        for uid,data in self.__issued.items():
            if data["userd_id"]== uid:
                print(
                    bid,
                    self.__books[bid]["title"],"Issued on",data["issued_date"]
                )
                found =True
        if not found:
            print("No Books Isssued")

    def issued_report(self):
        if not self.__issued:
            print("NO books are currently issued")
            return
        else:
            print("========Issued Books Report========")
            for bid,data in self.__issued.items():
                print("Book Id: ",bid)
                print("Title:" ,self.__books[bid]["title"])
                print("Author",self.__books[bid]["author"])
                print("Issued To:",self.__users[uid],["name"])
                print("Issued on: ",data["issue_date"])
                print("="*40)
                