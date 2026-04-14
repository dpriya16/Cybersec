# Cybersec - Basic Cybersecurity Working Project

This repository contains a **beginner-friendly cybersecurity toolkit** built with Python.
It is designed for learning and local lab practice.

## Features

1. **Password Strength Audit**
   - Checks password for:
     - length (12+ chars)
     - lowercase
     - uppercase
     - numbers
     - symbols
   - Returns a score, rating, and improvement recommendations.

2. **File Integrity Monitoring**
   - Calculates file hashes (`sha256`, `sha1`, `md5`).
   - Verifies whether a file matches an expected hash.

3. **Local Port Scanner**
   - Scans a host and port range for open TCP ports.
   - Intended for local/authorized testing only.

## Project Structure

```text
.
├── main.py
├── cybersec_toolkit/
│   ├── __init__.py
│   ├── password_audit.py
│   ├── integrity_monitor.py
│   └── port_scanner.py
└── tests/
    ├── test_password_audit.py
    ├── test_integrity_monitor.py
    └── test_port_scanner.py
```

## Requirements

- Python 3.10+

Install test dependency:

```bash
python3 -m pip install -r requirements.txt
```

## Usage

Run commands from the repository root:

### 1) Password audit

```bash
python3 main.py password-audit "MyWeakPass"
```

Example output:

```json
{
  "score": 2,
  "max_score": 5,
  "rating": "weak",
  "checks": {
    "length_12_plus": false,
    "has_lowercase": true,
    "has_uppercase": true,
    "has_digit": false,
    "has_symbol": false
  },
  "recommendations": [
    "Use at least 12 characters.",
    "Add at least one number.",
    "Add at least one symbol, e.g. !@#$%."
  ]
}
```

### 2) Hash a file

```bash
python3 main.py hash-file README.md --algorithm sha256
```

### 3) Verify file hash

```bash
python3 main.py verify-hash README.md "<expected_hash>" --algorithm sha256
```

If the hash matches, output is:

```json
{"valid": true}
```

### 4) Port scan (local/authorized only)

```bash
python3 main.py port-scan 127.0.0.1 20 1024 --timeout 0.2
```

## Run Tests

```bash
python3 -m pytest -q
```

## Important Security Note

Use this toolkit **only on systems you own or have explicit permission to test**.
Unauthorized scanning or security testing may violate laws and policies.
