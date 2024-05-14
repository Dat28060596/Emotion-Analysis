---

# Real-Time Emotion Analysis with DeepFace

This project performs real-time emotion analysis on live camera feed using DeepFace, OpenCV, and Matplotlib. It captures frames from the camera, analyzes them for emotions, and displays the emotion probabilities in a dynamic bar chart.

## Features

- Analyzes emotions including anger, disgust, fear, happiness, sadness, surprise, and neutral.
- Displays real-time emotion analysis using Matplotlib.
- Easily customizable for different camera setups and applications.

## Prerequisites

- Python 3.9
- OpenCV (cv2)
- Matplotlib
- DeepFace

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Dat28060596/Emotion-Analysis
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Connect your camera to your computer.

2. Run the `real_time_emotion_analysis.py` script:

   ```bash
   python real_time_emotion_analysis.py
   ```

3. Observe the real-time emotion analysis displayed in the Matplotlib window.
   
4. Press 'q' to exit the application.

## Configuration

- **Camera Selection**: If you have multiple cameras connected to your computer, you can change the camera index in the script (`camera = cv2.VideoCapture(0)`).
  
- **Emotion Analysis Model**: The script uses DeepFace for emotion analysis. You can customize the model or parameters for more specific analysis requirements.

## Credits

This project utilizes the [DeepFace](https://github.com/serengil/deepface) library for face analysis.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to use and modify this code according to your needs.
