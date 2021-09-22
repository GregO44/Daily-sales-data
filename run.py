import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('daily sales data')

def get_sales_data():
    """
    Get sales figures input from the user
    """
    print("Please enter daily sales data from COB: ")
    print("Data should be 4 numbers, seperated by commas.")
    print("Example: 32,41,11,16\n")

    data_str = input("Enter your data here: ")
    print(f"The data provided is {data_str}")

get_sales_data()