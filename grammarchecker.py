import nltk
from nltk import word_tokenize
from nltk.corpus import words
nltk.download('punkt')
nltk.download('words')

def detect_grammar_errors(text):
    tokens = word_tokenize(text)
    
    # Check if each word is in the NLTK words corpus
    misspelled_words = [word for word in tokens if word.lower() not in words.words()]

    # Return True if there are misspelled words
    return len(misspelled_words) > 0

def check_email_length(text, min_length=500):
    # Check if the length of the email exceeds the specified threshold
    return len(text) < min_length

def is_potential_scam(email_text):
    # Grammar check
    grammar_errors = detect_grammar_errors(email_text)

    # Length check
    exceeds_length_limit = check_email_length(email_text)

    # Return True if either grammar errors or length issue is detected
    return grammar_errors or exceeds_length_limit

# Example usage:
user_email = """
Dear user,

Congratulations! You have won a grand prize of $1,000,000. 
To claim your prize, click on the link below and provide your personal information:

http://example-scam-website.com

Best regards,
Scam Artist
"""

if is_potential_scam(user_email):
    print("Potential scam message detected.")
else:
    print("The email seems legitimate.")
