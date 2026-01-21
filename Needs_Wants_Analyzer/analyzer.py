import json
            
class Analyser():
        def __init__(self):
            #i have assigned the file name so that if file name changes in future 
            # i can easily change here with out changing multiple places
            self.__decision_file = "Needs_Wants_Analyzer/decision.json"
            
            #loaded the file before so it can run smoothly and privately 
            # to restrict access 
            self.__decision = self.__load(self.__decision_file)

        def __load(self,filename):
                try:
                    with open(filename,"r") as file:
                        return json.load(file)
                except:
                    {}
            
        def __save(self,filename,data):
                with open(filename,"w") as file:
                    return json.dump(data,file,indent=4)
                
        def making_decision(self):
            # Taking inputs 
            item =input("Enter Item Name:")
            price = int(input("Enter Price of item: "))
            pocket_money=int(input("Enter Your Pocket Money: "))
            
            # Afordability check
            if price <= pocket_money:
                print("item is under budget but doest it really needed")
                print("Lest's Check")
                affordable =True
            else:
                affordable=False
                print(f"{item} price is more than the budget ")

            #asking questions
            q1 =input(f"Is {item} for Study, Health or daily use (YES/NO) ").title()
            q2 = input("Can The Pucrchse be posponded (YES/NO) ").title()
            q3 = input("Will Not Buying Cause any Problem ? (YES/NO) ").title()
            q4 = input(f"Do you have any Alternative of {item} ").title()
            
            needed =False
            if q1=="Yes"and q4!="Yes" :
                needed = True
            elif q2=="No" and q3 =="NO":
                needed =True

            #final decison
            if affordable and needed:
                decision="You Can buy using pocket money"
            elif not affordable and needed:
                decision="Ask Parents"
            elif not affordable and not needed:
                decision="Dont Buy"
            else:
                decision="Optional Buying"

            # Decison result:
            print("*"*20)
            print(f"Item name: {item}")
            print(f"Decison : {decision}")
            print("*"*20)

            self.__decision[item]={
                 "price":price,
                 "pocket_money":pocket_money,
                 "decision":decision
            }
            self.__save(self.__decision_file,self.__decision)
            
        def past_decisions(self):
           for item,data in self.__decision.items():
                print(item,data["price"],data["pocket_money"],data["decision"])
                  