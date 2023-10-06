# rock apper scissors game

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
import random
# put images in list
images = [rock, paper, scissors]

# get choices
person_choice = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
print(images[person_choice])
# computer_choice = random.choice[images]
# or 
computer_choice = random.randint(0,2)
print(images[computer_choice])
print(f"{person_choice}\n {computer_choice}")
if person_choice == computer_choice:
    print(f"{images[computer_choice] images[person_choice] A draw!}")
elif:
    if computer_choice == "0" and person_choice == "1"




#computer_choice = random.randint(1, 3) - 1
print(computer_choice)
