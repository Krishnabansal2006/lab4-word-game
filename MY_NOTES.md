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

# App Bugs 
1. Input validation bugs
- What happens if input is empty, longer than one character, a number, or punctuation?
- Do you normalize case before processing, so A and a behave the same?

2. Repeated guess bugs
- If a user guesses the same letter again, do you accidentally penalize them twice?
- Is repeated input clearly rejected or ignored in a consistent way?

3. Wrong guess counter bugs
- Do you increment wrong guesses only when the letter is not in the secret word?
- Can wrong guesses ever exceed the max due to multiple updates in one turn?

4. Win condition bugs
- Do you check win using unique letters in the word, not total word length?
- For words with repeated letters, does one correct guess reveal all occurrences?

5. Lose condition and off-by-one bugs
- Do you lose exactly at max wrong guesses, not one turn early or late?
- Is remaining attempts computed correctly every time?

6. State transition bugs
- After won or lost, can the game still accept guesses and mutate state?
- Can status accidentally return from won or lost back to playing?

7. Display/progress bugs
- Is progress always the same length as the secret word?
- Are only guessed letters revealed, with unguessed letters masked reliably?

9. Word handling edge cases
- How do you handle spaces, hyphens, or apostrophes in secret words?
- Do non-letter characters auto-reveal or break your logic?

11. Random word source bugs
- Can the word list be empty?
- Do trailing newline characters from file reads leak into the secret word?

# Auto Play 

- When the game starts, ask the user to play or watch the computer autoplay.
- In autoplay, the computer guesses letters using frequency order (etaoinshrdlcumwfgypbvkjxqz).
- It never repeats a letter. After autoplay ends, ask again.

- New function needed: get_computer_guess(guessed_letters) — picks next unguessed letter.
- Reuses all existing functions, just swaps get_player_guess for get_computer_guess.
