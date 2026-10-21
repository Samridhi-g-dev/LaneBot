LaneBot Dev Log

## Session 1: Setup & Basic Edge Detection
- **Date**: 22-10-2026
- **Accomplishments:**
  - Created project structure and Python virtual environment (`venv`).
  - Installed `opencv-python` and `numpy`.
  - Built a real-time webcam video stream script (`lanebot.py`).
  - Implemented grayscale conversion, Gaussian blur, and Canny edge detection.
  - Added live OpenCV trackbars to tune Canny lower and upper thresholds in real time.
**Key Learnings:**
  - Blurring is crucial before edge detection to eliminate high-frequency noise.
  - Live trackbars make parameter tuning much faster and more intuitive.
