def password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_char_criteria = any(char in "!@#$%^&*()_+=-{}[]:;\"'|\\<,>.?/" for char in password)

    strength_score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])

    if strength_score == 5:
        return "Very Strong"
    elif strength_score == 4:
        return "Strong"
    elif strength_score == 3:
        return "Moderate"
    elif strength_score == 2:
        return "Weak"
    else:
        return "Very Weak"

def main():
    password = input("Enter your password: ")
    strength = password_strength(password)
    print("Password strength:", strength)

if __name__ == "__main__":
    main()

