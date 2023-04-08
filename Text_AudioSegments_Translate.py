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

# Initialize OpenAI API credentials
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Define function to transcribe audio file using OpenAI API
def translate_audio_file(audio_file_path):
    
    # Open audio file in read binary mode
    with open(audio_file_path, "rb") as audio_file:
        
        # Transcribe audio file using OpenAI API
        transcript = openai.Audio.translate("whisper-1", audio_file)
        
        # Print transcript
        print(transcript)
        
        # Write transcript to file
        with open("transcripts.txt", "a") as transcript_file:
            transcript_file.write(str(transcript) + "\n")
            
# Get input file path from command line argument
input_file = sys.argv[1]

# Set output file name and path
output_file = os.path.splitext(os.path.basename(input_file))[0] + ".mp3"
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Audio_Segment", output_file)

# Check if output directory exists, if not create it
if not os.path.exists(os.path.dirname(output_path)):
    os.makedirs(os.path.dirname(output_path))
    
# Check if Audio_Segment folder exists, if not create it
audio_segment_folder_path = os.path.join(os.path.dirname(output_path), "Audio_Segment")
if not os.path.exists(audio_segment_folder_path):
    os.makedirs(audio_segment_folder_path)
    
# Set ffmpeg command to extract audio and save as mp3
ffmpeg_cmd = f"ffmpeg -i \"{input_file}\" -vn -acodec libmp3lame -ac 1 -ab 64k -ar 22050 \"{output_path}\""

# Execute ffmpeg command to extract audio
subprocess.call(ffmpeg_cmd, shell=True)

# Set segment duration to 24 minutes
segment_duration = 50 * 60

# Get duration of extracted audio file
ffprobe_cmd = f"ffprobe -i \"{output_path}\" -show_entries format=duration -v quiet -of csv=\"p=0\""
audio_duration = float(subprocess.check_output(ffprobe_cmd, shell=True).decode("utf-8").strip())

# Calculate number of segments required to split audio file into segments of segment_duration
num_segments = int(math.ceil(audio_duration / segment_duration))

# Set ffmpeg command to split audio into segments and save as separate mp3 files
for i in range(num_segments):
    segment_output_path = os.path.join(audio_segment_folder_path, f"Audio_Segment_{str(i+1).zfill(2)}.mp3")
    segment_start_time = i * segment_duration
    ffmpeg_cmd = f"ffmpeg -i \"{output_path}\" -ss {segment_start_time} -t {segment_duration} -vn -acodec copy \"{segment_output_path}\""
    subprocess.call(ffmpeg_cmd, shell=True)
    
# Loop through Audio_Segment mp3 files and transcribe each file using OpenAI API
for file in os.listdir(audio_segment_folder_path):
    if file.endswith(".mp3") and file.startswith("Audio_Segment"):
        audio_file_path = os.path.join(audio_segment_folder_path, file)
        translate_audio_file(audio_file_path)
        
# Remove unwanted text from transcripts file
with open("transcripts.txt", "r") as transcript_file:
    contents = transcript_file.read()
    contents = contents.replace("text", "")
    contents = contents.replace(":", "")
    contents = contents.replace('"', "")
    contents = contents.replace("{", "")
    contents = contents.replace("}", "")
with open("transcripts.txt", "w") as transcript_file:
    transcript_file.write(contents)