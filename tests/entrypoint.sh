#!/usr/bin/env bash


export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python
. /usr/local/bin/virtualenvwrapper.sh


export PATH="${HOME}/.local/bin:$PATH"


while true
do
    for task_dir in /tests/tasks/*
    do
        task_name="$(basename "$task_dir")"

        if [ -d "$task_dir"/solution ]
        then
            if ! workon --no-cd "$task_name"
            then
                mkvirtualenv --python=python3 "$task_name"
            fi

            if [ -r "$task_dir"/solution/requirements.txt ]
            then
                pip3 install -r "$task_dir"/solution/requirements.txt
            fi
            print "Solution for task \"$task_name\": "
            python3 /tests/run_test.py "$task_dir" | true

            deactivate
        else
            echo "Task \"$task_name\" has no automatic solution!"
        fi
    done
done
