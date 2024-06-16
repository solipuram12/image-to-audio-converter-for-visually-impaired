import cv2
import pytesseract
from gtts import gTTS
import os

# Path to the Tesseract executable
# For Windows, you might need to specify the path if it's not added to your system's PATH
# Example: pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Uncomment and modify the line below if needed:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def image_to_text(image_path):
    # Load the image from the specified path
    image = cv2.imread(image_path)
    
    # Convert the image to gray scale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Perform OCR on the image
    text = pytesseract.image_to_string(gray_image)
    
    return text

def text_to_audio(text, audio_file_path):
    # Convert the text to speech
    tts = gTTS(text=text, lang='en')
    
    # Save the speech to an audio file
    tts.save(audio_file_path)

def image_to_audio(image_path, audio_file_path):
    # Convert image to text
    text = image_to_text(image_path)
    
    # Convert text to audio
    text_to_audio(text, audio_file_path)

if __name__ == "__main__":
    # Specify the paths for the input image and output audio file
    image_path = 'path_to_your_image.jpg'
    audio_file_path = 'output_audio.mp3'
    
    # Convert image to audio
    image_to_audio(image_path, audio_file_path)
    
    print(f"Audio saved to {audio_file_path}")
