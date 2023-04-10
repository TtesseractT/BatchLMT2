# BatchWhisper-Transcription-Translation (CPU & GPU Supported)

This Python script is designed to automate the process of translating or transcribing audio files into different languages. This script uses the Whisper API to perform the translations and transcriptions.

## Prerequisites

- Python 3.8 or higher
- System Environment Variables: OPENAI_API_KEY = Please add your API Key to the variables for "--type [1, 2]" to work.

## Installation

1. Clone this repository: `git clone https://github.com/TtesseractT/BatchWhisper-Transcription-Translation`
2. Run the following script in the command line: `python Setup-Rosetta.py`

## Usage

**Supported Input File Types:**

`3GP - Mobile Phone Video` : `AAC - Advanced Audio Codec` : `AC3 - Audio Codec 3` : `AIF, AIFF - Audio Interchange File Format` : `AMR - Adaptive Multi-Rate Audio Codec` : `APE - Monkey's Audio Format` : `ASF - Advanced Streaming Format` : `AVI - Audio Video Interleaved Format` : `CAF - Core Audio Format` : `DTS - Digital Theater Systems Audio` : `FLAC - Free Lossless Audio Codec` : `M4A, M4B - MPEG-4 Audio Layer` : `MIDI - Musical Instrument Digital Interface` : `MKV - Matroska Multimedia Container` : `MOV - Apple QuickTime Movie` : `MP4 - MPEG-4 Part 14 Container` : `MPEG - Moving Picture Experts Group Video` : `OGA, OGG - Ogg Vorbis Audio` : `RA - RealAudio` : `RM - RealMedia` : `WAV - Waveform Audio Format` : `WebM - Web Media Format` : `WMA - Windows Media Audio` : `WV - WavPack Audio Format` : `AVCHD - Advanced Video Codec High Definition` : `DV - Digital Video Format` : `FLV - Flash Video Format` : `M2TS, MTS - MPEG-2 Transport Stream` : `MJPEG - Motion JPEG Video Format` : `MPEG-1 - Moving Picture Experts Group Video` : `MPEG-2 - Moving Picture Experts Group Video` : `MPEG-4 - Moving Picture Experts Group Video` : `RMVB - RealMedia Variable Bitrate Format` : `SWF - Shockwave Flash Movie` : `VOB - DVD Video Object` : `WMV - Windows Media Video`

**Supported Languages:**

>Afrikaans,Albanian,Amharic,Arabic,Armenian,Assamese,Azerbaijani,Bashkir,Basque,Belarusian,Bengali,Bosnian,Breton,Bulgarian,Burmese,Castilian,Catalan,Chinese,Croatian,Czech,Danish,Dutch,English,Estonian,Faroese,Finnish,Flemish,French,Galician,Georgian,German,Greek,Gujarati,Haitian,Haitian,Creole,Hausa,Hawaiian,Hebrew,Hindi,Hungarian,Icelandic,Indonesian,Italian,Japanese,Javanese,Kannada,Kazakh,Khmer,Korean,Lao,Latin,Latvian,Letzeburgesch,Lingala,Lithuanian,Luxembourgish,Macedonian,Malagasy,Malay,Malayalam,Maltese,Maori,Marathi,Moldavian,Moldovan,Mongolian,Myanmar,Nepali,Norwegian,Nynorsk,Occitan,Panjabi,Pashto,Persian,Polish,Portuguese,Punjabi,Pushto,Romanian,Russian,Sanskrit,Serbian,Shona,Sindhi,Sinhala,Sinhalese,Slovak,Slovenian,Somali,Spanish,Sundanese,Swahili,Swedish,Tagalog,Tajik,Tamil,Tatar,Telugu,Thai,Tibetan,Turkish,Turkmen,Ukrainian,Urdu,Uzbek,Valencian,Vietnamese,Welsh,Yiddish,Yoruba

**Supported Output file type [3, 4, 5, 6]:**

`Text Format (txt)`

`Json Format (json)`

`WebVTT Format (vtt)`

`SubRip Subtitle Format (srt)`

`Tab Separated Values Format (tsv)`

**To use this script, follow these steps:**

1. Place your audio files in the `Input-Videos` directory.
2. Run the script using the following command: `python Run.py --type <process-type>`

Replace `<process-type>` with the type of process you want to run (1 to 6). The available process types are:

- `<process-type - [1]>` Text to Audio Segments
- `<process-type - [2]>` Text to Audio Segments with Translation
- `<process-type - [3]>` Audio Translation (CPU)
- `<process-type - [4]>` Audio Translation (GPU)
- `<process-type - [5]>` Audio Transcription (CPU)
- `<process-type - [6]>` Audio Transcription (GPU)

If you choose process types 3, 4, 5, or 6, you will be prompted to select a language and an output format.

The output files will be saved in the `Videos` directory.

## USAGES FOR WHISPER DEVELOPER BACKEND*

usage: whisper [-h] 

[--model {tiny.en,tiny,base.en,base,small.en,small,medium.en,medium,large-v1,large-v2,large}]

[--model_dir MODEL_DIR] 

[--device DEVICE] 

[--output_dir OUTPUT_DIR]

[--output_format {txt,vtt,srt,tsv,json,all}] 

[--verbose VERBOSE] 

[--task {transcribe,translate}]

[--temperature TEMPERATURE] 

[--best_of BEST_OF] 

[--beam_size BEAM_SIZE] 

[--patience PATIENCE]

[--length_penalty LENGTH_PENALTY] 

[--suppress_tokens SUPPRESS_TOKENS] 

[--initial_prompt INITIAL_PROMPT]

[--condition_on_previous_text CONDITION_ON_PREVIOUS_TEXT] 

[--fp16 FP16]

[--temperature_increment_on_fallback TEMPERATURE_INCREMENT_ON_FALLBACK]

[--compression_ratio_threshold COMPRESSION_RATIO_THRESHOLD] 

[--logprob_threshold LOGPROB_THRESHOLD]

[--no_speech_threshold NO_SPEECH_THRESHOLD] 

[--word_timestamps WORD_TIMESTAMPS]

[--prepend_punctuations PREPEND_PUNCTUATIONS] 

[--append_punctuations APPEND_PUNCTUATIONS]

[--threads THREADS]

## Input / Output structure

| EXPECTED INPUT - [ROOT DIR] |               | EXPECTED OUTPUT - [ROOT DIR] |                  |
|-----------------------------|---------------|------------------------------|------------------|
| Folder                      | File          | Folder                       | File             |
| Input-Videos                |               | Videos                       |                  |
|                             | Video 1       | Video -1                     |                  |
|                             | Video 2       |                              | Video 1 - File   |
|                             | Video 3       |                              | Transcription File|
|                             | Video 4       |                              | Audio Segment - File|
|                             | ...           | Video -2                     |                  |
|                             | Video [N]     |                              | Video 2 - File   |
|                             |               |                              | Transcription File|
|                             |               |                              | Audio Segment - File|


## License

This project is licensed under the terms of the MIT license. See `LICENSE` for more information.

## Author

Built by Sabian Hibbs.
