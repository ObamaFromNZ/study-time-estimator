from datetime import datetime

# Questions
print("Welcome to the Study Time Estimator")
date = input("What is the exam date? (DD-MM-YYYY):\n>").strip()
amount = input("How many topics do you need to study?\n>")
time_spent = input("How many total hours do you want to spend?\n>")

#Calculation of variables
exam_date = datetime.strptime(date,"%d-%m-%Y")
today = datetime.now()
days_left = (exam_date-today).days
if days_left<0:
    print("That exam date has already passed!")
    exit()

topics = int(amount)
topics_per_day = round(topics/days_left,2)

total_hours = float(time_spent)
minutes_per_day = round((total_hours*60)/ days_left)


#Output
print(f"""You have {days_left} days left.\n
    To finish {amount} topics, you should study {topics_per_day} topics per day.\n
    To hit {time_spent} hours total, that's {minutes_per_day} minutes per day.\n 
    Lock in NOW.""")

#Saving plan to txt file
with open("study_plan.txt", "w") as f:
    f.write(f"Exam Date: {exam_date.date()}\n")
    f.write(f"Days Left: {days_left}\n")
    f.write(f"Topics Per Day:{topics_per_day}\n")
    f.write(f"Minutes Per Day: {minutes_per_day}\n")

print("Your study plan has been saved to 'study_plan.txt'.")
