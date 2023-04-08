# AI-Rosetta-Transcription---Translation

This Python script is designed to automate the process of translating or transcribing audio files into different languages. This script uses the Whisper API to perform the translations and transcriptions.

**Prerequisites**

Python 3.7 or higher

ffmpeg

**Installation**

Clone this repository: git clone https://github.com/TtesseractT/AI-Rosetta-Transcription-Translation

**Usage**

To use this script, follow these steps:

1.  Place your audio files in the Input-Videos directory.
2.  Run the script using the following command:

CMD Line:

python rosetta.py --type <process-type>

Replace <process-type> with the type of process you want to run (1 to 6). The available process types are:

<process-type - [1]> Text to Audio Segments
  
<process-type - [2]> Text to Audio Segments with Translation
  
<process-type - [3]> Audio Translation (CPU)
  
<process-type - [4]> Audio Translation (GPU)
  
<process-type - [5]> Audio Transcription (CPU)
  
<process-type - [6]> Audio Transcription (GPU)

If you choose process types 3, 4, 5, or 6, you will be prompted to select a language and an output format.

The output files will be saved in the Videos directory.

**License**
  
This project is licensed under the terms of the MIT license. See LICENSE for more information.

**Author**
  
Built by Sabian Hibbs.
