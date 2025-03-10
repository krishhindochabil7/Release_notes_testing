def extract_text(file_path):
    if not file_path.endswith(".txt"):
        raise ValueError("Only .txt files are supported.")
    
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

# Usage Example
file_path = "example.txt"
try:
    content = extract_text(file_path)
    print(content)
except ValueError as e:
    print(f"Error: {e}")
