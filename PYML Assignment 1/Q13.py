def calculate_age(birth_year):
    import datetime
    current_year = datetime.datetime.now().year
    age = current_year - birth_year
    return age

def main():
    try:
        birth_year = int(input("Enter your birth year: "))
        age = calculate_age(birth_year)
        print(f"You are {age} years old.")
    except ValueError:
        print("Please enter a valid year (e.g., 1990).")

if __name__ == "__main__":
    main()
