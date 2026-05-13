import csv

def load_logs(file_path):
    logs = []
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            logs.append(row)
    return logs