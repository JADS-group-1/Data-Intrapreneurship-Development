# Project Summary

## Overview
This project is a web application designed for Kleurrijk Wonen, part of the Data Intrapreneurship in Action course, focusing on model development, dataset management, and web-app development. The project is structured into several key directories, each serving a specific purpose.

The goal is the creation of a computer vision model used for detecting doors and windows. Nonetheless, the obtained model is then integrated in a web-app, so that the used could use it without needing technical knowledge.  

## Directory Structure
- **documentation/**: Contains project documentation.
- **model_development/**: 
  - **code/**: Includes scripts for converting datasets and creating/testing models.
    - **convert_COCO_to_YOLO/**: Scripts for converting COCO dataset format to YOLO format.
    - **model_creation_and_testing/**: Scripts and notebooks for model creation and testing.
      - **MVP_development.ipynb**: The notebooks for the Minimum Viable Product (MVP) model, presenting the best methodology used with the best results.
      - **Regression_test.ipynb**: The notebook where we use the previously obtained model and translate the detection task to a regression task, calculating metrics such as Mean Average Error for doors and windows detection. 
  - **dataset/**: Contains the link to the dataset which is in the Google Drive, since the size of it is considerably large.
  - **experiments_and_tests/**: Directory for storing experimental and test results of different images, that may not be part in the test dataset, used for demostration purposes.
  - **extra/**: Additional files such as reports and research documents.
  - **papers/**: Research papers related to the project.
- **web_app/**: The web application directory, developed in Flask. To run the web app, travel with your terminal to this directory and run `bash start.sh` script.
  - **backend/**: Backend server code.
    - **model/**: Directory where the model should be placed.
    - **predictor.py**: Script for making predictions using the model.
  - **frontend/**: Frontend application code.
    - **templates/**: HTML templates for the web application.
  - **requirements.txt**: List of dependencies for the project.
  - **start.sh**: Script to start the web application.

## Important Notes
- The backend assumes the model is called `finaL_yolov8_freeze_10_14_epochs.pt` and should be placed in the `./backend/model/` directory. This can be changed in the `./backend/predictor.py` file.
- The project uses the Ultralytics YOLO framework for object detection, segmentation, and other tasks.

## Key Files
- **web_app/backend/predictor.py**: Script for loading and using the model for predictions.
- **web_app/frontend/templates/result_page.html**: Template for displaying results on the web application.

## Dependencies
The project dependencies are listed in the `requirements.txt` file and can be installed using pip.

## Running the Project
To run the project, use the `start.sh` script located in the `web_app` directory.