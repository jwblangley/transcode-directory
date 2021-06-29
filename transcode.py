import argparse
import os
import sys
from tqdm import tqdm
import ffmpeg

parser = argparse.ArgumentParser()
parser.add_argument("dir", help="directory of files to transcode")
args = parser.parse_args()

DIR = args.dir

if __name__ == "__main__":
    if not os.path.isdir(DIR):
        print(f"Directory: \"{DIR}\" does not exist")
        sys.exit(1)

    for file in tqdm(os.listdir(DIR)):
        file_path = f"{DIR}/{file}"

        if os.path.isfile(file_path):
            file_name, file_extension = os.path.splitext(file)

            if file_extension == ".mp4":
                print(f"Skipping \"{file_path}\": already mp4")
                continue

            out_file_path = f"{DIR}/{file_name}.mp4"

            print(f"Transcoding: {file}")
            ffmpeg.input(file_path).output(out_file_path, vcodec="libx264").run()
            print("\n"*5)
