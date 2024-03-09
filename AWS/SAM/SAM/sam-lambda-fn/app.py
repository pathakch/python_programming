import json
import pandas as pd

def lambda_handler(event, context):
    """Sample pure Lambda function"""

    count = event['count']
    data = []
    for i in range(count):
        data.append(i*50)
    df = pd.DataFrame(data,columns=['Numbers'])
    print("Data")
    print(df)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Success",
            "Count":count
          
        }),
    }
