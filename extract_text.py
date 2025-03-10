import PyPDF2

def extract_text(file_path):
    if file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    elif file_path.endswith(".pdf"):
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            return "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
    else:
        raise ValueError("Unsupported file type. Only .txt and .pdf are allowed.")

# Usage Example
file_path = "example.pdf"
try:
    content = extract_text(file_path)
    print(content)
except ValueError as e:
    print(f"Error: {e}")
