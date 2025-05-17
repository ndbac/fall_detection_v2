import argparse
import matplotlib.pyplot as plt
import os

from utils import FeatureExtractor

def compare_methods(video_path, save_plot=False):
    """
    Compare all available fall detection methods on a single video
    
    Args:
        video_path (str): Path to the video file to analyze
        save_plot (bool): Whether to save the plot as an image
    """
    featureextractor = FeatureExtractor()
    
    # List of all available detection methods
    methods = ['Division', 'DifferenceSum', 'MeanDifference', 'DifferenceMean', 'Mean']
    costs = {}
    
    # Process video with each method
    for method in methods:
        print(f"Processing video with {method} method...")
        cost = featureextractor.processVideo(video_path, method)
        costs[method] = cost
    
    # Plot results for comparison
    fig, ax = plt.subplots(1, len(methods), figsize=(25, 5))
    fig.suptitle('Fall Detection Method Comparison', fontsize=16)
    
    # Estimate fall period (can be adjusted based on your video)
    # For the sample video, frames 11-19 contain the fall
    fall_start = 11
    fall_end = 19
    
    # Plot each method
    for i, method in enumerate(methods):
        featureextractor.plot(ax[i], costs[method], method, fall_start, fall_end)
    
    # Set plot appearance
    fig.patch.set_facecolor('white')
    plt.tight_layout()
    
    if save_plot:
        output_dir = os.path.join(os.path.dirname(video_path), 'results')
        os.makedirs(output_dir, exist_ok=True)
        plt.savefig(os.path.join(output_dir, 'method_comparison.png'), dpi=300)
    
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compare fall detection methods")
    parser.add_argument("--video", default="./assets/videos/fall.mp4", 
                        help="Path to the video file (default: ./assets/videos/fall.mp4)")
    parser.add_argument("--save", action="store_true", 
                        help="Save the comparison plot")
    
    args = parser.parse_args()
    compare_methods(args.video, args.save)
