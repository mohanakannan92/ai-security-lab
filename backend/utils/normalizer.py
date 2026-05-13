import re

def normalize_input(text: str) -> str:
    text = text.lower()

    # Replace common obfuscations
    text = re.sub(r'1', 'i', text)
    text = re.sub(r'0', 'o', text)
    text = re.sub(r'@', 'a', text)

    # Remove special characters
    text = re.sub(r'[^a-z0-9\s]', ' ', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text