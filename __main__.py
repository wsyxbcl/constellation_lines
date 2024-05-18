import argparse

from utils import FishEyeImage
from pathlib import Path

parser = argparse.ArgumentParser(
    description="Draw constellation lines on given image"
)
parser.add_argument("raw_file_path", help="Path to the raw file")
parser.add_argument("jpeg_file_path", help="Path to the jpeg file")
parser.add_argument("-f", type=float, required=True, help="Focal length of the lens")

args = parser.parse_args()

pic = FishEyeImage(args.jpeg_file_path, args.raw_file_path, f=args.f, k=1)
print(args.f)
print(type(args.f))
pic.solve(solve_size=1000)

output_path = Path(args.jpeg_file_path).parent.joinpath("output.jpg")
pic.constellation(fn=output_path)