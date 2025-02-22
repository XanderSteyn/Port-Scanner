---

# 🕵️‍♂️ Port Scanner

A Python-based tool that performs a port scan on a target IP address to check which ports are open. It uses threading to speed up the scanning process.

⚠️ **Use responsibly** – Only run this tool on systems you own or have explicit permission to scan.

## ⚙️ Features
- Scans ports from 1 to 9999 on a target IP address.
- Uses Python's `socket` and `threading` libraries for efficient scanning.
- Displays open ports in real-time.

## 🚀 Installation

### Prerequisites

To run this project, you need Python 3.x installed. No additional dependencies are required.

### 🛠️ Setup

1. Clone the repository to your local machine :

   ```bash
   git clone https://github.com/XanderSteyn/Port-Scanner.git
   cd Port-Scanner
   ```

2. Run the script :

   ```bash
   python PortScanner.py
   ```

### 📦 Dependencies

- **No additional packages required.** This script uses Python's built-in libraries : `socket` and `threading`.

## 🛑 How It Works

1. The script prompts for a target IP address.
2. It scans ports from 1 to 9999 on the target IP address.
3. For each port, a new thread is created to attempt a connection to that port. If the port is open, it prints that the port is open; otherwise, it ignores the closed ports.

## 📝 Usage

1. Run the script :
   ```bash
   python PortScanner.py
   ```

2. Enter the target IP address when prompted :
   ```text
   IP: 1.1.1.1
   ```

3. The script will then scan ports from 1 to 9999 and print out the open ports.

## ⚙️ Configuration

- **Timeout** : The script sets a timeout of 5 seconds for the target connection and 0.5 seconds for each port connection.
- **Port Range** : The script scans ports from 1 to 9999 by default. You can modify the range in the loop if needed.

---
