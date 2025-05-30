import os
import csv
import PyPDF2

def extract_text(file_path):
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError("File does not exist.")

    # Limit file size (5MB max)
    if os.path.getsize(file_path) > 5 * 1024 * 1024:
        raise ValueError("File size exceeds the 5MB limit.")
    
    try:
        if file_path.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read().strip()
        
        elif file_path.endswith(".pdf"):
            with open(file_path, "rb") as file:
                reader = PyPDF2.PdfReader(file)
                return "\n".join(page.extract_text().strip() for page in reader.pages if page.extract_text()).strip()
        
        elif file_path.endswith(".csv"):
            with open(file_path, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                return "\n".join(["\t".join(row) for row in reader]).strip()
        
        else:
            raise ValueError("Unsupported file type. Only .txt, .pdf, and .csv are allowed.")

    except Exception as e:
        with open("error.log", "a") as log_file:
            log_file.write(f"Error processing {file_path}: {e}\n")
        raise

# Usage Example
file_path = "example.pdf"  # Change to test different files

try:
    content = extract_text(file_path)
    print(content)
except Exception as e:
    print(f"Error: {e}")
