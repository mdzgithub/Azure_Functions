import azure.functions as func
from datetime import datetime, timedelta
import json
import logging
import io
import csv
import random

app = func.FunctionApp()


def generate_expense(category):
    expenses = {
        'travel': (50, 500),
        'food': (10, 100),
        'supplies': (75, 300)
    }
    return round(random.uniform(*expenses[category]), 2)

@app.function_name(name="DailyExpenseReportGeneratorFromNew")
@app.timer_trigger(schedule="0 0 12 * * *", arg_name="myTimer")
@app.blob_output(arg_name="outputblob", 
                 path="expense-reports/expense-report-{datetime}.csv", 
                 connection="TargetBlob")
def main(myTimer: func.TimerRequest, outputblob: func.Out[bytes]) -> None:
    utc_timestamp = datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'
    
    # Generate expense report data
    people = ['Bill', 'Sue', 'Mary']
    categories = ['travel', 'food', 'supplies']
    entries_per_person = 4
    
    data = []
    for person in people:
        for _ in range(entries_per_person):
            category = random.choice(categories)
            amount = generate_expense(category)
            data.append((utc_timestamp, person, category, f'${amount:.2f}'))
    
    # Create a CSV in memory
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['Date', 'Name', 'Category', 'Amount'])
    writer.writerows(data)
    
    # Convert to bytes and write to blob
    outputblob.set(output.getvalue().encode('utf-8'))
    
    # Generate the filename for logging
    now = datetime.utcnow()
    filename = f"expense-report-{now.strftime('%Y%m%d')}.csv"
    
    # Log information
    if myTimer.past_due:
        logging.info('The timer is past due!')
    logging.info(f'Daily Expense Report Generator function ran at {utc_timestamp}')
    logging.info(f'CSV has been written to blob storage as {filename}')