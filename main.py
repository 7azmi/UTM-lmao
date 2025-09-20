import pandas as pd
import matplotlib.pyplot as plt

# --- Step 1: Load the dataset ---
df = pd.read_csv("carrymarks.csv") # download here: https://drive.google.com/file/d/1cWbeVwghJe6zlZvk90ikile7UtcTfQ_J/view?usp=drive_link

# --- Step 2: Compute total marks for each student ---
score_columns = ["Assign1","Assign2","Assign3","Assign4","Assign5",
                 "Quiz1","Quiz2","Quiz3","Midterm","Final"]
df["Total"] = df[score_columns].sum(axis=1)

# --- Step 3: Group by group and calculate average total ---
group_totals = df.groupby("Group")["Total"].mean().reset_index()

# --- Step 4: Visualize ---
plt.figure(figsize=(10,6))
plt.bar(group_totals["Group"], group_totals["Total"], color="skyblue", edgecolor="black")
plt.xticks(rotation=45, ha="right")
plt.title("Average Total Marks by Group")
plt.xlabel("Group")
plt.ylabel("Average Total Marks")
plt.tight_layout()
plt.show()

# TODO: Some UTM students from FC faculty were cheating during last semester.
#  Can you find the cheater pattern in this dataset and visualise it in the plot? 
# The correct plot pattern exposes the cheating students clearly.
# Submit your plot image to your mentor in Whatsapp. (20 Tokens)
