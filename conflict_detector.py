def time_to_minutes(time):
    hours, minutes = map(int, time.split(":"))
    return hours * 60 + minutes


def is_time_overlap(start1, end1, start2, end2):
    start1 = time_to_minutes(start1)
    end1 = time_to_minutes(end1)
    start2 = time_to_minutes(start2)
    end2 = time_to_minutes(end2)

    return start1 < end2 and start2 < end1


def detect_conflicts(timetable):
    conflicts = []

    for i in range(len(timetable)):
        for j in range(i + 1, len(timetable)):

            class1 = timetable[i]
            class2 = timetable[j]

            if class1["day"].lower() == class2["day"].lower():

                if is_time_overlap(
                    class1["start_time"],
                    class1["end_time"],
                    class2["start_time"],
                    class2["end_time"]
                ):

                    if class1["room"].lower() == class2["room"].lower():
                        conflict_type = "Room Conflict"

                    elif class1["teacher"].lower() == class2["teacher"].lower():
                        conflict_type = "Teacher Conflict"

                    else:
                        conflict_type = "Time Conflict"

                    conflicts.append(
                        (class1, class2, conflict_type)
                    )

    return conflicts