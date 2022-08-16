#Activity prioritizer 
#Helps users cut down their spending on hobbies!

hobbies  = ["Archery", "Bowling", "Canoeing", "Dance", "Embroidery", "Flute", "Gymnastics"]

#A user has added a list of hobbies inr order of preferences, want to delete everything after Dance. 
#Delete the last item in hobbies until the last item is Dance
while hobbies[-1] != "Dance":
    del hobbies[-1]
#Print a message with the remaining hobbies and the amount left after removal. We'll need to use
#type conversion on this value
number = str(len(hobbies))
print("These are your " + number + " favourite hobbies:")
print(hobbies)
#Extra activities are stored extras and include a list of costs. We need to remove the last item until we have enough savings. 
#First assign the value 0 to the variable savings. 
extras = ["Gym", "Cinema", "Resturants", "Jewellery", "Coffee", "Netflix", "Bingo"]
costs = [50, 20, 80, 30, 40, 10, 25]
to_save = 100

savings = 0

print(to_save - savings)

while to_save > 0:
    to_save -= costs[-1]
    savings += costs[-1]
    del costs[-1]
    del extras[-1]

print(costs)
print(extras)

savings = str(savings)
print("You'll save " + savings + " euros by sticking to these extras:")
print(extras)

next_saving = extras[-1]
print("If you need to save more money, take some time off " + next_saving + ".")