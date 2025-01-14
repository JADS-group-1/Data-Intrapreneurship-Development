#!/bin/bash

# Define the base directory and shared virtual environment
BASE_DIR="."
VENV_NAME="venv"
REQUIREMENTS_FILE="requirements.txt"

# Define the paths to your front-end and back-end applications
FRONTEND_DIR="$BASE_DIR/frontend"
BACKEND_DIR="$BASE_DIR/backend"

# Commands to run the applications
FRONTEND_COMMAND="python3 app.py" # Adjust to your front-end script
BACKEND_COMMAND="python3 -m web_app.backend.app"   # Adjust to your back-end script

# Setup and activate the shared virtual environment
echo "Setting up shared virtual environment..."
cd "$BASE_DIR" || { echo "Failed to navigate to $BASE_DIR"; exit 1; }

if [ ! -d "$VENV_NAME" ]; then
    python3 -m venv "$VENV_NAME"
    echo "Virtual environment created: $VENV_NAME"
fi

source "$VENV_NAME/bin/activate"

# Install requirements
if [ -f "$REQUIREMENTS_FILE" ]; then
    echo "Installing dependencies from $REQUIREMENTS_FILE..."
    pip install --upgrade pip
    pip install -r "$REQUIREMENTS_FILE"
else
    echo "Requirements file not found!"
    deactivate
    exit 1
fi

# Run the front-end application
echo "Starting Front-end Application..."
cd "$FRONTEND_DIR" || { echo "Failed to navigate to $FRONTEND_DIR"; exit 1; }
$FRONTEND_COMMAND &
FRONTEND_PID=$!

cd ..
cd ..
# Run the back-end application
echo "Starting Back-end Application..."
#cd "$BACKEND_DIR" || { echo "Failed to navigate to $BACKEND_DIR"; exit 1; }
$BACKEND_COMMAND &
BACKEND_PID=$!

# Wait for user input to terminate the script
echo "Both applications are running. Press [CTRL+C] to stop."
trap "echo 'Stopping applications...'; kill $FRONTEND_PID $BACKEND_PID; deactivate; exit" SIGINT SIGTERM
wait $FRONTEND_PID $BACKEND_PID
