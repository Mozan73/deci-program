import random
import time

high_score = 0

def start_game():
    global high_score
    print("Welcome, Detective! A mysterious crime awaits your expertise.")
    name = input("What is your name, Detective? ").strip().capitalize()
    print(f"\nNice to meet you, Detective {name}. Let's see if you can crack this case...")

    play_again = True

    while play_again:
        score = play_game(name)
        if score > high_score:
            high_score = score
            print("New High Score!")

        print(f"\nYour Score: {score} points")
        print(f"High Score: {high_score} points")

        choice = input("\nWould you like to play again? (y/n): ").lower()
        while choice not in ['y', 'n']:
            choice = input("Please enter 'y' or 'n': ").lower()
        play_again = (choice == 'y')

def generate_crime_scene():
    locations = ['library', 'kitchen', 'rooftop', 'garage', 'office']
    weapons = ['broken vase', 'kitchen knife', 'poisoned drink', 'bat', 'scissors']
    notes = [
        "He shouldn't have trusted her.",
        "The key was under the rug.",
        "Time is the enemy.",
        "Don't believe the witness.",
        "It happened before the lights went out."
    ]
    return random.choice(locations), random.choice(weapons), random.choice(notes)

def ask_question(question, correct_answer):
    print("\n" + question["q"])
    for i, option in enumerate(question["options"], 1):
        print(f"{i}) {option}")
    answer = input("> ").strip()
    if answer == str(correct_answer):
        print("Correct!")
        return 1
    else:
        print(f"Wrong. The correct answer was: {correct_answer}) {question['options'][correct_answer-1]}")
        return 0

def play_game(name):
    print("\nA new mystery is unfolding...\n")
    time.sleep(1)

    location, weapon, note = generate_crime_scene()

    print(f"Crime Scene: {location.capitalize()}")
    print(f"Weapon Found: {weapon}")
    print(f"Mysterious Note: \"{note}\"\n")
    time.sleep(1)

    score = 0
    max_turns = 6
    turns = 0

    # Questions pool
    questions = [
        {
            "q": "Who was the last person to see the victim alive?",
            "options": ["The maid", "The neighbor", "The victim's brother"],
            "answer": 3
        },
        {
            "q": "What time did the power go out?",
            "options": ["9 PM", "10 PM", "11 PM"],
            "answer": 2
        },
        {
            "q": "What was missing from the room?",
            "options": ["Wallet", "Phone", "CCTV footage"],
            "answer": 3
        },
        {
            "q": "Which fingerprint was found on the weapon?",
            "options": ["Victim", "No one", "Suspect"],
            "answer": 2
        },
        {
            "q": "Which direction was the body facing?",
            "options": ["North", "East", "Face down"],
            "answer": 3
        },
    {
            "q": "How many months of the year have 28 days?",
            "options": ["1", "2", "All of them"],
            "answer": 3
   }
]

    random.shuffle(questions)

    for q in questions[:max_turns]:
        score += ask_question(q, q["answer"])
        turns += 1

    print("\n--- GAME OVER ---")
    if score >= 4:
        print("You solved the case, Detective!")
    elif score == 3:
        print("Almost there... One more clue and you'd crack it.")
    else:
        print("The case remains unsolved.")
    return score
start_game()
