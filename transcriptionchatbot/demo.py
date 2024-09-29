import whisper
import warnings

# Suppress the specific FP16 warning
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead", category=UserWarning)

# Load the whisper model
model = whisper.load_model("base")

# Transcribe the audio file
result = model.transcribe("WhatsApp Audio 2024-09-29 at 02.01.42_d76c9255.mp3")

# Write the transcription result to a file using UTF-8 encoding
with open("transcription.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])
    
    # Specify the path to your text file
file_path = 'transcription.txt'  # Replace with your actual file path

try:
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read the contents of the file
        content = file.read()
        # Print the contents to the terminal
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
    
    
    
# DESCRIPTION
#     WE HAVE CREATED VOICE TO TEXT CONVERTER WHICH IS USEFULL WHICH ANOTHER STATE PEOPLE CAN 
#     SEE THE CAPTION IN THERE LAGUAGE TO UNDERSTAND WHAT IS HAPPNING !!

