def detect_vowels(text):
    vowels = "aeiouAEIOU"
    return [char for char in text if char in vowels]

def doesRhyme(sen1,sen2):
    sen1_last_vowels = detect_vowels(sen1.split(" ")[-1])
    sen2_last_vowels = detect_vowels(sen2.split(" ")[-1])
    return sen1_last_vowels[-1].lower() == sen2_last_vowels[-1].lower()

assert doesRhyme("Sam I am!", "Green eggs and ham.") == True , "doesRhyme doesn't work correctly"
assert doesRhyme("Sam I am!", "Green eggs and HAM") == True , "doesRhyme doesn't work correctly"
assert doesRhyme("You're built like a seat", "I bet you like to eat") == True , "doesRhyme doesn't work correctly"
assert doesRhyme("You are off to the races", "a splendid day.") == False , "doesRhyme doesn't work correctly"
assert doesRhyme("and frequently do?", "you gotta move.") == False , "doesRhyme doesn't work correctly"
