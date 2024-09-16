from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io

transfer_model = load_model('transfer_model.h5')  # Update with the correct path to your saved model

# Initialize the Flask app
app = Flask(__name__)


def preprocess_image(image):
    image = Image.open(io.BytesIO(image)).resize((256, 256)) 
    image = np.array(image) / 255.0 
    image = np.expand_dims(image, axis=0)  
    return image


@app.route('/predict_transfer', methods=['POST'])
def predict_transfer():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
   
    file = request.files['image'].read()
    
    
    image = preprocess_image(file)
    
   
    prediction = transfer_model.predict(image)
    predicted_class = np.argmax(prediction, axis=1)[0]
    
    
    class_names = ['Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']  # Replace with your actual class names
    
    
    return jsonify({'predicted_class': class_names[predicted_class]})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

