from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Print it in the format YYYY-MM-DD HH:MM:SS
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date(days_to_add):
    # Get the current date
    current_date = datetime.now()
    # Add the specified number of days
    future_date = current_date + timedelta(days=days_to_add)
    # Print the future date in YYYY-MM-DD format
    print("Future date:", future_date.strftime("%Y-%m-%d"))

def main():
    display_current_datetime()
    try:
        # Ask user for number of days
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("Please enter a valid integer for days.")

if __name__ == "__main__":
    main()