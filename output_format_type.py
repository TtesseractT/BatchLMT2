#-------------------------------------------------------------------#
# BatchWhisper-Transcription-Translation [LOCAL & API]              #
#-------------------------------------------------------------------#
# Author: SABIAN HIBBS                                              #
# License: MIT                                                      #
# Version: 3.4                                                      #
#-------------------------------------------------------------------#

# output_format_type.py

output_format_type = {
    
    "TEXT": "txt",
    "JSON": "json", 
    "VTT": "vtt",
    "SRT": "srt",
    "TSV": "tsv",
    "ALL": "all",
    
}

# Generate a comma-separated string of available languages
available_op_format = ','.join(output_format_type.keys())
