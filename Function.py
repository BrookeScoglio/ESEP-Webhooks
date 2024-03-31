import json
import os
import requests

def lambda_handler(event, context):
    # Parse the GitHub webhook payload
    payload = json.loads(event['body'])

    # Extract the HTML URL of the issue created
    issue_html_url = payload['issue']['html_url']

    # Construct the Slack notification message
    slack_message = {
        'text': f"Issue Created: {issue_html_url}"
    }

    # Get the Slack webhook URL from environment variables
    slack_url = os.environ.get('SLACK_URL')

    # Send the Slack notification
    response = requests.post(slack_url, json=slack_message)

    # Prepare the response for API Gateway
    response_body = response.text
    response_status_code = response.status_code

    return {
        'statusCode': response_status_code,
        'body': response_body
    }
