from datetime import datetime
from datetime import timedelta


def display_current_datetime():
    current_date = datetime.now()
    formatted = current_date.strftime('%Y-%m-%d %H:%M:%S')
    print(f"Current date and time: {formatted}")

def calculate_future_date():
    days = int(input("Please enter the number of days to add to the current date: "))
    current_date = datetime.now()
    future_date =current_date + timedelta(days=days)
    formatted = future_date.strftime('%Y-%m-%d')
    print(f"Future date: {formatted}")

