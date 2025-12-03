#!/bin/bash

run_and_check() {
    local cmd="$*"

    echo "> $cmd"
    
    output=$($cmd 2>&1)
    status=$?

    if [ $status -ne 0 ]; then
        echo "status code: $status"
        echo "$output"
        echo
    fi

    return $status
}

# Install the package
run_and_check pip install -e .

# Run black
run_and_check black --check $(git ls-files '*.py')

# Run isort
run_and_check isort --check-only $(git ls-files '*.py')

# Run mypy
run_and_check mypy .

# Run pylint
run_and_check pylint $(git ls-files '*.py')

# Run tests
run_and_check python -m unittest discover tests