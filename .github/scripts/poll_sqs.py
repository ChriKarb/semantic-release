import os
import json
import boto3
import requests

# Set up your AWS credentials and region
aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
aws_region = os.environ['AWS_REGION']

# Set up the SQS queue URL
sqs_queue_url = os.environ['SQS_QUEUE_URL']

# Set up your GitHub token
github_token = os.environ['GITHUB_TOKEN']

# Create an SQS client
sqs = boto3.client('sqs', region_name=aws_region, aws_accesss_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
def poll_sqs_queue():
    # Poll messages from the SQS queue
    response = sqs.receive_message(
        QueueUrl=sqs_queue_url,
        MaxNumberOfMessages=1,
        WaitTimeSeconds=20
    )

    # Process messages
    if 'Messages' in response:
        for message in response['Messages']:
            message_body = json.loads(message['body'])

            # Trigger the GitHub Actions workflow
            repo = message_body['repo']
            ref = message_body.get('ref', 'main')
            headers = {
                'Authorization': f'token {github_token}',
                'Accept': 'application/vnd.github+json'
            }
            api_url = f'https://api.github.com/repos/{repo}/actions/workflows/sqs_trigger.yml/dispatches'
            github_response = requests.post(api_url, headers=headers, json={'ref': ref})
            print(f"Triggered workflow in repo {repo} with response {github_response.status_code}")

            # Delete the processed message from the SQS queue
            receipt_handle = message['ReceiptHandle']
            sqs.delete_message(QueueUrl=sqs_queue_url, ReceiptHandle=receipt_handle)

        if __name__ == '__main__':
            poll_sqs_queue()