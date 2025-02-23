{\rtf1\ansi\ansicpg1252\cocoartf2820
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier-Bold;\f1\fmodern\fcharset0 Courier;\f2\froman\fcharset0 Times-Bold;
\f3\froman\fcharset0 Times-Roman;\f4\froman\fcharset0 TimesNewRomanPSMT;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red0\green0\blue233;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;\cssrgb\c0\c0\c93333;}
{\*\listtable{\list\listtemplateid1\listhybrid{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat2\levelspace360\levelindent0{\*\levelmarker \{decimal\}}{\leveltext\leveltemplateid1\'01\'00;}{\levelnumbers\'01;}\fi-360\li720\lin720 }{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{circle\}}{\leveltext\leveltemplateid2\'01\uc0\u9702 ;}{\levelnumbers;}\fi-360\li1440\lin1440 }{\listname ;}\listid1}
{\list\listtemplateid2\listhybrid{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat2\levelspace360\levelindent0{\*\levelmarker \{decimal\}}{\leveltext\leveltemplateid101\'01\'00;}{\levelnumbers\'01;}\fi-360\li720\lin720 }{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{circle\}}{\leveltext\leveltemplateid102\'01\uc0\u9702 ;}{\levelnumbers;}\fi-360\li1440\lin1440 }{\listname ;}\listid2}
{\list\listtemplateid3\listhybrid{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat2\levelspace360\levelindent0{\*\levelmarker \{decimal\}}{\leveltext\leveltemplateid201\'01\'00;}{\levelnumbers\'01;}\fi-360\li720\lin720 }{\listname ;}\listid3}
{\list\listtemplateid4\listhybrid{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat2\levelspace360\levelindent0{\*\levelmarker \{decimal\}}{\leveltext\leveltemplateid301\'01\'00;}{\levelnumbers\'01;}\fi-360\li720\lin720 }{\listname ;}\listid4}
{\list\listtemplateid5\listhybrid{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{decimal\}}{\leveltext\leveltemplateid401\'01\'00;}{\levelnumbers\'01;}\fi-360\li720\lin720 }{\listname ;}\listid5}}
{\*\listoverridetable{\listoverride\listid1\listoverridecount0\ls1}{\listoverride\listid2\listoverridecount0\ls2}{\listoverride\listid3\listoverridecount0\ls3}{\listoverride\listid4\listoverridecount0\ls4}{\listoverride\listid5\listoverridecount0\ls5}}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\b\fs26 \cf0 \expnd0\expndtw0\kerning0
# Traffic Monitoring and Vehicle Counting System
\f1\b0 \
\

\f0\b ## Overview
\f1\b0 \
\
This project implements a traffic monitoring system that detects and tracks vehicles in a video stream. Using state-of-the-art object detection and tracking algorithms, the system identifies vehicles, tracks them over time, and counts them as they cross a designated line in the video. The final output overlays detection boxes, tracking IDs, and a counting mechanism on the video frames.\
\

\f0\b ## Approach
\f1\b0 \
\
The solution is structured into several key steps:\
\
1. 
\f0\b **Video Capture and Preprocessing:**  
\f1\b0 \
   The system reads frames from a video file (`traffic.mp4`). A mask (`mask.png`) is optionally applied to focus on regions of interest, ensuring that only relevant areas of the frame are processed.\
\
2. 
\f0\b **Object Detection with YOLOv8:**
\f1\b0   \
   - The YOLOv8 model (`yolov8l.pt`) is used to detect objects in each frame.\
   - Detections are filtered by confidence (threshold > 0.3) and restricted to vehicle classes (car, truck, bus, motorbike).\
\
3. 
\f0\b **Tracking with SORT:**  
\f1\b0 \
   - The SORT (Simple Online and Realtime Tracking) algorithm tracks detected vehicles across frames by assigning unique IDs.\
   - This helps in reliably counting vehicles as they cross a specific line without double-counting.\
   - **Installation:** SORT is installed from GitHub. You can clone the repository from [abewley/sort](https://github.com/abewley/sort) and use the `sort.py` file in your project.\
\
4. 
\f0\b **Vehicle Counting:**  
\f1\b0 \
   - A vertical line is defined (at x=320, from y=-100 to y=600).\
   - The center point of each tracked vehicle is computed, and when a vehicle\'92s center crosses the line (within a \'b115 pixel range), it is counted.\
   - Once a vehicle is counted, its ID is stored to avoid duplicate counts.\
\
5. 
\f0\b **Visualization:** 
\f1\b0  \
   - The system overlays bounding boxes, tracking IDs, and the counting line on the video frames.\
   - The counting line changes color (from red to green) when a vehicle is counted, providing immediate visual feedback.\
\

\f0\b ## Technologies and Tools Used
\f1\b0 \
\
- **Python:** The primary programming language.\
- **OpenCV:** For video processing, image manipulation, and drawing functionalities.\
- **YOLOv8 (Ultralytics):** Object detection model to identify vehicles.\
- **PyTorch:** Underlying framework for running the YOLO model.\
- **cvzone:** Enhances OpenCV functionalities, particularly for drawing and text overlay.\
- **SORT:** Algorithm for tracking objects across video frames, installed via GitHub.\
- **NumPy:** For numerical operations and array manipulations.\
\
## Steps to Reproduce the Results\
\
1.	**Clone the Repository:**\
   	bash\
   	git clone <repository_url>\
   	cd <repository_directory>\
\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sa240\partightenfactor0
\ls1\ilvl0
\f2\b\fs24 \cf0 \kerning1\expnd0\expndtw0 2.		\expnd0\expndtw0\kerning0
Install Python Dependencies:
\f3\b0  Ensure you have Python 3.10 installed. Install the required packages:\
\pard\tx940\tx1440\pardeftab720\li1440\fi-1440\sa240\partightenfactor0
\ls1\ilvl1
\f1\fs26 \cf0 	bash\
	pip install -r requirement.txt\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sa240\partightenfactor0
\ls1\ilvl0\cf0 \uc0\u8232 
\f3\fs24 For detailed PyTorch installation instructions, visit the {\field{\*\fldinst{HYPERLINK "https://pytorch.org/"}}{\fldrslt \cf3 \ul \ulc3 PyTorch website}}.\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sa240\partightenfactor0
\ls1\ilvl0
\f2\b \cf0 \kerning1\expnd0\expndtw0 3.		\expnd0\expndtw0\kerning0
Install SORT:
\f3\b0  SORT is not available via PyPI and must be installed from GitHub:\
\pard\tx940\tx1440\pardeftab720\li1440\fi-1440\partightenfactor0
\ls1\ilvl1\cf0 \kerning1\expnd0\expndtw0 {\listtext	
\f4 \uc0\u9702 
\f3 	}\expnd0\expndtw0\kerning0
Clone the SORT repository:
\f1\fs26 bash\uc0\u8232 git clone https://github.com/abewley/sort.git\
\ls1\ilvl1
\f3\fs24 \kerning1\expnd0\expndtw0 {\listtext	
\f4 \uc0\u9702 
\f3 	}\expnd0\expndtw0\kerning0
Copy the 
\f1\fs26 sort.py
\f3\fs24  file from the cloned repository into your project directory or add the SORT repository to your Python path.\
\ls1\ilvl1\kerning1\expnd0\expndtw0 {\listtext	
\f4 \uc0\u9702 
\f3 	}\expnd0\expndtw0\kerning0
Alternatively, you can install it directly if a setup file is available, or manually include the file in your project.\
\pard\tx720\tx1440\pardeftab720\partightenfactor0
\cf0 \
\pard\tx940\tx1440\pardeftab720\li1440\fi-1440\partightenfactor0
\ls2\ilvl1
\f2\b \cf0 \kerning1\expnd0\expndtw0 4.	\expnd0\expndtw0\kerning0
Prepare Input Files:
\f3\b0 \
\pard\tx940\tx1440\pardeftab720\li1440\fi-1440\partightenfactor0
\ls2\ilvl1\cf0 \kerning1\expnd0\expndtw0 {\listtext	
\f4 \uc0\u9702 
\f3 	}\expnd0\expndtw0\kerning0
Place the video file 
\f1\fs26 traffic.mp4
\f3\fs24  in the project directory.\
\ls2\ilvl1\kerning1\expnd0\expndtw0 {\listtext	
\f4 \uc0\u9702 
\f3 	}\expnd0\expndtw0\kerning0
Add the mask image 
\f1\fs26 mask.png
\f3\fs24  (if using a mask).\
\ls2\ilvl1\kerning1\expnd0\expndtw0 {\listtext	
\f4 \uc0\u9702 
\f3 	}\expnd0\expndtw0\kerning0
Download the YOLOv8 model weights (
\f1\fs26 yolov8l.pt
\f3\fs24 ) from the {\field{\*\fldinst{HYPERLINK "https://ultralytics.com/"}}{\fldrslt \cf3 \ul \ulc3 Ultralytics YOLO website}} and place it in the same directory.\
\pard\tx720\tx1440\pardeftab720\partightenfactor0
\cf0 \
\pard\tx220\tx720\pardeftab720\li720\fi-720\sa240\partightenfactor0
\ls3\ilvl0
\f2\b \cf0 \kerning1\expnd0\expndtw0 5.		\expnd0\expndtw0\kerning0
Run the Application:
\f3\b0  Execute the main script:\uc0\u8232 
\f1\fs26 bash\uc0\u8232 python main.py\
\uc0\u8232 
\f3\fs24 A window will display the video stream with the overlay of detections, tracking IDs, and the vehicle count.\
\pard\tx720\pardeftab720\partightenfactor0
\cf0 \
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls4\ilvl0\cf0 6.		
\f2\b Exit the Application:
\f3\b0  Press the 
\f1\fs26 ESC
\f3\fs24  key to close the video window.\
\pard\tx720\pardeftab720\partightenfactor0
\cf0 \
\
\pard\pardeftab720\sa298\partightenfactor0

\f2\b\fs36 \cf0 \outl0\strokewidth0 \strokec2 Encountered Challenges and Resolutions\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sa240\partightenfactor0
\ls5\ilvl0
\fs24 \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	1	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Mask Resizing Issue:
\f3\b0 \uc0\u8232 The mask image often did not match the video frame dimensions, leading to misalignment when applying the mask.\u8232 
\f2\b Resolution:
\f3\b0  The mask is dynamically resized at runtime to match the dimensions of the video frame.\
\ls5\ilvl0
\f2\b \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	2	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Performance Bottlenecks:
\f3\b0 \uc0\u8232 Running the YOLOv8 model on a CPU resulted in slow processing speeds, affecting real-time performance.\u8232 
\f2\b Resolution:
\f3\b0  The model was optimized for GPU usage where available, and a lighter model variant was considered to enhance processing speed on lower-end hardware.\
\ls5\ilvl0
\f2\b \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	3	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Tracking Inconsistencies:
\f3\b0 \uc0\u8232 Occasionally, the SORT tracker would mis-assign IDs when vehicles overlapped or occluded each other, leading to incorrect counts.\u8232 
\f2\b Resolution:
\f3\b0  Tracker parameters such as 
\f1\fs26 max_age
\f3\fs24 , 
\f1\fs26 min_hits
\f3\fs24 , and 
\f1\fs26 iou_threshold
\f3\fs24  were fine-tuned to better handle occlusions and minimize false reassignments.\
\ls5\ilvl0
\f2\b \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	5	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Integration of Multiple Libraries:
\f3\b0 \uc0\u8232 Combining outputs from YOLO, cvzone, and SORT required careful handling of coordinate systems and data types.\u8232 
\f2\b Resolution:
\f3\b0  Detailed logging and iterative debugging helped ensure consistent data processing across all components.\
\pard\tx720\pardeftab720\partightenfactor0
\cf0 \outl0\strokewidth0 \
}