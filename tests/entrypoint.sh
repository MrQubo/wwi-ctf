#!/usr/bin/env bash


export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python
. /usr/local/bin/virtualenvwrapper.sh


export PATH="${HOME}/.local/bin:$PATH"


sleep 10

while true
do
    for task_dir in /tests/tasks/*
    do
        task_name="$(basename "$task_dir")"

        if [ -d "$task_dir"/solution ]
        then
            if [ -r "$task_dir"/solution/requirements.txt ]
            then
                if ! workon --no-cd "$task_name" 2>/dev/null
                then
                    mkvirtualenv --python=python3 "$task_name" >/dev/null 2>&1
                fi
                pip3 install -r "$task_dir"/solution/requirements.txt >/dev/null
            fi
            python3 /tests/run_test.py "$task_name" "$task_dir"

            deactivate
        else
            echo "Solution for task \"$task_name\": no automatic solution!"
        fi
    done

    sleep 3600
done
