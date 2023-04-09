# BatchWhisper-Transcription-Translation [CPU & GPU Supported]

This Python script is designed to automate the process of translating or transcribing audio files into different languages. This script uses the Whisper API to perform the translations and transcriptions.

**Prerequisites**

Python 3.7 or higher

System Environment Variables: OPENAI_API_KEY = Please add your own API Key to the variables for "--type [1, 2]" to work.

**Installation**

Clone this repository: git clone https://github.com/TtesseractT/AI-Rosetta-Transcription-Translation

Run the following script in command line:

python Setup-Rosetta.py

**Usage**

Supported Languages:

**Afrikaans,Albanian,Amharic,Arabic,Armenian,Assamese,Azerbaijani,Bashkir,Basque,Belarusian,Bengali,Bosnian,Breton,Bulgarian,Burmese,Castilian,Catalan,Chinese,Croatian,Czech,Danish,Dutch,English,Estonian,Faroese,Finnish,Flemish,French,Galician,Georgian,German,Greek,Gujarati,Haitian,Haitian,Creole,Hausa,Hawaiian,Hebrew,Hindi,Hungarian,Icelandic,Indonesian,Italian,Japanese,Javanese,Kannada,Kazakh,Khmer,Korean,Lao,Latin,Latvian,Letzeburgesch,Lingala,Lithuanian,Luxembourgish,Macedonian,Malagasy,Malay,Malayalam,Maltese,Maori,Marathi,Moldavian,Moldovan,Mongolian,Myanmar,Nepali,Norwegian,Nynorsk,Occitan,Panjabi,Pashto,Persian,Polish,Portuguese,Punjabi,Pushto,Romanian,Russian,Sanskrit,Serbian,Shona,Sindhi,Sinhala,Sinhalese,Slovak,Slovenian,Somali,Spanish,Sundanese,Swahili,Swedish,Tagalog,Tajik,Tamil,Tatar,Telugu,Thai,Tibetan,Turkish,Turkmen,Ukrainian,Urdu,Uzbek,Valencian,Vietnamese,Welsh,Yiddish,Yoruba**

To use this script, follow these steps:

1.  Place your audio files in the Input-Videos directory.
2.  Run the script using the following command:

CMD Line:

python Run.py --type <process-type>

Replace <process-type> with the type of process you want to run (1 to 6). The available process types are:

<process-type - [1]> Text to Audio Segments
  
<process-type - [2]> Text to Audio Segments with Translation
  
<process-type - [3]> Audio Translation (CPU)
  
<process-type - [4]> Audio Translation (GPU)
  
<process-type - [5]> Audio Transcription (CPU)
  
<process-type - [6]> Audio Transcription (GPU)

If you choose process types 3, 4, 5, or 6, you will be prompted to select a language and an output format.

The output files will be saved in the Videos directory.

**USAGES FOR WHISPER DEVELOPER BACKEND**

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

**License**
  
This project is licensed under the terms of the MIT license. See LICENSE for more information.

**Author**
  
Built by Sabian Hibbs.
