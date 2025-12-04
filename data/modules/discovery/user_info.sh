# show current UID and GID
( id ) | print_with_label "Current User/Group"

# show current user's sudo nopasswd permissions
( sudo -n -l | grep 'NOPASSWD' | awk '{$1=$1;print}' ) 2> /dev/null | print_with_label "Sudo NOPASSWD Permission"

# show last logged in users
( lastlog | grep -vE '\*\*.*\*\*' | cut -d $'\n' -f 2- ) | tail -n +2 | column -t | 2> /dev/null  print_with_label "Last Logged In Users"

# show all users logged into the current system
( w -hs ) 2> /dev/null | print_with_label "Users Logged In"

# list all user accounts
( for uid in $(awk -F ':' '{ print $1 }' /etc/passwd ); do id "$uid"; done ) 2> /dev/null | column -t | print_with_label "Current Users"

# list all super user accounts
( for uid in $(grep -Po '^sudo.+:\K.*$' /etc/group); do id "$uid"; done ) 2> /dev/null | print_with_label "Super Users"

# list all adm accounts
( for uid in $(grep -Po '^adm.+:\K.*$' /etc/group ); do id "$uid"; done ) 2> /dev/null | print_with_label "ADM Users"
