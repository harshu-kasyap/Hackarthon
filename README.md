# Hackarthon
Automatic number plate recognition
markdown
Copy code
# License Plate Detection using OpenCV and Firebase Cloud Storage

License Plate Detection is a Python script that uses OpenCV to detect license plates in a live video stream or recorded video. Detected license plate images are then uploaded to Firebase Cloud Storage.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Firebase Setup](#firebase-setup)
- [License Plate Detection](#license-plate-detection)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before using this project, make sure you have the following prerequisites installed:

- Python (version 3.6 or later)
- OpenCV (`cv2` package)
- Firebase Admin SDK
- Firebase service account credentials (`service_account.json`)

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
Install the required Python packages using pip:

bash
Copy code
pip install opencv-python-headless firebase-admin
Place your Firebase service account credentials (service_account.json) in the project directory.

Usage
To use this script:

Open a terminal and navigate to the project directory.

Run the script:

bash
Copy code
python license_plate_detection.py
Press 'q' to exit the video stream.

Firebase Setup
Make sure to set up a Firebase project and create a Cloud Storage bucket. Update the script with your Firebase project credentials and bucket name.

License Plate Detection
The script uses the Haar Cascade Classifier to detect license plates in the video stream. Detected plates are saved to Firebase Cloud Storage.

Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

Fork the repository.

Create a new branch for your feature or bug fix:

bash
Copy code
git checkout -b feature-name
Make your changes and commit them:

bash
Copy code
git commit -m "Description of your changes"
Push your changes to your fork:

bash
Copy code
git push origin feature-name
Create a pull request on the main repository's GitHub page.
