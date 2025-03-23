from hashlib import sha256

def hash_password(password):
    return sha256(password.encode()).hexdigest()

def login(email, password_to_check, stored_logins):
    if email in stored_logins:  
        return stored_logins[email] == hash_password(password_to_check)
    return False  


def  main():
    stored_logins = {
        "user@example.com": hash_password("securepassword123"),
        "john.doe@email.com": hash_password("mySuperSecret!"),
    }

    # Test login
    print(login("user@example.com", "securepassword123", stored_logins))  # True
    print(login("user@example.com", "wrongpassword", stored_logins))  # False
    print(login("unknown@email.com", "password", stored_logins))  # False
    print(login("john.doe@email.com", "mySuperSecret!", stored_logins))  # True


if __name__ == "__main__":
    main()