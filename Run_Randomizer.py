import random 

choice = 0
dist1 = 0
dist2 = 0
target_dist = 0
reps = 0
pace = 0


print(40 * "=")
print("Welcome to the run randomizer")
print("What workout would you like to do? :")
print("1. long" \
"      2. speed workout" \
"      3. base run" \
"      4. fartlek")
choice = int(input("Enter your preffered workout (1-4): "))

if choice == 1:
    dist1 = int(input("Enter Min distance(KM): "))
    dist2 = int(input("Enter Max distance(KM): "))
    pace = float(input("At what pace would you want to do for this run (min/km): "))
    target_dist = random.randint(dist1, dist2)
    time = target_dist * pace
    print(f"The workout will be {target_dist}KM @ pace {pace}min/km and the total time it would take is : {time}")
    

else :
    print("hello")