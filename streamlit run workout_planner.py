import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# Function to generate workout plan based on goals
def generate_workout_plan(goal, days=7):
    workouts = {
        "Weight Loss": ["Running", "Cycling", "Jump Rope", "HIIT", "Swimming"],
        "Muscle Gain": ["Squats", "Deadlifts", "Bench Press", "Pull-Ups", "Push-Ups"],
        "General Fitness": ["Yoga", "Pilates", "Swimming", "Running", "Cycling"]
    }
    
    workout_plan = workouts.get(goal, [])
    if not workout_plan:
        return []
    
    plan = []
    for i in range(days):
        day = datetime.now() + timedelta(days=i)
        plan.append({
            "Date": day.strftime("%Y-%m-%d"),
            "Workout": np.random.choice(workout_plan)
        })
    return pd.DataFrame(plan)

# Function to track progress
def track_progress(goal, progress_data, days=7):
    progress = []
    for i in range(days):
        progress.append({
            "Date": datetime.now() + timedelta(days=i),
            "Progress": np.random.randint(0, 100)  # Random progress data (for demo purposes)
        })
    progress_df = pd.DataFrame(progress)
    progress_df["Goal"] = goal
    return progress_df

# Function to plot progress graph
def plot_progress_graph(progress_df):
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=progress_df, x="Date", y="Progress", marker="o")
    plt.title("Progress Over Time")
    plt.xlabel("Date")
    plt.ylabel("Progress (%)")
    st.pyplot(plt)

# Streamlit UI
st.title("Workout Planner")

# Sidebar: User Input
goal = st.sidebar.selectbox("Select Your Goal", ["Weight Loss", "Muscle Gain", "General Fitness"])
days = st.sidebar.slider("Select the number of days for workout plan", 1, 30, 7)

# Generate workout plan
st.subheader("Your Workout Plan")
workout_plan = generate_workout_plan(goal, days)
st.write(workout_plan)

# Track progress
st.subheader("Track Your Progress")
progress_data = track_progress(goal, workout_plan, days)
st.write(progress_data)

# Plot progress
st.subheader("Progress Visualization")
plot_progress_graph(progress_data)

# Display workout completion prompt
if st.button("Mark Workout as Completed"):
    st.success("Workout completed for today!")
    # Here, you could store the user's completion data for further tracking
