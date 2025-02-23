# Traffic Monitoring and Vehicle Counting System

## Overview

This project implements a traffic monitoring system that detects and tracks vehicles in a video stream. Using state-of-the-art object detection and tracking algorithms, the system identifies vehicles, tracks them over time, and counts them as they cross a designated line in the video. The final output overlays detection boxes, tracking IDs, and a counting mechanism on the video frames.

## Approach

The solution is structured into several key steps:

1. **Video Capture and Preprocessing:**  
   The system reads frames from a video file (`traffic.mp4`). A mask (`mask.png`) is optionally applied to focus on regions of interest, ensuring that only relevant areas of the frame are processed.

2. **Object Detection with YOLOv8:**  
   - The YOLOv8 model (`yolov8l.pt`) is used to detect objects in each frame.
   - Detections are filtered by confidence (threshold > 0.3) and restricted to vehicle classes (car, truck, bus, motorbike).

3. **Tracking with SORT:**  
   - The SORT (Simple Online and Realtime Tracking) algorithm tracks detected vehicles across frames by assigning unique IDs.
   - This helps in reliably counting vehicles as they cross a specific line without double-counting.
   - **Installation:** SORT is installed from GitHub. You can clone the repository from [abewley/sort](https://github.com/abewley/sort) and use the `sort.py` file in your project.

4. **Vehicle Counting:**  
   - A vertical line is defined (at x=320, from y=-100 to y=600).
   - The center point of each tracked vehicle is computed, and when a vehicle’s center crosses the line (within a ±15 pixel range), it is counted.
   - Once a vehicle is counted, its ID is stored to avoid duplicate counts.

5. **Visualization:**  
   - The system overlays bounding boxes, tracking IDs, and the counting line on the video frames.
   - The counting line changes color (from red to green) when a vehicle is counted, providing immediate visual feedback.

## Technologies and Tools Used

- **Python:** The primary programming language.
- **OpenCV:** For video processing, image manipulation, and drawing functionalities.
- **YOLOv8 (Ultralytics):** Object detection model to identify vehicles.
- **PyTorch:** Underlying framework for running the YOLO model.
- **cvzone:** Enhances OpenCV functionalities, particularly for drawing and text overlay.
- **SORT:** Algorithm for tracking objects across video frames, installed via GitHub.
- **NumPy:** For numerical operations and array manipulations.

## Steps to Reproduce the Results

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/29aitch/FamilyMartAssesment
   cd <repository_directory>
   
2. Install Python Dependencies: Ensure you have Python 3.10 installed. Install the required packages:

   ```bash
   pip install requirement.txt

For detailed PyTorch installation instructions, visit the PyTorch website.

3. Install SORT: SORT is not available via PyPI and must be installed from GitHub:

   Clone the SORT repository:
   ```bash
   git clone https://github.com/abewley/sort.git

Copy the sort.py file from the cloned repository into your project directory or add the SORT repository to your Python path.
   Alternatively, you can install it directly if a setup file is available, or manually include the file in your project.
   
4. Prepare Input Files:

   Place the video file traffic.mp4 in the project directory.
   Add the mask image mask.png (if using a mask).
   Download the YOLOv8 model weights (yolov8l.pt) from the Ultralytics YOLO website and place it in the same directory.
   Run the Application: Execute the main script:
   ```bash
   python main.py
   
5. A window will display the video stream with the overlay of detections, tracking IDs, and the vehicle count.

6. Exit the Application: Press the ESC key to close the video window.

**Encountered Challenges and Resolutions**
Mask Resizing Issue:
The mask image often did not match the video frame dimensions, leading to misalignment when applying the mask.
Resolution: The mask is dynamically resized at runtime to match the dimensions of the video frame.

Performance Bottlenecks:
Running the YOLOv8 model on a CPU resulted in slow processing speeds, affecting real-time performance.
Resolution: The model was optimized for GPU usage where available, and a lighter model variant was considered to enhance processing speed on lower-end hardware.

Variable Lighting Conditions:
Changes in lighting and weather conditions in the video sometimes affected the detection confidence and overall performance.
Resolution: Preprocessing steps were added to normalize brightness and contrast, and the confidence threshold was dynamically adjusted based on real-time feedback.

Integration of Multiple Libraries:
Combining outputs from YOLO, cvzone, and SORT required careful handling of coordinate systems and data types.
Resolution: Detailed logging and iterative debugging helped ensure consistent data processing across all components.

