import random

def comparer(number, user_input):
    compare=[0,0]
    for i in range(len(number)):
        if number[i] == user_input[i]:
            compare[0]+=1
        elif user_input[i] in number:
            compare[1]+=1
    return compare

if __name__=="__main__":
    playing = True
    number = str(random.randint(0,9999))
    guesses = 0
    #print(number)
    while playing == True:
        user_input= input("enter your guess")
        if user_input == "exit":
            break
        counter = comparer(number,user_input)
        guesses+=1
        print("you have " + str(counter[0]) + " cows, and " +str(counter[1])+" bulls.")

        if counter[0]==4:
            playing = False
            print("You have won the game after " +str(guesses)+"guesses")
            break
        else:
            print("not yet try again")
        
    
                   
