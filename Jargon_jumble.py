import random

words = ["apple", "pear", "orange", "watermelon", "grape"]
score = 0

print("=" *40)
print("Welcome to the scrable game")

word = random.choice(words)

letters = list(word)
random.shuffle(letters)

scramble = "".join(letters)
print(f"Screabled word is : {scramble}")

user_guess = input("enter your guess or type 'skip' to skip this round : ").lower()


if user_guess == "skip":
    print(f"the answer was : {word}")
elif user_guess == word:
    print("your got it right!!")
else: 
    print("Wrong, nice try")
    print(f"the answer was : {word}")


print("hello ")