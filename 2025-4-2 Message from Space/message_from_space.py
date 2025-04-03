import re

def spaceMessage(encrypted_message: str) -> str:
    '''
    Return a decrypted message.
    '''
    regex = r"[\[\]]"
    lit = re.split(regex, encrypted_message)
    decrypted_message = ""
    for word in lit:
        # If the digit is existing.
        if re.search(r"\d+", word):
            # Deconstruct number as `times` and text as `text`
            times = re.search(r"[0-9]+", word).group()
            text = re.search(r"\D+", word).group()
            # Construct a decrypted string
            new_str = text * int(times)
        else:
            new_str = word
        decrypted_message += new_str
    return decrypted_message

# Test case
assert spaceMessage("ABCD") == "ABCD", "Error"
assert spaceMessage("AB[3CD]") == "ABCDCDCD", "Error"
assert spaceMessage("IF[2E]LG[5O]D") == "IFEELGOOOOOD", "Error"

if __name__ == "__main__":
    print(spaceMessage("ABCD"))
    print(spaceMessage("AB[3CD]"))
    print(spaceMessage("IF[2E]LG[5O]D"))

    