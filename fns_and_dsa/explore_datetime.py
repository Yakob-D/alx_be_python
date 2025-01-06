from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(f"Current date and time: {current_date}")

number_of_days = int(input("Enter number of days: "))
def calculate_future_date(number_of_days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days = number_of_days)
    print(f"Future date after {number_of_days} days: {future_date.strftime('%Y-%m-%d')}")

display_current_datetime()
calculate_future_date(number_of_days)