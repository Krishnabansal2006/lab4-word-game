import random

WORDS = ["apple", "banana", "grape", "mango", "cherry", "orange", "lemon"]
MAX_LIVES = 6


def update_game_state(secret_word: str, guessed_letters: list[str], guess: str, lives: int) -> tuple[list[str], int]:
    """
    Update guessed letters and lives after a guess in Hangman.

    Args:
        secret_word: The word to guess (lowercase).
        guessed_letters: List of letters already guessed (lowercase).
        guess: The player's guess (any case).
        lives: Remaining incorrect guesses allowed.

    Returns:
        (updated guessed_letters, updated lives)
    """
    guess = guess.lower()

    # Ignore invalid guesses (not a single alphabetic character)
    if len(guess) != 1 or not guess.isalpha():
        return (guessed_letters, lives)

    # Ignore repeated guesses
    if guess in guessed_letters:
        return (guessed_letters, lives)

    new_guessed = guessed_letters + [guess]
    # Decrement lives only if guess is incorrect
    new_lives = lives if guess in secret_word else lives - 1

    return (new_guessed, new_lives)


def get_masked_word(secret_word: str, guessed_letters: list[str]) -> str:
    return " ".join(letter if letter in guessed_letters else "_" for letter in secret_word)


def check_win(secret_word: str, guessed_letters: list[str]) -> bool:
    required_letters = set(secret_word)
    guessed_set = set(guessed_letters)
    return required_letters.issubset(guessed_set)


def check_loss(lives: int) -> bool:
    return lives <= 0


def get_wrong_letters(secret_word: str, guessed_letters: list[str]) -> list[str]:
    return [letter for letter in guessed_letters if letter not in secret_word]


def init_game() -> tuple[str, list[str], int]:
    return (random.choice(WORDS), [], MAX_LIVES)


def get_player_guess() -> str:
    return input("Guess a letter: ").strip().lower()


def display_board(secret_word: str, guessed_letters: list[str], lives: int) -> None:
    print(f"\nWord: {get_masked_word(secret_word, guessed_letters)}")
    print(f"Wrong letters: {' '.join(get_wrong_letters(secret_word, guessed_letters))}")
    print(f"Lives remaining: {lives}")


def play_game() -> None:
    replay_choice = "y"

    while replay_choice == "y":
        secret_word, guessed_letters, lives = init_game()

        while not check_win(secret_word, guessed_letters) and not check_loss(lives):
            display_board(secret_word, guessed_letters, lives)
            guess = get_player_guess()
            guessed_letters, lives = update_game_state(secret_word, guessed_letters, guess, lives)

        display_board(secret_word, guessed_letters, lives)
        if check_win(secret_word, guessed_letters):
            print("You win!")
        else:
            print(f"You lost! The word was: {secret_word}")

        replay_choice = input("Play again? (y/n): ").strip().lower()


if __name__ == "__main__":
    play_game()
