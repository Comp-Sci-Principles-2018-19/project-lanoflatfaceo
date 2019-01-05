import sys
import os

    
def PM():
    first_choice=input("Okay, photosynthesis is a very interesting process. press enter to continue (return for those playing on an apple)")
    if first_choice=="":
        second_choice=input("Photosynthesis is the conversion of carbon dioxide, and water vapor, into glucose by using sunlight.")
        if second_choice=="":
            third_choice=input("Where as cellular respiration is really the opposite of photosynthesis, where you use glucose, and oxygen, to get carbon dioxide, water vapors, as well as ATP (adenosine triphosphate)")
            if third_choice=="":
                fourth_choice=input("A good way to remember the two, is to think of the two as a cycle, where photosynthesis happens, producing the glucose, then the cellular respiration takes in the glucose, and makes ATP, carbon dioxide, and water, which the carbon dioxide and water are then again used in photosynthesis.")
        
    else:
        start()
def M():
    first_choice_1=input("Mitosis and meiosis have to do with reproduction of cells in the human body. press enter to continue")
    if first_choice_1=="":
        first_choice_2=input("The difference between the two is with what each one does.")
        if first_choice_2=="":
            first_choice_3=input("Mitosis is the reproduction of body cells, and aids in the growth, repair, and replacement of cells.")
            if first_choice_3=="":
                first_choice_4=input("Where as Meiosis is for sexual rerproduction.")
                if first_choice_4=="":
                    first_choice_5=input("The reason why is because each of the cycles are different.")
                    if first_choice_5=="":
                        first_choice_6=input("Anyways, there are 4 stages which take palce in mitosis, and 8 in meiosis.")
                        if first_choice_6=="":
                            first_choice_7=input("For mitosis in order, Prophase, Metaphase, Anaphase, and finally, Telophase.")
                            if first_choice_7=="":
                                first_choice_8=input("And in Meiosis, Prophase 1, Metaphase 1, Anaphase 1, Telophase 1, Prophase 2, Metaphase 2, Anaphase 2, and finally telophase 2")
                                if first_choice_8=="":
                                    first_choice_9=input("Both essentially do the same things, except for meiosis doing something in Metaphase 1, called crossing over.")
                                    if first_choice_9=="":
                                        first_choice_10=input("Crossing over is when two homologous chromosomes line up together and can share each other's DNA, which gives us traits.")
                
    else:
        start()
def DNA():
    second_choice_1=input("DNA (Deoxyribonucleic acid) is a molecule which is known for its shape, which is a double helix. DNA's job is to contain all of your genetic information, inside your nucleus, inside a cell.")
    if second_choice_1=="":
        second_choice_2=input("Where as RNA (Ribonucleic Acid)")
    else:
        start()
    
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
    
               
    
    
    
