import argparse
import os
import sys
from tqdm import tqdm
import ffmpeg

parser = argparse.ArgumentParser()
parser.add_argument("in_dir", help="directory of files to transcode")
parser.add_argument("out_dir", default=None, nargs="?", help="destination directory for transcoded videos. Same if not specified")
args = parser.parse_args()

IN_DIR = args.in_dir
OUT_DIR = IN_DIR if args.out_dir is None else args.out_dir

if __name__ == "__main__":
    if not os.path.isdir(IN_DIR):
        print(f"Input directory: \"{IN_DIR}\" does not exist")
        sys.exit(1)

    if not os.path.isdir(OUT_DIR):
        print(f"Destination directory: \"{OUT_DIR}\" does not exist")
        sys.exit(1)

    for file in tqdm(os.listdir(IN_DIR)):
        file_path = f"{IN_DIR}/{file}"

        if os.path.isfile(file_path):
            file_name, file_extension = os.path.splitext(file)

            if file_extension == ".mp4":
                print(f"Skipping \"{file_path}\": already mp4")
                continue

            out_file_path = f"{OUT_DIR}/{file_name}.mp4"
            if os.path.exists(out_file_path):
                print(f"Skipping \"{file_path}\": mp4 with the same name already exists")
                continue

            print(f"Transcoding: {file}")
            ffmpeg.input(file_path).output(out_file_path, vcodec="libx264").run()
            print("\n"*5)
