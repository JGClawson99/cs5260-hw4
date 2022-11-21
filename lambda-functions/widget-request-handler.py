import json
import boto3

queue_url = "https://sqs.us-east-1.amazonaws.com/839482323059/cs5260-requests"

def lambda_handler(event, context):
    if not 'message' in event:
        return False
        
    request = event['message']
    try:
        json_request = json.dumps(request)
        if 'type' not in json_request:
            return False
        if 'requestId' not in json_request:
            return False
        if 'widgetId' not in json_request:
            return False
        if 'owner' not in json_request:
            return False
        try:
            boto3.client('sqs').send_message(QueueUrl=queue_url, MessageBody=json_request)
            return True
        except:
            return False
            
    except:
        return False
    