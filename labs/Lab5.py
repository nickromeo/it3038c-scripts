import  random

rando = random.randint(1,50)
count = 0
print("Guess my number 1-50. I bet you can't")
userrando = int
while rando != userrando:
    userrando = int(input())
    count += 1
    if userrando < rando :
        print("Your close but a bit more")   

    elif userrando > 50 :
        print("Invalid input try again")
    
    elif userrando > rando :
        print("Woah buddy too much")
     
else:
    print("You got it! The number was", rando ,"and it took you", count, "trys")
