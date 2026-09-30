def display_timetable(timetable):
    print("\n========== TIMETABLE ==========")

    if not (timetable) :        
        print("No timetable data available.")
        return

    for i, class_info in enumerate(timetable, 1):
        print(f"\nClass {i}")
        print("Day       :", class_info["day"])
        print("Subject   :", class_info["subject"])
        print(
            "Time      :",
            class_info["start_time"],
            "-",
            class_info["end_time"]
        )
        print("Room      :", class_info["room"])
        print("Teacher   :", class_info["teacher"])


def display_conflicts(conflicts):
    print("\n========== CONFLICTS ==========")

    if not conflicts:
        print("No timetable conflicts found.")
        return

    print("Timetable conflicts found:")

    for i, (class1, class2, conflict_type) in enumerate(conflicts, 1):

        print(f"\nConflict {i}")
        print("Type:", conflict_type)
        print("Day :", class1["day"])

        print(
            class1["subject"],
            "(",
            class1["start_time"],
            "-",
            class1["end_time"],
            ")"
        )

        print(
            class2["subject"],
            "(",
            class2["start_time"],
            "-",
            class2["end_time"],
            ")"
        )

        print("Room 1   :", class1["room"])
        print("Room 2   :", class2["room"])
        print("Teacher 1:", class1["teacher"])
        print("Teacher 2:", class2["teacher"])