from csv_validator.csv_validator import CSVValidator

validator = CSVValidator('C:/Users/Tuf/OneDrive/Desktop/python/pythonHomeworks/lab7/file.csv')
validator.read_csv()
validator.validate([
    {'column': 'Age', 'validation_type': 'missing_values'},
    {'column': 'Salary', 'validation_type': 'data_type', 'data_type': 'float64'}
])
print("All good in your file.csv")