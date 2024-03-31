import json
import os
import requests

def lambda_handler(event, context):
    input_json = json.loads(event['body'])

    payload = {
        'text': f"Issue Created: {input_json['issue']['html_url']}"
    }

    slack_url = os.environ.get('SLACK_URL')

    response = requests.post(slack_url, json=payload)
    response_text = response.text

    return {
        'statusCode': response.status_code,
        'body': response_text
    }
