print("You want to know Hindi meanings of English word,So write in down")

a={"fast":"Jaldi","what":"Kya","attitude":"Bartava","carrot":"Gajar","Carrot":"Gajar"}
b=input("\tEnter English word:- ")
if b in a:
    print("WoW")
else:
    print("So sad,Try again with new word")    

c=(a.get(b))
print("\tYour Hindi word is- ",c)

input()
