import datetime
curr_time = datetime.datetime.now()

def demo_function(event,context):
    print(f"Hi This is demo lambda function running at the current time : {curr_time}")