print ("Welcome to DOOM(game) ")
name = input("What is your name? ")
age = int(input("what is your age? "))
print("Hello", name, "you are", age)
health = 10
print("you have starting hp of", health)
def remove_health (damage):
    global health
    health -= damage
    print("{} has recieved damage of {} and has this hp {}".format(name, damage, health))
    
if age >= 18:
    wants_to_play = input("Do you want to join doom?(yes/not)").lower()
    if wants_to_play == "yes":
        print("LETS DOOM")
        left_or_right = input("First choice... Left or Right (left/right)?").lower()
        if left_or_right == "left":
            ans = input("Nice, you follow the path and reach a lake... do you swim across or go aroud (across/around)? ")
            if ans == "around":
                print("You went around and reached the other side of the lake")

            elif ans == "across":
                print("You managed to get across, but were bit by a shark ")
                remove_health(5)
            ans = input("You notice a house and a river. Which do you go to (river/house)? ").lower()
            if ans == "house":
                print("You found a guy in the house that kick you ass.")
                remove_health(5)
                if health <=0:
                    print("You have 0 HP and lost the game...")
                    exit()
                else:
                    print("You survived like trump")
            else:
                print("You fell in the river and lost...")

        else:
            ans = input('You notice a tree with an apple, do you want to eat it? yes/not').lower()
            if ans == 'yes':
                print('Now you are snowhite and need a prince to kiss you, bye bye')
            else:
                print('you won congratulations')
                exit()
            print ("You just got killed and you lost")
    else:
        print("see you later niqa")

else:
    print("YOU SHALL NOT PLAY")
