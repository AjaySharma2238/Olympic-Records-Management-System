import json

records = []


def save_records():
    with open("athlete_records.json", "w") as f:
        json.dump(records, f, indent=2)


def load_records():
    try:
        with open("athlete_records.json", "r") as f:
            global records
            records = json.load(f)
    except FileNotFoundError:
        pass


def add_athlete():
    name = input("Enter athlete's name: ")
    country = input("Enter country: ")
    sport = input("Enter sport: ")
    event = input("Enter event: ")
    year = int(input("Enter year: "))
    medal = input("Enter medal type (Gold, Silver, Bronze): ")

    athlete = {
        "Name": name,
        "Country": country,
        "Sport": sport,
        "Event": event,
        "Year": year,
        "Medal": medal,
    }

    records.append(athlete)
    save_records()
    print("Record added successfully!")


def view_athletes():

    if len(records) == 0:
        print("No records available.")
    else:
        for athlete in records:
            print(
                athlete["Name"],
                "-",
                athlete["Country"],
                "-",
                athlete["Sport"],
                "-",
                athlete["Event"],
                "-",
                athlete["Year"],
                "-",
                athlete["Medal"],
            )


def view_medal_count():
    medal_counts = {}
    for athlete in records:
        country = athlete["Country"]
        if country in medal_counts:
            medal_counts[country] += 1
        else:
            medal_counts[country] = 1

    for country in medal_counts:
        print(f"{country}:", medal_counts[country], "medals")


def search_athlete():
    name = input("Enter athlete's name to search: ")
    found = False
    for athlete in records:
        if athlete["Name"].lower() == name.lower():
            print(
                athlete["Name"],
                "-",
                athlete["Country"],
                "-",
                athlete["Sport"],
                "-",
                athlete["Event"],
                "-",
                athlete["Year"],
                "-",
                athlete["Medal"],
            )
            found = True

    if not found:
        print("No records found for athlete:", name)


def view_event():
    event_name = input("Enter event name to view details: ")
    found = False
    for athlete in records:
        if athlete["Event"].lower() == event_name.lower():
            print(
                athlete["Name"],
                "-",
                athlete["Country"],
                "-",
                athlete["Sport"],
                "-",
                athlete["Year"],
                "-",
                athlete["Medal"],
            )
            found = True

    if not found:
        print("No records found for event:", event_name)


def view_statistics():
    if len(records) == 0:
        print("No records available.")
    else:
        total_records = len(records)
        medal_counts = {"Gold": 0, "Silver": 0, "Bronze": 0}
        for athlete in records:
            medal_counts[athlete["Medal"]] += 1
        print("Total records:", total_records)
        print(
            "Medal distribution: Gold:",
            medal_counts["Gold"],
            "Silver:",
            medal_counts["Silver"],
            "Bronze:",
            medal_counts["Bronze"],
        )


def main():
    load_records()

    while True:
        print("\nOlympic Records Management System")
        print("1. Add Details")
        print("2. View Details")
        print("3. View Medal Count by Country")
        print("4. Search Athlete Performance")
        print("5. View Event Details")
        print("6. View Statistics")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_athlete()
        elif choice == "2":
            view_athletes()
        elif choice == "3":
            view_medal_count()
        elif choice == "4":
            search_athlete()
        elif choice == "5":
            view_event()
        elif choice == "6":
            view_statistics()
        elif choice == "7":
            print("Saving changes and exiting the program.")
            save_records()
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
