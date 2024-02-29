import pandas as pd


class CSVValidator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def read_csv(self):
        try:
            self.df = pd.read_csv(self.file_path)
        except Exception as e:
            raise Exception(f"Error reading CSV file: {str(e)}")

    def validate(self, rules):
        if self.df is None:
            raise ValueError("CSV file not yet read. Call read_csv() first.")

        for rule in rules:
            self._apply_rule(rule)

    def _apply_rule(self, rule):
        column = rule['column']
        validation_type = rule['validation_type']

        if validation_type == 'missing_values':
            self._check_missing_values(column)
        elif validation_type == 'data_type':
            data_type = rule['data_type']
            self._check_data_type(column, data_type)

    def _check_missing_values(self, column):
        if self.df[column].isnull().any():
            raise ValueError(f"Missing values found in column: {column}")

    def _check_data_type(self, column, data_type):
        if self.df[column].dtype != data_type:
            raise ValueError(f"Invalid data type in column {column}. Expected {data_type}, got {self.df[column].dtype}")
