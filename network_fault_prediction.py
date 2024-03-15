import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load data from CSV
data = pd.read_csv('data.csv')


# Separate features and target variable

X = data[['signal_strength', 'packet_loss', 'latency', 'errors']]
y = data['fault']


# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train the model (Logistic Regression for demonstration)
model = LogisticRegression()
model.fit(X_train, y_train)
import pickle

# Save the model to a file
with open('network_fault_model.pkl', 'wb') as f:
  pickle.dump(model, f)

