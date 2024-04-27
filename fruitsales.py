import pandas as pd

# Create the data
data = {
    'Apples': [35, 41],
    'Bananas': [21, 34]
}
index = ['2017 Sales', '2018 Sales']

# Create a Pandas DataFrame
df = pd.DataFrame(data, index=index)

# Write the DataFrame to a CSV file
df.to_csv('sales_data.csv', index=True)

