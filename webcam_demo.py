#!/usr/bin/env python3
"""
Webcam-based Fall Detection Demo

This script provides a simple interface to test fall detection using your webcam.
Press 'ESC' to exit the program.
"""

import argparse
from utils import FeatureExtractor

def run_webcam_demo(camera_id=0, method="DifferenceMean", save=False):
    """
    Run fall detection on webcam input
    
    Args:
        camera_id (int): Camera device ID
        method (str): Fall detection method
        save (bool): Save output video
    """
    print(f"Starting fall detection using camera ID {camera_id}")
    print(f"Detection method: {method}")
    print("Press 'ESC' to exit")
    
    feature_extractor = FeatureExtractor()
    result = feature_extractor.realTimeVideo(f"webcam:{camera_id}", method, save)
    
    if isinstance(result, str) and result.startswith("Error"):
        print(f"Detection failed: {result}")
    else:
        print("Detection completed successfully")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Webcam-based Fall Detection Demo")
    parser.add_argument("--camera_id", type=int, default=0, 
                        help="Camera device ID (default: 0)")
    parser.add_argument("--method", default="DifferenceMean", 
                        choices=["Division", "DifferenceSum", "MeanDifference", "DifferenceMean", "Mean"],
                        help="Fall detection method (default: DifferenceMean)")
    parser.add_argument("--save", action="store_true", 
                        help="Save output video")
    
    args = parser.parse_args()
    run_webcam_demo(args.camera_id, args.method, args.save) 