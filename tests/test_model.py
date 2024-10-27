import json
from sklearn.metrics import root_mean_squared_error
import xgboost as xgb
import pandas as pd

class TestPerformance:
    model = xgb.XGBRegressor()
    model.load_model('model/model.bst')

    def test_model_performance(self):

        # load data and target
        data   = pd.read_csv('tests/dataset/data.csv')
        labels = pd.read_csv('tests/dataset/target.csv')

        data.drop(data.columns[data.columns.str.contains('unnamed', case=False)], axis=1, inplace=True)
        labels.drop(labels.columns[labels.columns.str.contains('unnamed', case=False)], axis=1, inplace=True)
        data   = data.values
        labels = labels.values
        labels = labels.reshape((labels.size,))

        # Load baseline metrics
        with open('tests/data/baseline_metrics.json', 'r') as f:
            baseline_metrics = json.load(f)

        # Evaluate the new model
        pred = self.model.predict(data)
        predictions = [round(value, 1) for value in pred]
    
        # evaluate predictions
        mse = root_mean_squared_error(labels, predictions)

        # Compare new metrics with baseline
        assert mse < baseline_metrics['root_mean_squared_error']
        # Add more assertions if needed

