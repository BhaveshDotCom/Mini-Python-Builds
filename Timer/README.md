# Timer

A simple Python countdown timer that displays time in DD:HH:MM:SS format.

## ⏱️ How it works

The script takes a time value in seconds and counts down to zero, displaying the remaining time in days, hours, minutes, and seconds format (DD:HH:MM:SS).

## 🚀 Usage

Run the script with Python:

### macOS / Linux
```bash
python3 timer.py
```

### Windows
```bash
python timer.py
```

The timer will start counting down from 172800 seconds (2 days) as set in the code.

To change the duration, modify the value in the `timer(172800)` function call at the bottom of the script.

## 📝 Example

When run with the default 2-day timer, you'll see output like:
```
02:00:00:00
01:23:45:12
01:23:45:11
...
00:00:00:02
00:00:00:01
00:00:00:00
```

## 🔧 Requirements

- Python 3.x
- Standard library module: `time`