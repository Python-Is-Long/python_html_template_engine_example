import csv
import os
from flask import Flask, render_template
from pathlib import Path
from typing import List, Dict, Tuple, Union, Optional, Any

app = Flask(__name__, template_folder='templates')

# Read sales data from CSV (replace this with your actual data retrieval method)
def read_sales_data(csv_file: str) -> List[Dict[str, Any]]:
    """Read sales data from a CSV file and return as a list of dictionaries.

    Args:
        csv_file (str): Path to the CSV file.

    Returns:
        List[Dict[str, Any]]: List of dictionaries containing sales data.
    """
    sales_data: List[Dict[str, Any]] = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row: Dict[str, Any] = dict(row)
            sales_data.append(row)
    return sales_data

# Define route to generate and render HTML report
@app.route('/sales_report')
def generate_sales_report():
    # Replace 'sales_data.csv' with your actual file path or database query
    sales_data = read_sales_data('sales_data.csv')
    total_sales = sum(float(item['sales']) for item in sales_data)
    return render_template('sales_report.html', sales_data=sales_data, total_sales=total_sales)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
