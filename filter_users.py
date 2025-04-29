def filter_by_age(data, min_age):
    '''Returns all Persons with min_age or older'''
    return [person for person in data if person.get("age", 0) >= min_age]

def main():

    sample_data = [
        {"name": "Anna", "age": 22},
        {"name": "Ben", "age": 19},
        {"name": "Clara", "age": 27}
        ]
    result = filter_by_age(sample_data, 20)
    print(result)

if __name__ == "__main__":
     main()