import json
import boto3

queue_url = "https://sqs.us-east-1.amazonaws.com/839482323059/cs5260-requests"

def lambda_handler(event, context=None):
    if 'message' in event:
        body = [False, "no message found"]
        
        request = event['message']
        try:
            json_request = json.dumps(request)
            json.loads(json_request)
            if 'type' not in json_request:
                return error("type not in request")
            elif 'requestId' not in json_request:
                return error("requestId not in request")
            elif 'widgetId' not in json_request:
                return error("widgetId not in request")
            elif 'owner' not in json_request:
                return error("owner not in request")
            else:
                try:
                    return formatResponse(boto3.client('sqs').send_message(QueueUrl=queue_url, MessageBody=json_request))
                except:
                    return error("error sending message")
        except:
            return error("invalid format")
    else:
        return error("message not found")
    
def error(message):
    return {
            "statusCode": 400,
            "headers": {
                "Content-Type": "text/plain",
                "x-amzn-ErrorType": 400
            },
            "isBase64Encoded": "false",
            "body": "400: " + message
        }
    
def formatResponse(body):
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "isBase64Encoded": "false",
        "multiValueHeaders": {
            "X-Custom-Header": ["My value", "My other value"]
        },
        "body": body
    }
    