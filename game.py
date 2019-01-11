import sys
import os
#def start():
    

def game_1():
    x=input("Question 1: What must a codon start with?:A=AUG, B=GUA, C=UAG")
    if x=="A":
        game_2()
    elif x=="B":
        print("WRONG.")
        beginning()
    elif x=="C":
        print("WRONG.")
        beginning()
    else:
        print("Input one of the following letters to proceed.")
        game_1()
def game_2():
    x=input("Okay, question 2: What comes first: 1:Transcription, 2:Translation")
    if x=="1":
        game_3()
    elif x=="2":
        print("WRONG.")
        beginning()
    else:
        print("Input one of the following letters to proceed.")
        game_2()
def game_3():
    x=input("Question 3:How many cells does meiosis produce? 1:Two Identical daughter cells, 2:Two unidentical daughter cells, 3: 4 Unidentical daughter cells, 4: 4 Identical daughter cells.")
    if x=="1":
        print("WRONG.")
        beginning()
    elif x=="2":
        print("WRONG.")
        beginning()
    elif x=="3":
        game_4()
    elif x=="4":
        print("WRONG.")
    else:
        print("Input one of the following letters to proceed.")
        game_3()
def game_4():
    x=input("What are the reactants (what is being used) during cellular respiration? (there can be two answers): 1:Glucose, 2: Oxygen, 3: Carbon dioxide, 4: ATP")
    if x=="1":
        game_5()
    elif x=="2":
        game_5
    elif x=="3":
        print("WRONG.")
        beginning()
    if x=="4":
        print("WRONG.")
        beginning()
    else:
        print("Input one of the following letters to proceed.")
        game_4()
def game_5():
    x=input("How much ATP is created during Aerobic respiration? 1:32-38, 2:10, 3:40")
    if x=="1":
        end_screen()
    elif x=="2":
        print("WRONG.")
        beginning()
    elif x=="3":
        print("WRONG")
        beginning()
    else:
        print("Input one of the following letters to proceed.")
        game_5()
def end_screen():
    print("Congrats on aceing this ''Quiz''. Well, I hope this mini game which i have created will help you understand more about Photosynthesis, cellular respiraiton, mitosis, meiosis, DNA, and RNA. :)")
    end()
        
def PM():
    first_choice=input("Okay, photosynthesis is a very interesting process. press enter to continue (return for those playing on an apple)")
    if first_choice=="":
        second_choice=input("Photosynthesis is the conversion of carbon dioxide, and water vapor, into glucose by using sunlight.")
        if second_choice=="":
            third_choice=input("Where as cellular respiration is really the opposite of photosynthesis, where you use glucose, and oxygen, to get carbon dioxide, water vapors, as well as ATP (adenosine triphosphate)")
            if third_choice=="":
                fourth_choice=input("A good way to remember the two, is to think of the two as a cycle, where photosynthesis happens, producing the glucose, then the cellular respiration takes in the glucose, and makes ATP, carbon dioxide, and water, which the carbon dioxide and water are then again used in photosynthesis.")
                if fourth_choice=="":
                    fifth_choice=input("Photosynthesis happens in the chlorophyll, whereas cellular respiration happens in the mitochondria, and there are two versions: Aerobic respiration, and anaerobic respiration.")
                    if fifth_choice=="":
                        sixth_choice=input("For aerobic respiration, Glucose is consumed, which then goes through glycolysis, producing a bit of ATP. If no oxygen is present, then anaerobic respiration(fermentation) will occur after glycolysis, thus completing anaerobic respiration. but, if oxygen is present, then after glycolysis, then the next stage is krebs cycle, of which electrons from the glucose is put on electron carriers,  which then goes on into the Electron transport chain (ETC).")
                        if sixth_choice=="":
                            seventh_choice=input("During ETC, the electrons from the electron carriers go through proteins via active transport, which then travel through a protein called ATP synthase. Essentially a protein which creates protein.")
                            if seventh_choice=="":
                                eighth_choice=input("This creates around 32-38 ATP, where as anaerobic respiration creates less, but at a faster pace since it only has two stages compared to having 4.")
                                if eighth_choice=="":
                                    ninth_choice=input("Photosynthesis is really the opposite, but has two stages, light independent, and light dependent reaction.")
                                    if ninth_choice=="":
                                        tenth_choice=input("Light dependent reaction happens in the Thylakoid, where the ATP is produced via using the sunlight to power the active transport.")
                                        if tenth_choice=="":
                                            eleventh_choice=input("Light independent reaction happens after light dependent reaction, in the Stroma.")
                                            if eleventh_choice=="":
                                                twelveth_choice=input("This is where the ATP produced from the light dependent reaction from earlier is used in order to produce glucose.")
                                                beginning()
                                                
                    
    else:
        print("Just press space bar. that's all")
        start()
def M():
    first_choice_1=input("Mitosis and meiosis have to do with reproduction of cells in the human body. press enter to continue")
    if first_choice_1=="":
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
                                    if first_choice_10=="":
                                        first_choice_11=input("However, there is one stage which happens before either mitosis, or meiosis occurs: Interphase.")
                                        if first_choice_11=="":
                                            first_choice_12=input("Interphase is where the amount of chromatids is doubled.")
                                            if first_choice_12=="":
                                                first_choice_13=input("Thus, after interphase is completed, mitosis or meiosis would begin.")
                                                beginning()
                                    
    else:
        print("Just press space bar. that's all")
        start()
def DNA():
    second_choice_1=input("DNA (Deoxyribonucleic acid) is a molecule which is known for its shape, which is a double helix. DNA's job is to contain all of your genetic information, inside your nucleus, inside a cell.")
    if second_choice_1=="":
        second_choice_2=input("Where as RNA (Ribonucleic Acid) is just a single helix, and is not organized in the same way as DNA.")
        if second_choice_2=="":
            second_choice_3=input("RNA's job is to do protein synthesis. Essentially, a fancy way of saying it produces and creates proteins.")
            if second_choice_3=="":
                second_choice_4=input("There are also three kinds of RNA, rRNA(ribosomal ribonucleic acid), mRNA(Messenger ribonucleic acid), and tRNA(Transfer ribonucleic acid. All three are used when making proteins.")
                if second_choice_4=="":
                    second_choice_5=input("During Protein Synthesis, there are two process which happen in this order: Transcription, and then translation." )
                    if second_choice_5=="":
                        second_choice_6=input("Transcription happens in the nucleus of the cell, and this is where mRNA is created, which the travels to the mitochondria, to then get attached to the mitochondria, to start tranlsation.")
                        if second_choice_6=="":
                            second_choice_7=input("During translation, the mRNA is connected to the mitochondria, and the tRNA, which contains a protein is also connected to the mitochondria which the mRNA is on.")
                            if second_choice_7=="":
                                second_choice_8=input("mRNA contains something called codon, which is a triplet of nucleobases (what makes up the strands of DNA and RNA). Where as tRNA contains anti codon, which connects up with the codon in the mitochondria. The anti codon is really just a codon, but on the tRNA.")
                                if second_choice_8=="":
                                    second_choice_9=input("However, the codon must start with AUG (Adenine, uracil, Guanine).")
                                    if second_choice_9=="":
                                        second_choice_10=input("Adenine must go with Thymine, or Uracil. Uracil in our case because RNA does not contain Thymine, but instead Uracil.")
                                        if second_choice_10=="":
                                            second_choice_11=input("And Cytosine must go with Guanine, or the other way around.")
                                            beginning()
                    
                            
    else:
        print("Just press space bar. that's all")
        start()
               
    
    
    



def beginning():
    choice_1=input("Welcome to this text based game. Would you like to learn about Photosynthesis and cellular respiration (pm), mitosis and meiosis (m), or DNA and RNA (XMA) first? Or, alternatively, if you have completed all three, here is a ''Quiz''(QUIZ).")
    if choice_1=="QUIZ":
        game()
    if choice_1=="pm":
        PM()
    elif choice_1=="m":
        M()
    elif choice_1=="XMA":
        DNA()


    else:
        print("please use one of the 'words' from above to continue.")
        start() 
def game():
    print("Okay, now that you have adequate knowledge on these three topics, I shall ''quiz'' you.")
    game_1()

   


beginning()

