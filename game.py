import sys
import os

    
def PM():
    first_choice=input("Okay, photosynthesis is a very interesting process. press enter to continue (return for those playing on an apple)")
    if first_choice=="":
        print("")
    else:
        start()
def M():
    print("Why hello there ya filthy animal")
def DNA():
    print("It is i, the evil memelord XD")

    
choice_1=input("Welcome to this text based game. Would you like to learn about Photosynthesis and cellular respiration (pm), mitosis and meiosis (m), or DNA and RNA (XMA) first?")

if choice_1=="pm":
    PM()
elif choice_1=="m":
    M()
elif choice_1=="XMA":
    DNA()

else:
    print("please use one of the 'words' from above to continue.")
    start() 
    
               
    
    
    
