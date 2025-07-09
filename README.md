# 🔍 Python Port Scanner

A simple TCP port scanner written in Python. This project includes two scripts:

* `script.py`: a **sequential scanner**, simple but slower.
* `faster_script.py`: an **optimized parallel scanner**, using Python’s `ProcessPoolExecutor` for faster scanning.

Both scripts scan ports from **0 to 65535** and report the open ports on a given IP address.

---

## 🚀 Features

* Full TCP port scan (ports 0–65535)
* IP address validation
* Detailed console output for each connection attempt
* **Parallel scanning** (in `faster_script.py`) using multiprocessing for improved performance
* Graceful handling of user interruptions (`Ctrl+C`)
* No external dependencies (only Python standard library)

---

## 🛠️ Technologies Used

* Python 3
* Standard Libraries:

  * `socket`
  * `concurrent.futures`
  * `ipaddress`
  * `sys`, `time`

---

## ⚙️ Installation & Usage

### 1. Clone the repository

```bash
git clone https://github.com/your-username/port-scanner.git
cd port-scanner
```

### 2. Run the **basic scanner**

```bash
python3 script.py <IP_ADDRESS>
```

Example:

```bash
python3 script.py 192.168.1.1
```

---

### 3. Run the **faster parallel scanner**

```bash
python3 faster_script.py <IP_ADDRESS>
```

Example:

```bash
python3 faster_script.py 192.168.1.1
```

---

## 🔬 Example Output

```
Starting the script...
Connecting to port 80
Port 80 is available.
Initialization complete.
Available ports on 192.168.1.1: [80, 443, 8080]
Script finished running.
Total time taken: 8.32 seconds
```

---

## 📄 Script Comparison

| Script             | Speed  | Architecture                 | Use Case                           |
| ------------------ | ------ | ---------------------------- | ---------------------------------- |
| `script.py`        | Slower | Single-threaded (sequential) | Simple scanning, small port ranges |
| `faster_script.py` | Faster | Multi-process (parallel)     | Scanning large ranges efficiently  |

---

## ⚠️ Disclaimer

> Use this tool responsibly. Port scanning may be illegal or restricted without authorization. Only scan devices that you own or have explicit permission to test.

---

## 🔧 Possible Improvements

* Add UDP scan capability
* Use `asyncio` for non-blocking connections
* Replace CLI parsing with `argparse` for better usability
* Export results to JSON/CSV files
* Add DNS resolution (hostnames instead of just IP addresses)

---

## 📂 Project Structure

```
port-scanner/
├── script.py            # Simple single-threaded scanner
├── faster_script.py     # Parallelized scanner using multiprocessing
└── README.md            # Documentation
```

---
