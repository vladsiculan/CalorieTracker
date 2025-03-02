from pyisemail import is_email

def validate(email):
    """
    Validates an email address using the `pyisemail` library.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    return is_email(email)

if __name__ == "__main__":
    # List of email addresses to test
    emails = [
        'example@example.com',
        'exa-mple@gmail.com',
        'exa mple@gmail.com',
        'example@example@example.com',
        'example@gmail'
    ]

    # Test each email and print whether it is valid or invalid
    for email in emails:
        print(f"{email}: {'Valid' if validate(email) else 'Invalid'}")