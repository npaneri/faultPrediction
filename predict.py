import pickle
import pandas as pd
# Load the saved model
with open('network_fault_model.pkl', 'rb') as f:
  model = pickle.load(f)

# New network data for prediction (replace with actual values)
new_data = {'signal_strength': -2, 'packet_loss': 1000, 'latency': 55, 'errors': 15}

# Convert data to a DataFrame
new_data_df = pd.DataFrame([new_data])

# Make prediction
prediction = model.predict(new_data_df)[0]

if prediction == 1:
  print("Potential network fault detected!")
else:
  print("Network functioning normally.")
