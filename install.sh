#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "python3 ${DIR}/main.py" > /usr/local/bin/weather
chmod +x /usr/local/bin/weather

echo "/usr/local/bin/weather" >> ~/.profile
