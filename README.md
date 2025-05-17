# Fall Detection System

A computer vision-based system for detecting falls in video footage using pose estimation and angular analysis.

## Overview

This project uses OpenPifPaf, a state-of-the-art pose estimation library, to detect human keypoints in video frames. The system analyzes the relationships and changes between these keypoints over time to identify potential fall events. Five different methods for fall detection are implemented and compared:

1. Division
2. Mean Difference
3. Difference Mean
4. Difference Sum
5. Mean

## Features

- Real-time fall detection in video streams
- Multiple detection methods for comparison
- Visualization tools for fall analysis
- Command-line interface for easy usage

## Requirements

- Python 3.7+
- OpenCV
- OpenPifPaf
- PyTorch
- NumPy
- Matplotlib

## Installation

1. Clone this repository:
```bash
git clone https://github.com/your-username/fall-detection.git
cd fall-detection
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Command Line Interface

To process a video file for fall detection:

```bash
python fall_detection.py --video path/to/video.mp4 --method DifferenceMean --save
```

To use webcam for real-time fall detection:

```bash
python fall_detection.py --webcam --camera_id 0 --method DifferenceMean --save
```

Parameters:
- `--video`: Path to the video file
- `--webcam`: Use webcam as input source
- `--camera_id`: Camera device ID (default: 0)
- `--method`: Detection method to use (default: "DifferenceMean")
  - Available methods: "Division", "MeanDifference", "DifferenceMean", "DifferenceSum", "Mean"
- `--save`: Flag to save the processed video with annotations

### Using as a Module

```python
from utils import FeatureExtractor

# Initialize the feature extractor
feature_extractor = FeatureExtractor()

# Process a video file
cost = feature_extractor.realTimeVideo("path/to/video.mp4", "DifferenceMean", save=True)

# Or use webcam
cost = feature_extractor.realTimeVideo("webcam:0", "DifferenceMean", save=True)
```

## How It Works

1. **Pose Estimation**: Uses OpenPifPaf to detect human keypoints in each frame
2. **Feature Extraction**: Calculates angles between specific body parts
3. **Analysis**: Applies different methods to analyze changes in angles over time
4. **Detection**: Identifies fall events when the cost function exceeds a predetermined threshold

## Method Comparison

The system implements five different methods for detecting falls:

1. **Division**: Compares the ratio of current to previous frame angles
2. **Mean Difference**: Compares the difference between the mean angles of current and previous frames
3. **Difference Mean**: Calculates the mean of the differences between angles in current and previous frames
4. **Difference Sum**: Sums the differences between angles in current and previous frames
5. **Mean**: Uses only the mean of the current frame angles

## Examples

The repository includes sample videos in the `assets/videos` directory that can be used to test the system.

Run the example script to visualize all five methods on a sample video:

```bash
python index.py
```

Or try the webcam-based fall detection demo:

```bash
python webcam_demo.py
```

## Webcam Usage

The system supports real-time fall detection using a webcam. You can use the dedicated webcam demo script:

```bash
python webcam_demo.py --camera_id 0 --method DifferenceMean --save
```

Tips for webcam usage:
1. Ensure you have good lighting
2. Position the camera to capture your full body
3. Try to have a clear background
4. Maintain a distance of at least 2 meters from the camera
5. Move slowly to allow the system to track your movements accurately

## License

[MIT License](LICENSE)

## Contributors

- Your Name
