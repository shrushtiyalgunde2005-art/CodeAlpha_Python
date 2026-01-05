# Hangman Game
# CodeAlpha Python Programming Internship - Task 1


import random

word_list = ["coding", "python", "internship", "software", "developer"]
secret_word = random.choice(word_list)

used_letters = []             #stores letters gussed by the user
max_chances = 6

print("Welcome to Hangman Game!")     #welcome messages
print("You have", max_chances, "chances to guess the word.")

while max_chances > 0:
    result = ""
    for ch in secret_word:
        if ch in used_letters:
            result += ch
        else:
            result += "_"

    print("\nWord:", result)

    if "_" not in result:
        print("🎉 You won! Great job.")
        break
    
    user_letter = input("Enter a letter: ").lower()

    if user_letter in used_letters:
        print("⚠ You already tried this letter.")
        continue
    
    used_letters.append(user_letter)

    if user_letter not in secret_word:
        max_chances -= 1
        print("❌ Wrong guess. Remaining chances:", max_chances)
    else:
        print("✅ Correct guess!")

if max_chances == 0:
    print("\nGame Over! The word was:", secret_word)