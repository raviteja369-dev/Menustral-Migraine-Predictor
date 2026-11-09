
from django.shortcuts import render
import joblib
import numpy as np
import os

# Load model
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model.pkl')

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")

try:
    model = joblib.load(MODEL_PATH)
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    raise RuntimeError(f"Error loading model: {e}")

def home(request):
    """ Render the input form (predict.html) """
    return render(request, 'prediction/predict.html')

def predict_migraine(request):
    """ Process input & render result.html """
    if request.method == "POST":
        try:
            print("✅ Received POST request")  # Debugging Message

            # Extract input values
            features = [
                "age", "duration", "frequency", "on_periods",
                "symptom_severity", "stress_level", "sleep_hours",
                "diet_quality", "exercise_frequency", "medication_use"
            ]

            input_values = [float(request.POST.get(feature, 0)) for feature in features]

            # Convert inputs to NumPy array
            input_data = np.array([input_values])
            print(f"🔍 Input Data Shape: {input_data.shape}")  # Debugging Message

            # Ensure correct feature size
            if input_data.shape[1] != model.n_features_in_:
                raise ValueError(f"Expected {model.n_features_in_} features, but got {input_data.shape[1]}.")

            # Make prediction
            prediction = model.predict(input_data)[0]
            print(f"🎯 Prediction: {prediction}")  # Debugging Message

            return render(request, 'prediction/result.html', {"prediction": prediction})

        except Exception as e:
            print(f"❌ Error: {e}")
            return render(request, 'prediction/result.html', {"error": str(e)})

    return render(request, 'prediction/predict.html')  # Redirect back if not POST
