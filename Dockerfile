#-------------------------------------------------------------------#
# BatchWhisper-Transcription-Translation [LOCAL & API]              #
#-------------------------------------------------------------------#
# Author: SABIAN HIBBS                                              #
# License: MIT                                                      #
# Version: 3.34                                                     #
#-------------------------------------------------------------------#

# Use an official Python runtime as a parent image
FROM python:3.9-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN mkdir Input-Videos

# Install the whisper-asr and ffmpeg dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends git ffmpeg && \
    pip install -U openai-whisper && \
    pip install git+https://github.com/openai/whisper.git && \
    pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git && \
    pip install ffmpeg && \
    pip install openai && \
    pip install setuptools-rust && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Define environment variable
ENV OPENAI_API_KEY YourAPIKeyHere

# Run app.py when the container launches
CMD ["python", "Text_AudioSegments.py"]
