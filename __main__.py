import argparse

from utils import FishEyeImage
from pathlib import Path

parser = argparse.ArgumentParser(description="Draw constellation lines on given image")
parser.add_argument("raw_file_path", help="Path to the raw file")
parser.add_argument("jpeg_file_path", help="Path to the jpeg file")
parser.add_argument("-f", type=float, help="Focal length")
parser.add_argument("-k", type=float, help="k value, ref. https://ptgui.com/support.html#3_28")

args = parser.parse_args()

k = args.k if args.k else 1.0
pic = FishEyeImage(args.jpeg_file_path, args.raw_file_path, f=args.f, k=k)

pic.solve(solve_size=1000)

if not pic.f:
    pic.calculate_focal_length()

output_path = Path(args.jpeg_file_path).parent.joinpath("output.jpg")
pic.constellation(fn=output_path)
print(f"Output: {output_path}")
