# Expense Report Simulator Azure Function

This Azure Function simulates the daily submission of expense reports for three employees. It generates a CSV file containing the simulated expense data and uploads it to Azure Data Lake Storage for further processing.

## Overview

The function is scheduled to run daily at 7:00 AM, simulating the submission of expense reports by three employees. This automated process ensures consistent data generation for downstream analysis and processing.

## Features

- Generates simulated expense report data for three employees
- Creates a CSV file with the simulated data
- Uploads the CSV file to Azure Data Lake Storage
- Runs automatically at 7:00 AM daily

## Prerequisites

- Azure subscription
- Azure Function App
- Azure Data Lake Storage Gen2 account


## Usage

Once deployed and configured, the function will automatically run daily at 7:00 AM. No manual intervention is required.

The generated CSV file will be stored in the specified Azure Data Lake Storage container with the following naming convention:

```
expense_report_YYYY-MM-DD.csv
```

Where `YYYY-MM-DD` represents the current date.

## Function Code Overview

The main components of the function are:

1. `generate_expense()`: Creates simulated expense data for three employees.

## Customization

To modify the number of employees or the structure of the expense report, edit the `generate_expense_data()` function in the `__init__.py` file.

