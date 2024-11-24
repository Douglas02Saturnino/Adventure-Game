name = input("Hey type your name:")
print("Hello " + name + " welcome to my game!")

should_we_play = input("Do you want to play? (Yes/No) ").lower()

if should_we_play == "yes" or should_we_play == "y":
    print("We are gonna play")

    direction = input("Do you want to go left or right? (left/right) ").lower()
    if direction == "left":
        print("You went left and fell a cliff, game over, try again.")
    elif directio == "right":
        choice = input("Okay, you now see a bridge, do you want to swim under it or cross it? (swim/cross) ").lower()
        if choice == "swim":
            print("You swim under the bridge and get eaten by a shark, game over.")
        elif choice == "cross":
            print("You cross the bridge and find a treasure, you win!")
    else:
        print("Sorry not a valid reply, you die!")
else:
    print("We are NOT playing...")