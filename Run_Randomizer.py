import random 

choice = 0
dist1 = 0
dist2 = 0
target_dist = 0
reps = 0
pace = 0
hr = 0

print(40 * "=")
print("Welcome to the run randomizer")
print("What workout would you like to do? :")
print("1. long" \
"      2. speed workout" \
"      3. base run")
choice = int(input("Enter your preffered workout (1-3): "))

if choice == 1:
    dist1 = int(input("Enter Min distance(KM): "))
    dist2 = int(input("Enter Max distance(KM): "))
    pace = float(input("At what pace would you want to do for this run (eg. 5.5 -> 5:30min/km): "))
    hr = int(input("Enter your zone 2 heartrate(average): "))
    target_dist = random.randint(dist1, dist2)
    time = target_dist * pace
    print(f"The workout will be {target_dist}KM @ pace {pace} min/km in Z2({hr}bpm)and the total time it would take is : {time} minutes")
    print("Enjoy your run !!!\n")
elif choice == 2 : 
    type = input("Tempo(T) or Interval(I) : ")
    if type == "T":
        dist1 = int(input("Enter Min distance(KM): "))
        dist2 = int(input("Enter Max distance(KM): "))
        pace = float(input("At what pace would you want to do for this run (eg. 5.5 -> 5:30min/km): "))
        hr = int(input("Enter your zone 4 heartrate(average): "))
        target_dist = random.randint(dist1, dist2)
        time = target_dist * pace
        print(f"The workout will be {target_dist}KM @ pace {pace} min/km in Z4({hr}bpm)and the total time it would take is : {time} minutes")
        print("Enjoy your run !!!\n") 
    elif type == "I" :
        dist1 = float(input("Enter Min distance(KM): "))
        dist2 = float(input("Enter Max distance(KM): "))
        pace = float(input("At what pace would you want to do for this run (eg. 5.5 -> 5:30min/km): "))
        hr = int(input("Enter your zone 4 heartrate(average): "))
        reps = int(input("Enter reps to be done :"))
        target_dist = round(random.uniform(dist1, dist2), 1)
        total_dist = target_dist * reps 
        time = total_dist * pace
        print(f"The workout will be {total_dist}KM @ pace {pace} min/km in Z4({hr}bpm)and the total time it would take is : {time} minutes")
        print("Enjoy your run !!!\n")
elif choice == 3:
    dist1 = int(input("Enter Min distance(KM): "))
    dist2 = int(input("Enter Max distance(KM): "))
    pace = float(input("At what pace would you want to do for this run (eg. 5.5 -> 5:30min/km): "))
    hr = int(input("Enter your zone 2 heartrate(average): "))
    target_dist = random.randint(dist1, dist2)
    time = target_dist * pace
    print(f"The workout will be {target_dist}KM @ pace {pace} min/km in Z2({hr}bpm)and the total time it would take is : {time} minutes")
    print("Enjoy your run !!!\n")
else:
    print("Invalid choice, please choose between 1,2 and 3!!!")