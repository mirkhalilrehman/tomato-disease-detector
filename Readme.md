# Tomato Disease Detector

## Project Overview

**Tomato Disease Detector** is a machine learning-based application designed to identify various diseases affecting tomato leaves. By using deep learning models, this project aims to assist farmers and gardeners in detecting diseases early, improving crop health, and preventing yield loss.

## Features

- **Multi-Disease Detection**: Accurately detects 10 different classes of tomato leaf conditions, including bacterial spots, early blight, and healthy leaves.
- **Deep Learning Models**: Utilizes Convolutional Neural Networks (CNN) and transfer learning techniques for robust disease classification.
- **User-Friendly API**: Provides an easy-to-use Flask API for predicting disease from uploaded images.
- **Scalable and Adaptable**: Built with TensorFlow, allowing for further customization and scalability.

## Technologies Used

- **Python**: Primary language for development.
- **TensorFlow/Keras**: For building and training deep learning models.
- **Flask**: Backend framework used to create the API.
- **NumPy**: For numerical operations.
- **PIL (Pillow)**: For image preprocessing.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- Git
- Required Python packages (listed in `requirements.txt`)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/mirkhalilrehman/tomato-disease-detector.git
Navigate to the Project Directory

bash
Copy code
cd tomato-disease-detector
Install Dependencies

bash
Copy code
pip install -r requirements.txt
Model Training
Prepare the Dataset: Ensure your dataset is structured and placed in the appropriate directories as expected by the model training script.

Run the Training Script:

bash
Copy code
python train.py
Transfer Learning: You can also fine-tune the model using MobileNetV2 for better performance by running:

bash
Copy code
python transfer_learning.py
Running the Flask API
Start the API:

bash
Copy code
python app.py
Make Predictions: Use a tool like Postman or cURL to send a POST request to http://localhost:5000/predict_transfer with an image file.

API Endpoints
/predict_transfer: Accepts a POST request with an image and returns the predicted disease class.
Contributing
We welcome contributions! If you have ideas, features, or improvements, feel free to fork the repository, make changes, and submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Thanks to the creators of open-source datasets and pre-trained models.
Special appreciation to those who have contributed to improving image classification technologies.