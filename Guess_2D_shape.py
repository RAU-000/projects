

import random

scalene = ['3 sides', 'no equal sides','total angles 180', 'no symmetry line']
equilateral = ['3 sides', '3 equal sides','total angles 180', '3 symmetry lines']
circle = ['no side', 'no corners','total angles 360', 'infinite symmetry lines']
square = ['equal sides', 'contain right angles','total angles 360', '2 pair of parallel sides']

random_shape=[scalene,equilateral,circle,square]



def shapes():
    


    
    z = {'scalene': scalene, 'equilateral': equilateral,'circle':circle,'square':square}

    shape_chosen = random.choice(random_shape)
    
    chosen_properties = random.choice(shape_chosen)
    
    
    
    
    if shape_chosen == scalene:
        
        
       
        shape_str = list(z.keys())[0]
    
        

    if shape_chosen == equilateral:
        
        
        
        
        shape_str = list(z.keys())[1]
    
        

    if shape_chosen == circle:
        
        
        shape_str = list(z.keys())[2]


    if shape_chosen == square:
        
        
        shape_str = list(z.keys())[3]
    
       

     
    

    return shape_str,shape_chosen

shape_str,shape_chosen = shapes()
#print(shape_str)
#print(type(shape_str))
#print(shape_chosen)



def guesses():

    guess_random = input("What is your guess?")
       
    numbers = ["0","1","2","3","4","5","6","7","8","9"]

    for i in guess_random:
        
            

        if i in numbers:
            
                

            raise TypeError("Your guess should only contain letters forming a word")
        

        elif len(guess_random) < 4:
            
            raise Exception("Your answer should form at least a 4 letter word")

    


        return guess_random


    

def quiz_questions():

    

   
    
    chosen_properties = random.choice(shape_chosen)
    print(chosen_properties)
    shape_chosen.remove(chosen_properties)
    
    
    
        
     
    guess = guesses()

    if guess == shape_str:
        
                
        
        
        print("correct shape")
    

        
    while guess != shape_str:
        
                    
                            
        print("wait for your next clue")
        chosen_properties = random.choice(shape_chosen)
        print(chosen_properties)
        shape_chosen.remove(chosen_properties)
                          

        guess = guesses()

        if guess == shape_str:
                
        
        
            print("correct shape")
                            


        elif  shape_chosen == []:
                    
                        
                            
            print("no more clues - Game over")

            break

      
        
quiz_questions()
        
        
