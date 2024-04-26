import boto3

def lambda_handler(event, context):
    # Initialize the AWS client
    ec2_client = boto3.client('ec2')

    # Specify the security group ID
    security_group_id =  'sg-id' #addhere the Security Group ID that you want to revoke the HTTPS Protocol.

    # Define the ingress rule for HTTP traffic (TCP port 80)
    http_rule = {
        'IpProtocol': 'tcp',
        'FromPort': 443,
        'ToPort': 443,
        'IpRanges': [{'CidrIp': '0.0.0.0/0'}], # Adjust as needed, this allows HTTP traffic from any IP

    }

    # Add the HTTP rule to the security group
    response = ec2_client.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[http_rule]
    )

    print("HTTP rule added:", response)

    return {
        'statusCode': 200,
        'body': 'HTTP rule added successfully'
    }
