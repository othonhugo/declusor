# list running processes
( ps -aux | awk '{ printf "%s %s %s %s\n", $1, $2, $9, $11 }' | column -t ) 2> /dev/null | print_with_label 'Running Processes'

# list PCI buses and connected devices
( lspci ) 2> /dev/null | print_with_label 'PCI Buses & Devices'
