import argparse

from utils import FeatureExtractor, KeyPoints

parser = argparse.ArgumentParser(description="Process a video or webcam stream for fall detection")
parser.add_argument(
    "--video", metavar="Video", help="The video file to be processed", default=None
)
parser.add_argument(
    "--webcam", action="store_true", help="Use webcam as input source"
)
parser.add_argument(
    "--camera_id", type=int, default=0, help="Camera device ID (default: 0)"
)
parser.add_argument(
    "-m",
    "--method",
    metavar="Method",
    help="The type of the cost calculated. Available methods: Division, MeanDifference, DifferenceMean, DifferenceSum, Mean",
    nargs="?",
    default="DifferenceMean",
    const="DifferenceMean",
)
parser.add_argument(
    "--save", action=argparse.BooleanOptionalAction, help="Save or not save the output video"
)

args = parser.parse_args()

if __name__ == "__main__":
    featureextractor = FeatureExtractor()
    
    if args.webcam:
        # Use webcam input
        print(f"Starting fall detection using webcam (camera ID: {args.camera_id})...")
        print(f"Detection method: {args.method}")
        print("Press 'ESC' to exit")
        cost = featureextractor.realTimeVideo(f"webcam:{args.camera_id}", str(args.method), args.save)
    elif args.video:
        # Use video file input
        print(f"Processing video: {args.video}")
        print(f"Detection method: {args.method}")
        cost = featureextractor.realTimeVideo(str(args.video), str(args.method), args.save)
    else:
        print("Error: Either --video or --webcam must be specified")
        parser.print_help() 