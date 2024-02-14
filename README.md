# Security Surveillance System

## Overview
This project implements a security surveillance system using Python and OpenCV. It captures video frames from the default camera, detects motion, and sends email alerts with images when motion is detected. The system employs background subtraction and contour detection techniques to identify significant changes in the scene.

## Dependencies
The project relies on the following Python libraries:
- [OpenCV](https://opencv.org/) - for computer vision tasks
- [smtplib](https://docs.python.org/3/library/smtplib.html) - for sending email alerts
- [imghdr](https://docs.python.org/3/library/imghdr.html) - for determining the image type
- [threading](https://docs.python.org/3/library/threading.html) - for asynchronous execution of email sending

## Setup
To run the project, follow these steps:
1. Clone the repository: `git clone https://github.com/tur14cus/security-surveillance.git`
2. Install OpenCV using pip: `pip install opencv-python`
3. Ensure you have a Gmail account with less secure app access enabled. You can enable this feature in your Gmail settings.
4. Replace the placeholders in `mailing.py` with your email address and password.
5. Run the Python script: `python main.py`
6. Press 'q' to quit the application.

## Usage
The security surveillance system continuously monitors the area and detects any motion. When motion is detected, the system captures an image and sends an email alert with the image attachment to the specified recipient. Users can adjust parameters such as the threshold value and dilation iterations to fine-tune the motion detection sensitivity.

## Structure
The project consists of the following files:
- `main.py`: Contains the Python script for implementing the security surveillance system.
- `mailing.py`: Defines functions for sending email alerts with image attachments.
- `README.md`: This readme file providing an overview of the project.

## Contributions
Contributions are welcome. Feel free to fork the repository, make improvements, and submit pull requests.

## License
This project is licensed under the [MIT License](LICENSE).
