# Facial Detection
A simple implementation of facial detection using OpenCV and Python.

## Requirements
- OpenCV
- Python 3

## Usage
1. Clone the repository
2. Run the script with the path to the Haar cascade as an argument:
```
python facial_detection.py /path/to/cascade
```
3. The program will start using the default webcam to detect faces.
4. Press `q` to quit the program.

## Notes
- The program displays the number of faces detected in the top left of the frame.
- The faces are surrounded by rectangle-like shapes drawn with green lines.
- I have provided two Haar cascades (one for human faces and one for cat faces), however others should work.
- If using your own Haar cascade, you may need to adjust the scaleFactor and minNeighbors variables for better accuracy
