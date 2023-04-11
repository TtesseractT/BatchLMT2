#######################################################
# Rosetta v1 Python Script - Created on 08/04/2023    #
#######################################################
# Built by Sabian Hibbs                               #
#                                                     #
#######################################################

import os
import sys
import subprocess
import math
import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")

def transcribe_audio(audio_file_path):
    with open(audio_file_path, "rb") as audio_file:
        transcript = openai.Audio.translate("whisper-1", audio_file)
        print(transcript)
        with open("transcripts.txt", "a") as transcript_file:
            transcript_file.write(str(transcript) + "\n")
            
def create_folder_if_not_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

def main():
    input_file = sys.argv[1]
    output_file = os.path.splitext(os.path.basename(input_file))[0] + ".mp3"
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Audio_Segment", output_file)
    create_folder_if_not_exists(os.path.dirname(output_path))
    audio_segment_folder_path = os.path.join(os.path.dirname(output_path), "Audio_Segment")
    create_folder_if_not_exists(audio_segment_folder_path)
    ffmpeg_extract_audio_cmd = f"ffmpeg -i \"{input_file}\" -vn -acodec libmp3lame -ac 1 -ab 64k -ar 22050 \"{output_path}\""
    subprocess.call(ffmpeg_extract_audio_cmd, shell=True)
    segment_duration = 50 * 60
    ffprobe_get_duration_cmd = f"ffprobe -i \"{output_path}\" -show_entries format=duration -v quiet -of csv=\"p=0\""
    audio_duration = float(subprocess.check_output(ffprobe_get_duration_cmd, shell=True).decode("utf-8").strip())
    num_segments = int(math.ceil(audio_duration / segment_duration))

    for i in range(num_segments):
        segment_output_path = os.path.join(audio_segment_folder_path, f"Audio_Segment_{str(i+1).zfill(2)}.mp3")
        segment_start_time = i * segment_duration
        ffmpeg_split_audio_cmd = f"ffmpeg -i \"{output_path}\" -ss {segment_start_time} -t {segment_duration} -vn -acodec copy \"{segment_output_path}\""
        subprocess.call(ffmpeg_split_audio_cmd, shell=True)

    for file in os.listdir(audio_segment_folder_path):
        if file.endswith(".mp3") and file.startswith("Audio_Segment"):
            audio_file_path = os.path.join(audio_segment_folder_path, file)
            transcribe_audio(audio_file_path)

    with open("transcripts.txt", "r") as transcript_file:
        contents = transcript_file.read()
        for char in ["text", ":", '"', "{", "}"]:
            contents = contents.replace(char, "")

    with open("transcripts.txt", "w") as transcript_file:
        transcript_file.write(contents)

if __name__ == "__main__":
    main()
