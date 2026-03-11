# My Original Thinking 

# App State
A Hangman-style game usually needs this state:

secret_word: the actual word to guess

guessed_letters: set/list of letters already guessed

wrong_guesses: count of incorrect guesses

max_wrong_guesses: losing threshold (for example, 6)

current_progress: masked view like _ A _ _ M A _

game_status: playing | won | lost

Optional but useful:
remaining_attempts (can be derived from max - wrong)
wrong_letters (for display)
guess_history (if you want undo/replay/stats)

# App Variable 
For a Hangman implementation:

secret_word (str): word to guess

guessed_letters (set[str]): all letters guessed so far

wrong_guesses (int): number of incorrect guesses

max_wrong_guesses (int): lose limit (like 6)

game_status ("playing" | "won" | "lost")

Good rule: only store what can’t be reliably recalculated.

So these are usually derived, not stored:
current_progress (build from secret_word + guessed_letters)
remaining_attempts (max_wrong_guesses - wrong_guesses)
wrong_letters (filter guessed_letters against secret_word)

# App Rules ans Invariants 
What inputs are valid for a guess?
Must it be exactly one alphabetic character?
Do you force lowercase/uppercase normalization first?
What happens on empty input, numbers, or symbols?

What happens on repeated guesses?
Is a repeated letter ignored, penalized, or rejected with a message?
If ignored/rejected, does wrong_guesses stay unchanged?

When does wrong_guesses change?
Only when the guessed letter is not in secret_word?
Never on correct guesses?
Never exceeds max_wrong_guesses?
What must always be true about guessed_letters?

No duplicates (set behavior)?
Contains only normalized single letters?
Every processed guess is added exactly once?

What must always be true about progress display?
Same length as secret_word?
Reveals only letters in guessed_letters?
Unrevealed positions always shown as _?

When does game status change?
won exactly when all unique letters in secret_word are guessed?
lost exactly when wrong_guesses == max_wrong_guesses?
Otherwise playing?

What transitions are forbidden?
Once won or lost, can no further guesses modify state?
Can status ever go from won/lost back to playing? (usually no)

