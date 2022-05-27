# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

print(names)
# gives me the length of the total number of names
names_length = len(names)
# names[0]
print(names_length)
random_choice = random.randint(0, names_length - 1)
who_pays_the_bill = names[random_choice]
print(f"{who_pays_the_bill} will pay the bills for today")
