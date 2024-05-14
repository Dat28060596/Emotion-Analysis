import pandas as pd
from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt

# Initialize the camera
camera = cv2.VideoCapture(0)  # 0 for default camera, you can change it if you have multiple cameras

# Check if the camera opened successfully
if not camera.isOpened():
    print("Error: Could not open camera.")
    exit()

# Create a matplotlib figure
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots()

# Continuously capture frames
while True:
    # Capture a frame
    ret, frame = camera.read()

    # Show the frame in a window (optional)
    cv2.imshow('Camera', frame)

    if not ret:
        print("Error: Could not capture frame.")
        break

    try:
        demography = DeepFace.analyze(
            img_path=frame,
            actions=['emotion']  # Only analyze emotions to speed up the process
        )

        if isinstance(demography, list):
            demography = demography[0]  # Assuming we need the first element

        # Extract emotions and plot
        emotions = demography["emotion"]
        emo_df = pd.DataFrame(emotions, index=[0]).T
        emo_df.columns = ['Probability']  # Rename the column for better readability

        # Clear the previous plot
        ax.clear()

        # Plot the emotions
        emo_df.plot(kind='bar', legend=False, ax=ax)
        ax.set_xlabel('Emotions')
        ax.set_ylabel('Probability')
        ax.set_title('Emotion Analysis')

        # Pause to allow the plot to update
        plt.pause(0.01)

    except Exception as e:
        print(f"Error in DeepFace analysis: {e}")

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
plt.ioff()  # Turn off interactive mode
plt.show()
