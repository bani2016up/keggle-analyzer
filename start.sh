#!/bin/bash

# Function to be executed on script exit
cleanup() {
    echo "Performing cleanup..."
    python scripts/delete_kaggle_json.py
}

# Set trap to call cleanup function on script exit
trap cleanup EXIT

# Main script execution
set -e  # Exit immediately if a command exits with a non-zero status

echo "RUNNING poetry lock"

cd backend
poetry lock
cd ../
cd kaggle-storage-manager
poetry lock
cd ../

echo "RUNNING creating kaggle.json file"
python scripts/generate_kaggle_json.py

echo "RUNNING docker compose"
docker compose up -d --no-deps --build

# The cleanup function will be called automatically when the script exits
