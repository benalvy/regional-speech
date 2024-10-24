import gradio as gr
from gtts import gTTS
import os

def text_to_speech(text):
    # Create a gTTS object
    tts = gTTS(text=text, lang='hi')
    # Save the audio file
    audio_file = "output.mp3"
    tts.save(audio_file)
    return audio_file

# Create a Gradio interface
interface = gr.Interface(
    fn=text_to_speech,  # Function to call
    inputs="text",  # Input type
    outputs="audio",  # Output type
    title="Hindi Text to Speech",
    description="Enter Hindi text to convert it to speech.",
)

# Launch the Gradio app
interface.launch()
