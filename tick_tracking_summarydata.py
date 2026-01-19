import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Load the CSV
csv_path = ("C:\samplefile")#REPLACE WITH YOUR FILE PATH
df = pd.read_csv(csv_path)

# Remove all rows with NaN values
df = df.dropna()

# Get filename for output
file_name = os.path.basename(csv_path)
print(f"Analyzing file: {file_name}")

#Replace based on camera used by using the "TickScalingfinder.py"
cm_per_pixel = 0.0343
pixels_per_cm = 29.13


# --- Extract coordinates ---
x = df['trajectories1'].values
y = df['trajectories2'].values
x = -x
time = df['time'].values

# --- Trajectory Plot (normalized to cm) ---
plt.figure()
plt.plot(x * cm_per_pixel, y * cm_per_pixel, marker='o', markersize=3, label="Trajectory")

# Highlight start position in red
plt.scatter(x[0] * cm_per_pixel, y[0] * cm_per_pixel, color='red', s=80, zorder=5, label="Start")

plt.title("Tick Trajectory (XY Path, cm)")
plt.xlabel("X position (cm)")
plt.ylabel("Y position (cm)")
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()

# --- Compute step distance and cumulative distance ---
dx = df['trajectories1'].diff()
dy = df['trajectories2'].diff()
df['StepDistance_px'] = np.sqrt(dx**2 + dy**2)
df['CumulativeDistance_px'] = df['StepDistance_px'].cumsum()

# Convert to cm
df['StepDistance_cm'] = df['StepDistance_px'] * cm_per_pixel
df['CumulativeDistance_cm'] = df['CumulativeDistance_px'] * cm_per_pixel

# --- Compute Speed (cm/s) ---
dt = df['time'].diff()
df['Speed_cm_s'] = df['StepDistance_cm'] / dt

# --- Cumulative Distance vs Time ---
plt.figure()
plt.plot(df['time'], df['CumulativeDistance_cm'])
plt.title("Cumulative Distance Traveled vs Time (cm)")
plt.xlabel("Time (s)")
plt.ylabel("Cumulative Distance (cm)")
plt.grid(True)
plt.show()

# --- Basic Stats ---
total_time = df['time'].iloc[-1] - df['time'].iloc[0]
max_speed = df['Speed_cm_s'].max()
avg_speed = df['Speed_cm_s'].mean()
moving_speed = df['Speed_cm_s'][df['Speed_cm_s'] > 0.01].mean()

displacement_px = np.sqrt(
    (df['trajectories1'].iloc[-1] - df['trajectories1'].iloc[0])**2 +
    (df['trajectories2'].iloc[-1] - df['trajectories2'].iloc[0])**2
)
displacement_cm = displacement_px * cm_per_pixel

moving_time = dt[df['Speed_cm_s'] > 0.01].sum()
percent_time_moving = (moving_time / total_time) * 100

# --- Print Results ---
print()
print(f"Total Time of Run: {total_time:.2f} seconds")
print(f"Max Speed: {max_speed:.3f} cm/s")
print(f"Average Speed: {avg_speed:.3f} cm/s")
print(f"Average Speed While Moving: {moving_speed:.3f} cm/s")
print(f"Displacement: {displacement_cm:.3f} cm")
print(f"Time Moving: {moving_time:.2f} s ({percent_time_moving:.2f}%)")

# --- Save Summary ---
summary = {
    "File": file_name,
    "Total Time (s)": total_time,
    "Max Speed (cm/s)": max_speed,
    "Average Speed (cm/s)": avg_speed,
    "Avg Speed While Moving (cm/s)": moving_speed,
    "Displacement (cm)": displacement_cm,
    "Time Moving (s)": moving_time,
    "Percent Time Moving": percent_time_moving,
    "Scale (cm/pixel)": cm_per_pixel
}

# --- Uncomment if you want output files ---

# output_dir = r"C:\samplefile"
# os.makedirs(output_dir, exist_ok=True)
#
# session_name = os.path.splitext(file_name)[0]
# output_csv = os.path.join(output_dir, f"{session_name}_summary.csv")
#
# pd.DataFrame([summary]).to_csv(output_csv, index=False)
# print(f"Summary written to {output_csv}")