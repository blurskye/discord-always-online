#!/bin/bash

script_path=$(cd $(dirname ${BASH_SOURCE[0]}); pwd -P)
"$script_path"/.venv/bin/python "$script_path"/main.py



