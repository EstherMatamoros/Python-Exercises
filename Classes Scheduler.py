#Classes Scheduler
#We will create a loop that runs once fro each class, joins it with a time slot at the same 
#index, and saves the schedule in a new list

def schedule_classes(classes, times):
    schedule = []

    index = 0
    while index < len(classes):
        scheduled_class = classes[index] + ":" + times[index]
        schedule.append(scheduled_class)
        index += 1

    return schedule

#Data
classes = ["Algebra", "History", "Biology", "Swimming"]
times = ["9a.m.", "11a.m.", "1p.m.", "3p.m."]
schedule = schedule_classes(classes, times)
print(f"Monday's schedule: {schedule}")

