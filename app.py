import csv
from flask import Flask, render_template
from typing import List, Dict, Any

# Create a Flask app instance
app = Flask(__name__, template_folder='templates')


def read_sales_data(csv_file: str) -> List[Dict[str, Any]]:
    """Read sales data from a CSV file and return as a list of dictionaries.

    Args:
        csv_file (str): Path to the CSV file.

    Returns:
        List[Dict[str, Any]]: List of dictionaries containing sales data.
    """
    # Initialize an empty list to store sales data
    sales_data: List[Dict[str, Any]] = []

    # Open the CSV file in read mode
    with open(csv_file, 'r') as file:
        # Create a CSV reader object
        reader = csv.DictReader(file)

        # Iterate through each row in the CSV file
        for row in reader:
            # Convert each row to a dictionary and append it to the sales_data list
            row: Dict[str, Any] = dict(row)
            sales_data.append(row)

    # Return the list of sales data
    return sales_data


@app.route('/sales_report')
def generate_sales_report():
    # Call the read_sales_data function to read sales data from the CSV file
    # Replace 'sales_data.csv' with the actual path to your CSV file
    sales_data = read_sales_data('sales_data.csv')

    # Calculate the total sales from the sales data
    total_sales = sum(float(item['sales']) for item in sales_data)

    # Render the 'sales_report.html' template with the sales data and total sales
    return render_template(
        template_name_or_list='sales_report.html',
        sales_data=sales_data,
        total_sales=total_sales,
    )


if __name__ == "__main__":
    # Run the Flask app in debug mode on a selected port
    app.run(debug=True, port=5000)
