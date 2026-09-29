#https://youtu.be/kLZgQWjnUz0?si=2zMbepRRwpKSkrSy
# challange 1: Payup App

print("=" * 40 )
print("Welcome to Payup !!")

event_name = input("What was the event called ? ")
total_price = int(input("What was the total amount that was to be payed? "))
tax = int(input("What was the service tax (eg. 20 for 20%)? "))
people = int(input ("How many people were there? "))


grand_total = total_price + total_price * (tax / 100)
each_total = grand_total / people

print()
print(f"Your event at {event_name}'s overview: ")
print(f"Grand total was RM{grand_total} with tax.")
print(f"Total number of people in your party was {people}.")
print(f"Thus each person must pay : RM{each_total} (IF split evenly).")
print()
print("thank you for using Payup !!!")
print()
print("=" * 40 )


