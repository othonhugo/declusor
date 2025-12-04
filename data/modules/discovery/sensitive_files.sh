# list home directories
( find /home -maxdepth 1 -printf "$_FIND_PRINTF_SEPARATOR_PATTERN" ) 2> /dev/null | column -t -s ';' 2> /dev/null | print_with_label "Home Directories"

# list user's crontab
( crontab -l ) 2> /dev/null | column -t -s ';' 2> /dev/null | print_with_label "User's Crontab"

# search for key files
( find /home -type f \( -name authorized_keys -o -name '*id_dsa*' -o -name '*id_ecdsa*' -o -name '*id_ed25519*' -o -name '*id_rsa*' -o -name '*.key' -o -name '*.pub' \) -printf "$_FIND_PRINTF_SEPARATOR_PATTERN" ) 2> /dev/null | column -t -s ';' 2> /dev/null | print_with_label "Key Files"

# list sensitive /etc directories
( find /etc \( -type f -o -type d \) \( -name 'init*' -o -name 'cron*' -o -name 'anacrontab' -o -name 'sudoers' -o -name 'exports' \ \) -printf "$_FIND_PRINTF_SEPARATOR_PATTERN" ) 2> /dev/null | column -t -s ';' 2> /dev/null | print_with_label "Config Directories"

# list cron files
( find /var/spool/cron /etc/cron* -type f -printf "$_FIND_PRINTF_SEPARATOR_PATTERN" ) 2> /dev/null | column -t -s ';' 2> /dev/null | print_with_label "Cron Files"
