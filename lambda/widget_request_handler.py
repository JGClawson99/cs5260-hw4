import json
import boto3

queue_url = "https://sqs.us-east-1.amazonaws.com/839482323059/cs5260-requests"

def lambda_handler(event, context=None):
    if not 'message' in event:
        return [False, "no message found"]
        
    request = event['message']
    try:
        json_request = json.dumps(request)
        json.loads(json_request)
        if 'type' not in json_request:
            return [False, "type not in request"]
        elif 'requestId' not in json_request:
            return [False, "requestId not in request"]
        elif 'widgetId' not in json_request:
            return [False, "widgetId not in request"]
        elif 'owner' not in json_request:
            return [False, "owner not in request"]
        else:
            try:
                return [True, boto3.client('sqs').send_message(QueueUrl=queue_url, MessageBody=json_request)]
            except:
                return [False, "error sending message"]
            
    except:
        return [False, "invalid json"]
