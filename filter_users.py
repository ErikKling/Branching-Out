def filter_by_age(data, min_age):
    '''Returns all Persons with min_age or older'''
    return [person for person in data if person.get("age", 0) >= min_age]

def filter_by_email(data, email_domain):
    """
    Gibt alle Benutzer zurück, deren E-Mail mit der angegebenen Domain endet.
    Beispiel: email_domain = "@gmail.com"
    """
    return [person for person in data if person.get("email", "").endswith(email_domain)]

def main():

    sample_data = [
        {"name": "Anna", "age": 22, "email": "annana@web.de"},
        {"name": "Ben", "age": 19, "email": "benno@web.de"},
        {"name": "Clara", "age": 27, "email": "cl94mueller@gmx.de"}
        ]
    result = filter_by_email(sample_data, "annana@web.de")
    print(result)

if __name__ == "__main__":
     main()