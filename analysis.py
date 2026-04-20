import pandas as pd
import matplotlib.pyplot as plt
import random
from datetime import datetime, timedelta

print("Program started...")

# ---------- STEP 1: Generate 3 months data ----------
start_date = datetime(2025, 1, 1)
data = []

courses = ["Python Basics", "Web Development", "Data Science"]

for i in range(1, 301):  # 300 records
    date = start_date + timedelta(days=random.randint(0, 90))
    user_id = 100 + i
    course = random.choice(courses)
    time_spent = random.randint(30, 240)
    sessions = random.randint(1, 7)

    if time_spent > 100:
        completion = "Completed"
        rating = random.randint(4, 5)
    else:
        completion = "Not Completed"
        rating = random.randint(2, 4)

    data.append([user_id, course, time_spent, sessions, completion, rating, date])

# ---------- STEP 2: Create DataFrame ----------
df = pd.DataFrame(data, columns=[
    "User_ID", "Course_Name", "Time_Spent",
    "Sessions_Per_Week", "Completion_Status",
    "Feedback_Rating", "Date"
])

# Save dataset (important for proof)
df.to_csv("user_data_generated.csv", index=False)

# ---------- STEP 3: Print Output ----------
print("\nSample Data:\n", df.head())

print("\nAverage Time Spent:", df["Time_Spent"].mean())
print("\nCompletion Count:\n", df["Completion_Status"].value_counts())

course_engagement = df.groupby("Course_Name")["Time_Spent"].mean()
print("\nAverage Time per Course:\n", course_engagement)

# ---------- STEP 4: Graphs ----------

# Graph 1
df.groupby("Completion_Status")["Time_Spent"].mean().plot(kind='bar')
plt.title("Time Spent vs Completion")
plt.xlabel("Completion Status")
plt.ylabel("Average Time Spent")
plt.show(block=True)

# Graph 2
course_engagement.plot(kind='bar')
plt.title("Course Engagement")
plt.xlabel("Course")
plt.ylabel("Average Time Spent")
plt.show(block=True)

# Graph 3
df.groupby("Course_Name")["Feedback_Rating"].mean().plot(kind='bar')
plt.title("Feedback Ratings")
plt.xlabel("Course")
plt.ylabel("Rating")
plt.show(block=True)

# Graph 4 (extra - looks professional)
df.groupby("Date")["Time_Spent"].mean().plot()
plt.title("Daily Engagement Trend")
plt.xticks(rotation=45)
plt.show(block=True)

input("\nPress Enter to exit...")