# quality_inspection_ai.py
"""
AI-powered quality inspection script.
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

class QualityInspectionAI:
    def __init__(self, data_file='quality_inspection_data.csv'):
        self.data = pd.read_csv(data_file)
        self.model = RandomForestClassifier(n_estimators=100)
    
    def preprocess_data(self):
        """
        Preprocess the data for training the quality inspection model.
        """
        # Example preprocessing logic
        self.data.dropna(inplace=True)
        X = self.data.drop('quality_label', axis=1)
        y = self.data['quality_label']
        return train_test_split(X, y, test_size=0.2, random_state=42)
    
    def train_model(self):
        """
        Train the quality inspection model.
        """
        X_train, X_test, y_train, y_test = self.preprocess_data()
        self.model.fit(X_train, y_train)
        score = self.model.score(X_test, y_test)
        print(f'Model trained with score: {score}')
    
    def inspect_quality(self, input_data):
        """
        Inspect the quality of the product based on input data.
        """
        prediction = self.model.predict([input_data])
        return prediction[0]

# Example usage
if __name__ == "__main__":
    # Assume quality_inspection_data.csv exists with appropriate data
    qia = QualityInspectionAI()
    qia.train_model()
    
    # Example input data
    input_data = np.array([0.5, 0.2, 0.1, 0.3])  # Replace with actual feature values
    quality = qia.inspect_quality(input_data)
    print(f'Predicted quality label: {quality}')
