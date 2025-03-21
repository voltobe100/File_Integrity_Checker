import hashlib
import os
import json
import time

# Configuration
WATCHED_DIR = "./watched_files"  # Change this to the directory you want to monitor
HASH_FILE = "file_hashes.json"
SCAN_INTERVAL = 10  # Time interval in seconds

def calculate_hash(file_path):
    """Calculate SHA-256 hash of a file."""
    hasher = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(4096):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def scan_files():
    """Scan directory and return dictionary of file hashes."""
    file_hashes = {}
    for root, _, files in os.walk(WATCHED_DIR):
        for file in files:
            file_path = os.path.join(root, file)
            file_hashes[file_path] = calculate_hash(file_path)
    return file_hashes

def load_previous_hashes():
    """Load previous file hashes from JSON file."""
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_hashes(file_hashes):
    """Save current file hashes to JSON file."""
    with open(HASH_FILE, 'w') as f:
        json.dump(file_hashes, f, indent=4)

def check_integrity():
    """Compare current hashes with stored hashes to detect changes."""
    print("Scanning for file changes...")
    previous_hashes = load_previous_hashes()
    current_hashes = scan_files()
    
    for file, new_hash in current_hashes.items():
        old_hash = previous_hashes.get(file)
        if old_hash is None:
            print(f"[NEW] {file} added!")
        elif old_hash != new_hash:
            print(f"[MODIFIED] {file} has changed!")
    
    for file in previous_hashes:
        if file not in current_hashes:
            print(f"[DELETED] {file} has been removed!")
    
    save_hashes(current_hashes)

if __name__ == "__main__":
    print("Starting File Integrity Checker...")
    while True:
        check_integrity()
        time.sleep(SCAN_INTERVAL)
