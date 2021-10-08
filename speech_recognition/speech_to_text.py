
from google.cloud import speech
import os
import io

# Create google client
client = speech.SpeechClient()

# Load audio file to memory
file_name = os.path.join(os.path.dirname(__file__),"test.wav")

#???
with io.open(file_name, "rb") as audio_file:
    content = audio_file.read()
    audio = speech.RecognitionAudio(content=content)

config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    audio_channel_count=2,
    language_code="en-US",
)

# Send the request to google to transcribe the audio
response = client.recognize(request={"config": config, "audio": audio})

# Read the response
for result in response.results:
    print("Transcript: {}".format(result.alternatives[0].transcript))


# AWS api