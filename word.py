import random

# List of (clue, word) pairs
word_list = [
    ("A yellow fruit", "banana"),
    ("The opposite of cold", "hot"),
    ("A place where you live", "house"),
    ("It barks and wags its tail", "dog"),
    ("You write with it", "pen"),
    ("It shines in the sky during the day", "sun"),
    ("You wear it on your feet", "shoes"),
    ("A large body of salt water", "ocean"),
    ("A flying mammal", "bat"),
    ("You use it to call someone", "phone")
]

def play_game():
    print("🎯 Welcome to 'What's the Word?'")
    clue, answer = random.choice(word_list)
    attempts = 3

    print(f"\nClue: {clue}")
    while attempts > 0:
        guess = input("Your guess: ").strip().lower()
        if guess == answer:
            print("✅ Correct! You guessed the word!")
            break
        else:
            attempts -= 1
            print(f"❌ Wrong! Attempts left: {attempts}")
    else:
        print(f"💡 The correct word was: {answer}")

# Run the game
if __name__ == "__main__":
    play_game()



