# 🔍 File Integrity Checker

A Python-based **File Integrity Checker** that monitors changes in system files using **SHA-256 hashing**. Detects file modifications, additions, and deletions.

## 🚀 Features

✅ **Monitors files** for changes in a specified directory  
✅ **Detects** modified, added, and deleted files  
✅ Uses **SHA-256 hashing** for integrity verification  
✅ **Cross-platform support** (Linux & Windows)  
✅ **Automated periodic scanning**

## 🛠️ Installation

Ensure you have **Python 3.x** installed.  
Clone the repository and navigate into it:

```bash
git clone https://github.com/yourusername/file-integrity-checker.git
cd file-integrity-checker
```

## 📌 Usage

Run the script with administrative privileges:

```bash
python File_Integrity_Checker.py
```

### Customize Directory to Watch

Modify the `WATCHED_DIR` variable in the script to monitor a specific folder:

```python
WATCHED_DIR = "C:/Users/YourName/Documents"  # Windows
WATCHED_DIR = "/home/user/important_files"  # Linux
```

### Adjust Scan Interval

Change `SCAN_INTERVAL` in seconds for how often files are checked:

```python
SCAN_INTERVAL = 30  # Checks every 30 seconds
```

## ⚠️ Requirements

- **Python 3.x**
- **Admin/root privileges** for full access

## 📝 License

This project is licensed under the **MIT License**.
