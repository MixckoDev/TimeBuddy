from datetime import datetime
import pytz

def display_time_in_timezones():
    timezones = {
        "New York": "America/New_York",
        "London": "Europe/London",
        "Berlin": "Europe/Berlin",
        "Tokyo": "Asia/Tokyo",
        "Sydney": "Australia/Sydney"
    }

    print("\nCurrent Time in Different Cities:")
    for city, tz in timezones.items():
        timezone = pytz.timezone(tz)
        city_time = datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")
        print(f"{city}: {city_time}")

def main():
    print("Welcome to TimeBuddy!")
    while True:
        print("\nMenu:")
        print("1. View current local time")
        print("2. View time in different cities")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            local_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"\nLocal Time: {local_time}")
        elif choice == "2":
            display_time_in_timezones()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
