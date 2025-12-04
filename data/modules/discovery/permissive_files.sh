# list writable files 
( find / -writable ! -user $(whoami) -type f ! -path '/proc/*' ! -path '/sys/*' -printf "$_FIND_PRINTF_SEPARATOR_PATTERN" ) 2> /dev/null | column -t -s ';' 2> /dev/null | print_with_label "Writable Files"

# list SUID files
( find / -perm -4000 -type f -printf "$_FIND_PRINTF_SEPARATOR_PATTERN" ) 2> /dev/null | column -t -s ';' 2> /dev/null | print_with_label "SUID Files"

# list SUID-root files in /usr/bin and /usr/lib
( find /usr/bin /usr/lib -perm /4000 -user root -printf "$_FIND_PRINTF_SEPARATOR_PATTERN" ) 2> /dev/null | column -t -s ';' 2> /dev/null | print_with_label "SUID-root bins/libs"

# list SGID-root files in /usr/bin and /usr/lib
( find /usr/bin /usr/lib -perm /2000 -group root -printf "$_FIND_PRINTF_SEPARATOR_PATTERN" ) 2> /dev/null | column -t -s ';' 2> /dev/null | print_with_label "SGID-root bins/libs"
