import random 

food = {
"Indian": ["Indian Oven", "Jasmine Fusion Grill", "Haveli Bistro"], 
"Korean": ["Diaspora", "Min-Ga", "GOGI Korean BBQ"], 
"Mexican": ["Cinco", "Tortilla", "Condado Tacos"],
"Japanese": ["Rishi Sushi", "Tiger + Lily", "Kooma Sushi"]
}

def get_dinner():
    print("Random Dinner Generator \n#######################")
    response = input("To start... what preference do you have? \n[1] Indian \n[2] Korean \n[3] Mexican \n[4] Japanese \n[5] Pick for me \n>")

    if response == "1":
        print("You chose Indian for dinner. You should eat at " + random.choice(food["Indian"]) + ".")
    elif response == "2":
        print("You chose Korean for dinner. You should eat at " + random.choice(food["Korean"]) + ".")
    elif response == "3":
        print("You chose Mexican for dinner. You should eat at " + random.choice(food["Mexican"]) + ".")
    elif response == "4":
        print("You chose Japanese for dinner. You should eat at " + random.choice(food["Japanese"]) + ".")
    elif response == "5":
        random_number = random.randint(1, 4)
        if random_number == 1:
            print("How about Indian for dinner? You could eat at " + random.choice(food["Indian"]) + ".")
        elif random_number == 2:
            print("How about Korean for dinner? You could eat at " + random.choice(food["Korean"]) + ".")
        elif random_number == 3:
            print("How about Mexican for dinner? You could eat at " + random.choice(food["Mexican"]) + ".")
        elif random_number == 4:
            print("How about Japanese for dinner? You could eat at " + random.choice(food["Japanese"]) + ".")
    else:
        print("That's not a valid option. Please choose a number 1-5.")
get_dinner()