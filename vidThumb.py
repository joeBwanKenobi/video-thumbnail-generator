#! /usr/bin/env python3
import ffmpeg, sys, os

source_dir = sys.argv[1]
thumb_dir = sys.argv[2]
thumb_width = 800 # pixels
thumb_time = 55 # seconds
extension = '.png'

def generate_thumbnail(in_filename, out_filename, time, width):
    try:
        (
            ffmpeg
            .input(in_filename, ss=time)
            .filter('scale', width, -1)
            .output(out_filename, vframes=1)
            .overwrite_output()
            .run(capture_stdout=True, capture_stderr=True)
        )
    except ffmpeg.Error as e:
        print(e.stderr.decode(), file=sys.stderr)
        sys.exit(1)

for vid in os.listdir(source_dir):
    title = vid.split('.')[0] + extension
    out_path = thumb_dir + title
    print("Generating thumbnail: " + out_path)
    generate_thumbnail(source_dir + vid, out_path, thumb_time, thumb_width)