import random
print("Let's compare numbers!")
print("Type 'greater', 'less' or'equal'")
score = 0

for i in range(3):
    a = random.randint(1,100)
    b = random.randint(1,100)

    print(f"\nWhich is true about {a} and {b}?")
    answer = input("Your answer (greater / less/ equal):").lower()

    # Check the correct answer 
    if a > b and answer == "greater":
        print(" Yes! You're right")
        score +=1
    elif a < b and answer == "less":
        print(" Goood job That's correct")
        score +=1
    
    elif a == b and answer == "equals":
        print(" Yay! You got it ")
        score +=1


    else:
        print(" Ooops! Not quite.")
        if a > b:
            print(f"The right answer is: {a} is greater than {b}")
        elif a < b:
            print(f"The right answer is: {a} is less than {b}")
        else :
            print(f"The right answer is: {a} is equal to {b}")

print(f"\n All done! You got {score} out of 3 correct!")            
    
    



    

        