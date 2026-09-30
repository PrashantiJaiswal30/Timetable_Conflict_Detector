from timetable import load_timetable, add_class
from conflict_detector import detect_conflicts
from display import display_timetable, display_conflicts


def main():

    filename = "timetable_data.txt"

    print("======================================")
    print("     TIMETABLE CONFLICT DETECTOR")
    print("======================================")

    timetable = load_timetable(filename)

    while True:

        print("\n========== MENU ==========")
        print("1. Display Timetable")
        print("2. Detect Conflicts")
        print("3. Add New Class")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            display_timetable(timetable)

        elif choice == "2":

            conflicts = detect_conflicts(timetable)
            display_conflicts(conflicts)

        elif choice == "3":

            add_class(timetable, filename)

        elif choice == "4":

            print("\nThank you for using Timetable Conflict Detector.")
            print("Program ended.")
            break

        else:

            print("\nInvalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()