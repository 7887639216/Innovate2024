def email_slicer(email):
    # Split the email address into username and domain
    username, domain = email.split('@')
    return username, domain

def main():
    # Get the email address from the user
    email = input("Enter your email address: ").strip()

    # Slice the email address
    username, domain = email_slicer(email)

    # Display the sliced parts
    print("Username:", username)
    print("Domain:", domain)

if __name__ == "__main__":
    main()
