from flask import Flask, render_template
import csv

app = Flask(__name__)

# Read sales data from CSV (replace this with your actual data retrieval method)
def read_sales_data(csv_file):
    sales_data = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
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
