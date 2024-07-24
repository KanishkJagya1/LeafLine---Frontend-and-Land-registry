from flask import Flask, request, jsonify
from PIL import Image
from io import BytesIO
import torch
import torchvision.transforms as transforms
from torchvision import models
import numpy as np

# Define the Flask app
app = Flask(__name__)

# Load a pre-trained segmentation model
model = models.segmentation.deeplabv3_resnet101(pretrained=True)
model.eval()

# Define image processing function
def process_image(file):
    image = Image.open(BytesIO(file.read()))
    transform = transforms.Compose([
        transforms.Resize((256, 256)),  # Adjust size as per model requirements
        transforms.ToTensor(),
    ])
    return transform(image).unsqueeze(0)  # Add batch dimension

# Define segmentation conversion function
def convert_segmentation_to_json(segmentation):
    # Assuming the segmentation output is a tensor of shape [1, C, H, W]
    segmentation_np = segmentation.squeeze().cpu().detach().numpy()
    segmentation_list = segmentation_np.tolist()
    return {'segmentation': segmentation_list}

# Define the segment endpoint
@app.route('/segment', methods=['POST'])
def segment_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    try:
        # Process the image
        image = process_image(file)
        with torch.no_grad():
            segmentation = model(image)['out']

        # Convert the segmentation output to JSON
        result = convert_segmentation_to_json(segmentation)
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
