# AI-Rosetta-Transcription---Translation

This Python script is designed to automate the process of translating or transcribing audio files into different languages. This script uses the Whisper API to perform the translations and transcriptions.

**Prerequisites**

Python 3.7 or higher

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

**License**
  
This project is licensed under the terms of the MIT license. See LICENSE for more information.

**Author**
  
Built by Sabian Hibbs.
