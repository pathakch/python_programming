import json
import datetime
import os

# import requests


def lambda_handler(event=None, context=None):
    """
    This is a practice function built on SAM and deployed in AWS 
    which shows current date and time"""
    curr_date_time = datetime.datetime.now()
    print(f"This is present working directory : {os.getcwd()}")
    print(f"This is current date and time :{curr_date_time}") 