def lambda_handler(event,context):
    print(event)
    print(event['Records'][0]['body'])
    return {"statusCode" : 200, "body":'Success !!!'}