rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
inputs = [rock , paper , scissors]
game = input("Hey there, would you like to play rock, paper and scissors?\n").lower()
if game == "yes":
    decision = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

    import random
    random_decision = random.choice(inputs)

    if decision == "0":
        print(rock)
        print("Computer chose: \n" + random_decision)

        if random_decision == rock:
            print("It's a draw.")
        elif random_decision == paper:
            print("Computer won.")
        elif random_decision == scissors:
            print("You won.")
        else:
            print("Idk where i am wrong gotta learn more! haha.")

    elif decision == "1":
        print(paper)
        print("Computer chose: \n" + random_decision)

        if random_decision == paper:
            print("It's a draw.")
        elif random_decision == rock:
            print("You won.")
        elif random_decision == scissors:
            print("Computer won.")
        else:
            print("Idk where i am wrong gotta learn more! haha.")

    elif decision == "2":
        print(scissors)
        print("Computer chose: \n" + random_decision)

        if random_decision == scissors:
            print("It's a draw.")
        elif random_decision == rock:
            print("Computer won.")
        elif random_decision == paper:
            print("You won.")
        else:
            print("Idk where i am wrong gotta learn more! haha.")

    else:
        print("ERROR - Wrong input - Answer in '0','1' or '2'.")
elif game == "no":
    print("Okay come back when you feel like playing :).")
else:
    print("ERROR - Wrong input - Answer in 'yes' or 'no'.")
