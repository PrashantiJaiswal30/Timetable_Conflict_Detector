def load_timetable(filename):
    timetable = []

    try:
        with open(filename, "r") as file:
            for line in file:
                data = line.strip().split(",")

                if len(data) == 6:
                    class_info = {
                        "day": data[0],
                        "subject": data[1],
                        "start_time": data[2],
                        "end_time": data[3],
                        "room": data[4],
                        "teacher": data[5]
                    }

                    timetable.append(class_info)

    except FileNotFoundError:
        print("Timetable data file not found.")

    return timetable


def add_class(timetable, filename):
    print("\n========== ADD NEW CLASS ==========")

    day = input("Enter day: ")
    subject = input("Enter subject: ")
    start_time = input("Enter start time (HH:MM): ")
    end_time = input("Enter end time (HH:MM): ")
    room = input("Enter room number: ")
    teacher = input("Enter teacher name: ")

    class_info = {
        "day": day,
        "subject": subject,
        "start_time": start_time,
        "end_time": end_time,
        "room": room,
        "teacher": teacher
    }

    timetable.append(class_info)

    with open(filename, "a") as file:
        file.write(
            f"{day},{subject},{start_time},{end_time},{room},{teacher}\n"
        )

    print("\nClass added successfully.")