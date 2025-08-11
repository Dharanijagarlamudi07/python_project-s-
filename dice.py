import random
def roll_dice(num_dice):
    return[random.randint(1,6) for _ in range(num_dice)]
def main():
    num_dice = int(input("how many dice do you want to rokll? "))
    roll_count=0
    while True:
        results=roll_dice(num_dice)
        print("you rolled: " , results)
        roll_count += 1
        again = input("roll again ? (y/n):").lower()
        if again != 'y':
            break
    print(f"you rolled {roll_count} times.good bye!")
if __name__ == "__main__":
    main()