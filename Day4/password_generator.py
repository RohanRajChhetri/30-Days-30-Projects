import random
import string

def generate_password(MinLength, Numbers=True, SpecialChars=True):
    letters = string.ascii_letters 
    digits = string.digits 
    special= string.punctuation


    characters = letters 
    if Numbers:
        characters += digits
    if SpecialChars:
        characters += special

    pwd = ""
    criteria = False
    has_digit = False
    has_special = False

    while not criteria or len(pwd) < MinLength:

        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_digit = True
        elif new_char in special:
            has_special = True
        
        criteria = True
        if Numbers:
            criteria = criteria and has_digit
        if SpecialChars:
            criteria = criteria and has_special
        
    return pwd


if __name__ == "__main__":
    Minlength = int(input("Enter the minimum length of the password: "))
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower () == 'y'
    pwd = generate_password(Minlength, use_numbers, use_special_chars)
    print(f"Generated password: {pwd}")