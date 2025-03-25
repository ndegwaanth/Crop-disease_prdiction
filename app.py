from flask import Flask, render_template, request, flash
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import io
from forms import ImageSubmission
from labels import class_labels
import secrets


app = Flask(__name__)
key = secrets.token_hex(16)
app.config["SECRET_KEY"] = key

# Load the crop disease model
# model = load_model("crop_disease_cnn_model.h5", compile=False)
model = load_model("crop_disease_cnn_model.h5", compile=False)

@app.route("/upload", methods=["GET", "POST"])
def upload_image():
    form = ImageSubmission()
    predicted_class = None  # Initialize variable before the if statement

    if form.validate_on_submit():
        file = form.image.data

        # Read image file as a PIL Image
        img = image.load_img(io.BytesIO(file.read()), target_size=(224, 224))

        # Normalize image
        img_array = image.img_to_array(img) / 255.0

        # Reshape for model
        img_array = np.expand_dims(img_array, axis=0)

        # Make prediction
        prediction = model.predict(img_array)
        predicted_class = class_labels[np.argmax(prediction)]  # Get class label

        flash(f"Prediction: {predicted_class}", "success")

    return render_template("index.html", form=form, prediction=predicted_class)

    


if __name__ == "__main__":
    app.run(debug=True, port=7000)
