import random

# Word list for the game
WORD_LIST = [
    "apple", "brave", "crane", "delta", "eagle",
    "flame", "grape", "heart", "ivory", "joker",
    "kneel", "lemon", "mango", "noble", "olive",
    "piano", "queen", "river", "stone", "tiger",
    "ultra", "vivid", "water", "xenon", "yacht",
    "zebra", "audio", "blaze", "chess", "dwarf",
    "elder", "frost", "gloom", "hinge", "index",
    "judge", "knife", "label", "maple", "night",
    "ocean", "plumb", "quirk", "ranch", "scout",
    "taste", "umbra", "venom", "wheat", "yield"
]

MAX_ATTEMPTS = 6
WORD_LENGTH = 5

# ANSI colour codes for terminal output
GREEN = "\033[92m"   # Correct letter, correct position
YELLOW = "\033[93m"  # Correct letter, wrong position
GRAY = "\033[90m"    # Letter not in word
RESET = "\033[0m"
BOLD = "\033[1m"


def choose_word():
    """Randomly select a secret word from the word list."""
    return random.choice(WORD_LIST)


def check_guess(secret, guess):
    """
    Compare the guess against the secret word.
    Returns a list of tuples: (letter, status)
    Status: 'green' = correct position, 'yellow' = wrong position, 'gray' = not in word.
    """
    result = []
    secret_letters = list(secret)
    guess_letters = list(guess)
    # First pass: mark greens
    marked = [False] * WORD_LENGTH
    for i in range(WORD_LENGTH):
        if guess_letters[i] == secret_letters[i]:
            result.append((guess_letters[i], 'green'))
            marked[i] = True
            secret_letters[i] = None  # consume this letter
        else:
            result.append((guess_letters[i], None))
    # Second pass: mark yellows and grays
    for i in range(WORD_LENGTH):
        if result[i][1] is None:
            letter = guess_letters[i]
            if letter in secret_letters:
                result[i] = (letter, 'yellow')
                secret_letters[secret_letters.index(letter)] = None
            else:
                result[i] = (letter, 'gray')
    return result


def colour_result(result):
    """Return a coloured string representation of the guess result."""
    output = ""
    for letter, status in result:
        if status == 'green':
            output += GREEN + BOLD + letter.upper() + RESET
        elif status == 'yellow':
            output += YELLOW + BOLD + letter.upper() + RESET
        else:
            output += GRAY + letter.upper() + RESET
    return output


def display_keyboard(used_letters):
    """Display a simple keyboard showing used letters and their status."""
    rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    print("\n  Keyboard:")
    for row in rows:
        line = "  "
        for ch in row:
            if ch in used_letters:
                status = used_letters[ch]
                if status == 'green':
                    line += GREEN + ch.upper() + RESET + " "
                elif status == 'yellow':
                    line += YELLOW + ch.upper() + RESET + " "
                else:
                    line += GRAY + ch.upper() + RESET + " "
            else:
                line += ch.upper() + " "
        print(line)
    print()


def get_valid_guess():
    """Prompt the player for a valid 5-letter guess."""
    while True:
        guess = input("  Enter your guess: ").strip().lower()
        if len(guess) != WORD_LENGTH:
            print(f"  Please enter exactly {WORD_LENGTH} letters.")
        elif not guess.isalpha():
            print("  Only letters are allowed.")
        else:
            return guess


def play_game():
    """Main game loop."""
    secret = choose_word()
    attempts = 0
    used_letters = {}  # letter -> best status seen
    guesses_log = []   # store (guess, result) for display

    print("\n" + "=" * 40)
    print(BOLD + "  Welcome to Word Game!" + RESET)
    print("  Guess the 5-letter word.")
    print(f"  You have {MAX_ATTEMPTS} attempts.")
    print("  " + GREEN + "GREEN" + RESET + " = right letter, right spot")
    print("  " + YELLOW + "YELLOW" + RESET + " = right letter, wrong spot")
    print("  " + GRAY + "GRAY" + RESET + " = letter not in word")
    print("=" * 40 + "\n")

    while attempts < MAX_ATTEMPTS:
        print(f"  Attempt {attempts + 1}/{MAX_ATTEMPTS}")

        # Show previous guesses
        for past_guess, past_result in guesses_log:
            print("  " + colour_result(past_result) + f"  ({past_guess})")

        display_keyboard(used_letters)
        guess = get_valid_guess()
        result = check_guess(secret, guess)
        guesses_log.append((guess, result))
        attempts += 1

        # Update used_letters with best status
        priority = {'green': 3, 'yellow': 2, 'gray': 1}
        for letter, status in result:
            if letter not in used_letters or priority[status] > priority[used_letters[letter]]:
                used_letters[letter] = status

        # Show the result
        print("  " + colour_result(result))

        if all(status == 'green' for _, status in result):
            print(f"\n" + GREEN + BOLD + "  Congratulations! You guessed it in {attempts} attempt(s)!" + RESET)
            print(f"  The word was: {BOLD}{secret.upper()}{RESET}\n")
            return True

        remaining = MAX_ATTEMPTS - attempts
        if remaining > 0:
            print(f"  {remaining} attempt(s) remaining.\n")

    print("\n" + GRAY + BOLD + f"  Game over! The word was: {secret.upper()}" + RESET + "\n")
    return False


def play_again():
    """Ask the player if they want to play again."""
    answer = input("  Play again? (yes/no): ").strip().lower()
    return answer in ('yes', 'y')


def main():
    """Entry point: run the game loop."""
    wins = 0
    games = 0
    while True:
        result = play_game()
        games += 1
        if result:
            wins += 1
        print(f"  Stats: {wins} win(s) out of {games} game(s) played.")
        if not play_again():
            print("\n  Thanks for playing! Goodbye.\n")
            break


if __name__ == "__main__":
    main()
