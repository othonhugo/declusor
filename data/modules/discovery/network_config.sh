# list network addresses
( ip addr | grep -e 'link' -e 'inet' -e 'inet6' -e '[0-9]:' | cut -d ' ' -f 1,2,5,6 ) 2> /dev/null | print_with_label 'Network Addresses'

# list DNS nameservers
( grep "^[^#;]" /etc/resolv.conf | grep nameserver ) 2> /dev/null | print_with_label 'DNS Nameservers'

# list ARP table
( arp -a || ip neighbour ) 2> /dev/null | print_with_label 'ARP Table'

# display listening services
( netstat -tunlp || ss -tunpl ) 2> /dev/null | column -t | print_with_label 'Listening Services'
