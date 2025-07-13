import json

def load_logs(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def extract_errors(logs):
    return [log["message"] for log in logs if log["level"] == "ERROR"]

if __name__ == "__main__":
    logs = load_logs("logs/sample_mq_logs.json")
    errors = extract_errors(logs)
    for e in errors:
        print(e)

