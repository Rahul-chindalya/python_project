# Project Name: Needs and Wants Analyzer

# This project is a simple decision-making program that helps users
# decide whether they should buy a product or not.

# The program checks:
# - The user’s pocket money
# - The price of the product
# - Whether the product is really needed or just a want

# If the product can be bought using pocket money and it is necessary,
# the program suggests buying it.
# If the product is necessary but costs more than pocket money,
# the program suggests asking parents.
# If the product is not necessary and costs more than pocket money,
# the program suggests not buying it.

# The main goal of this project is to encourage thoughtful spending
# and help users understand the difference between needs and wants.

from analyzer import Analyser

analyser=Analyser()

print("*"*50)
print("--------NEED OR WANT ANALYZER--------")
print("*"*50)

while True:
    print("*"*20)
    print("1- CHECK BUYING DECISION")
    print("2-VIEW PAST DECISION")
    print("3-EXIT")
    print("*"*20)
    choice = input("Enter Your Choice: ")

    if choice=="1":
        print("Lests Check If U Really Need It or Want It")
        analyser.making_decision()
    elif choice =="2":
        print("Past Decisions")
        analyser.past_decisions()
    elif choice =="3":
        print("Thank YOU")
        break
    else:
        print("Enter Between (1-3) only!!!!!!!")


