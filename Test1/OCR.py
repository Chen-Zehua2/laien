import easyocr
import re
import os
# Initialize EasyOCR reader (supports multiple languages, 'en' for English)
reader = easyocr.Reader(['en'])

# Define a mapping for special characters to digits
char_to_digit = {
    '/': '1',  # Example: mapping / to 1
    '|': '1',  # Example: mapping | to 1
    # You can add more mappings based on common misread symbols
}

def clean_text(text):
    # Replace unwanted characters with the closest digit
    for char, digit in char_to_digit.items():
        text = text.replace(char, digit)
    return text

# Read the image with EasyOCR
folder_path = 'output/'  # Replace with your folder path

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is an image (you can expand this list as needed)
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        image_path = os.path.join(folder_path, filename)
        
        # Read the image with EasyOCR
        result = reader.readtext(image_path)

        print(result)
        # Extract phone numbers with exactly 8 digits
        phone_numbers = []

        for text in result:
            cleaned_text = clean_text(text[1])
            
            # Check if the cleaned text contains exactly 8 digits
            if re.match(r'^\d{8}$', cleaned_text):
                phone_numbers.append(cleaned_text)

        # Print the found phone numbers
        print("Extracted phone numbers with 8 digits:", phone_numbers)
