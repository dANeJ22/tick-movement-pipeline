import cv2
import matplotlib
matplotlib.use('TkAgg')  # Force interactive backend for PyCharm
import matplotlib.pyplot as plt


# Load one frame (replace with your video or image path)
frame = cv2.imread(r"C:\samplefile")

# Convert to RGB for matplotlib
frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

plt.ion()  # interactive mode on

plt.imshow(frame_rgb)
plt.title("Click two points across 5 cm square side")
points = plt.ginput(2)  # Click once on each side of the square edge
plt.close()

# Compute pixel distance
(x1, y1), (x2, y2) = points
pixel_distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

# Assuming 5cm Reference Square
cm_per_pixel = 5 / pixel_distance
pixels_per_cm = pixel_distance / 5

print(f"Pixels across 5 cm: {pixel_distance:.2f}")
print(f"Scale: {cm_per_pixel:.4f} cm/pixel  |  {pixels_per_cm:.2f} pixels/cm")

