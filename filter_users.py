import json

def filter_by_age(data, min_age):
    '''Returns all persons with min_age or older'''
    return [person for person in data if person.get("age", 0) >= min_age]

def filter_by_email(data, email_domain):
    """
    Returns all users whose email ends with the given domain
    or matches the given email address exactly.
    """
    return [person for person in data if person.get("email", "").endswith(email_domain)]

def main():
    try:
        # Open and load data from the JSON file
        with open("users.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Error: 'users.json' file not found.")
        return
    except json.JSONDecodeError:
        print("Error: 'users.json' does not contain valid JSON.")
        return

    # Apply filters
    filtered_by_age = filter_by_age(data, 21)
    filtered_by_email = filter_by_email(data, "@web.de")  # or a specific email like "annana@web.de"

    # Display results
    print("\n📋 Filtered by age (>=21):")
    for person in filtered_by_age:
        print("-", person)

    print("\n📧 Filtered by email domain '@web.de':")
    for person in filtered_by_email:
        print("-", person)

if __name__ == "__main__":
    main()