# Simple Quiz Game

score = 0

# Question 1
print("Question 1: What is the capital of France?")
print("a) Paris")
print("b) London")
print("c) Rome")
answer1 = input("Your answer: ").lower()

if answer1 == "a":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is a) Paris")

print()

# Question 2
print("Question 2: What is the largest planet in our solar system?")
print("a) Earth")
print("b) Jupiter")
print("c) Mars")
answer2 = input("Your answer: ").lower()

if answer2 == "b":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is b) Jupiter")

print()
print(f"Your final score: {score}/2")