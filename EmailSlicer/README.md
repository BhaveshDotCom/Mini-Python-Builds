# Email Slicer

A simple Python script that extracts the username and domain from an email address.

## How it works

The script prompts the user to enter an email address, then:
1. Finds the position of the "@" symbol
2. Extracts the username (everything before "@")
3. Extracts the domain (everything after "@")
4. Displays both parts

## 🚀 Usage

Run the script with Python:

### macOS / Linux
```bash
python3 email_slicer.py
```

### Windows
```bash
python email_slicer.py
```

Then enter an email address when prompted.

## Example

```
Enter your email...   user@example.com
--------------------
Username:  user
Domain:  example.com
--------------------
```

## Requirements

- Python 3.x