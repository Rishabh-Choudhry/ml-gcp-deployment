import pandas as pd
import numpy as np
from flask import Flask, request, jsonify
import pickle
import pandas as pd
import xgboost as xgb
import ast
import json

app = Flask(__name__)

# Load the model
model = xgb.XGBRegressor()
model.load_model('model/model.bst')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    input_df = ast.literal_eval(data['input_data'])
    input_df = np.array(input_df)
    prediction = model.predict([input_df])
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


# import os
# import xgboost as xgb
# import pandas as pd
# import pickle

# # Rename existing new_model.pkl to previous_model.pkl
# if os.path.exists('new_model.pkl'):
#     os.rename('new_model.pkl', 'previous_model.pkl')

# # Load training data
# X_train = pd.read_csv('X_train.csv')
# y_train = pd.read_csv('y_train.csv')

# # Train the model
# model = xgb.XGBClassifier()
# model.fit(X_train, y_train)

# # Save the new model
# with open('new_model.pkl', 'wb') as f:
#     pickle.dump(model, f)
