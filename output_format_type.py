#######################################################
# Rosetta v1 Python Script - Created on 08/04/2023    #
#######################################################
# Built by Sabian Hibbs                               #
#                                                     #
#######################################################

# output_format_type.py

output_format_type = {
    
    "TEXT": "txt",
    "JSON": "json", 
    "VTT": "vtt",
    "SRT": "srt",
    "TSV": "tsv",
    "All": "all",
    
}

# Generate a comma-separated string of available languages
available_op_format = ','.join(output_format_type.keys())