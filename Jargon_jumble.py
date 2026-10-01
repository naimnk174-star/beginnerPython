import random

words = ["apple", "pear", "orange", "watermelon", "grape"]
score = 0
count = 1
ROUNDS = 5


print("=" *40)
print("Welcome to the scrable game")

while count <= ROUNDS :
    print(f"Round number {count}")
    word = random.choice(words)
    letters = list(word)
    random.shuffle(letters)

    scramble = "".join(letters)
    print(f"Screabled word is : {scramble}")

    user_guess = input("enter your guess or type 'skip' to skip this round : ").lower()
    if user_guess == "skip":
        print(f"the answer was : {word}")
        print()
    elif user_guess == word:
        print("your got it right, plus 1 point!!")
        print()
        score =  score + 1
    else: 
        print("Wrong, nice try")
        print(f"the answer was : {word}")
        print()
    count = count + 1
print()
print(f"Your final score is {score}/5")
print("thanks for playing!!")


