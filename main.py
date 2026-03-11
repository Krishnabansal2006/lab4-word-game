def update_game_state(secret_word: str, 
                      guessed_letters: list[str],
                      guess: str,
                      lives: int) -> tuple[list[str], int]: