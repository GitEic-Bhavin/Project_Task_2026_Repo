import os
import boto3

ssm = boto3.client('ssm')

def lambda_handler(event, context):
    param_name = "/test/dev/*"
    
    # Fetch parameter from SSM
    response = ssm.get_parameter(
        Name=param_name,
        WithDecryption=True  # Set True if using SecureString
    )
    
    env = response['Parameter']['Value']
    
    return {
        'statusCode': 200,
        'body': f"Retrieved DB URL successfully: {env}"
    }
