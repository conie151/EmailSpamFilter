import re

def detect_grammar_errors_and_scams(email):
    # Check for multiple dots in the email address
    if email.count('.') > 1:
        return True, "Multiple dots detected in email address."

    # Check for consecutive identical letters (double or triple letters)
    if re.search(r'(.)\1{1,}', email):
        return True, "Consecutive identical letters detected in email address."

    # Check email address length
    if len(email) > 50:
        return True, "Email address length exceeds the recommended limit."

    # Add more grammar error checks as needed

    return False, None  # No errors detected

# Example usage:
user_email = "john.doe@gamil.com"
is_error, error_message = detect_grammar_errors_and_scams(user_email)

if is_error:
    print("Potential issues detected:")
    print(error_message)
else:
    print("Email address appears to be valid.")
