from main import update_game_state

def test_valid_correct_guess():
    guessed, lives = update_game_state("apple", [], "a", 6)
    assert guessed == ["a"]
    assert lives == 6

def test_valid_wrong_guess():
    guessed, lives = update_game_state("apple", [], "z", 6)
    assert guessed == ["z"]
    assert lives == 5

def test_repeated_guess_no_change():
    guessed, lives = update_game_state("apple", ["a"], "a", 6)
    assert guessed == ["a"]
    assert lives == 6

def test_uppercase_guess_normalized():
    guessed, lives = update_game_state("apple", [], "A", 6)  
    assert guessed == ["a"]
    assert lives == 6

def test_empty_guess_ignored():
    guessed, lives = update_game_state("apple", [], "", 6)
    assert guessed == []
    assert lives == 6

def test_multi_char_guess_ignored():
    guessed, lives = update_game_state("apple", [], "ab", 6)
    assert guessed == []
    assert lives == 6

def test_non_alpha_guess_ignored():
    guessed, lives = update_game_state("apple", [], "1", 6)
    assert guessed == []
    assert lives == 6

def test_original_list_not_mutated_on_valid_guess():
    original = ["a"]
    before = original.copy()
    guessed, lives = update_game_state("apple", original, "p", 6)
    assert original == before
    assert guessed == ["a", "p"]
    assert lives == 6
