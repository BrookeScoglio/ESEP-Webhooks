import json

def lambda_handler(event, context):
    # Extract information from the event
    headers = event['headers']
    body = json.loads(event['body'])
    
    # Check if GitHub sent a ping event
    if headers.get('X-GitHub-Event') == 'ping':
        return {
            'statusCode': 200,
            'body': json.dumps('Ping received from GitHub!')
        }
    
    # Handle other GitHub events here
    # Example: Extract information from the issue event
    if headers.get('X-GitHub-Event') == 'issues':
        issue_title = body['issue']['title']
        issue_url = body['issue']['html_url']
        message = f"Issue Created: {issue_title}\nURL: {issue_url}"
        print(message)  # Log the message
        
        # You can add further processing or integrations here
        
        return {
            'statusCode': 200,
            'body': json.dumps('Issue event processed successfully.')
        }
    
    # If the event type is not supported, return an error
    return {
        'statusCode': 400,
        'body': json.dumps('Unsupported GitHub event type.')
    }
