import boto3

def lambda_handler(event, context):
    # Initialize the AWS client
    ec2_client = boto3.client('ec2')

    # Specify the security group ID and the rule to remove
    security_group_id = 'sg-id' #addhere the Security Group ID that you want to revoke the HTTPS Protocol.
    ip_permission_to_remove = {
        'IpProtocol': 'tcp',
        'FromPort': 443,
        'ToPort': 443,
        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]  # Example IP range to remove
    }

    # Revoke the ingress rule
    response = ec2_client.revoke_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[ip_permission_to_remove]
    )

    print("Ingress rule revoked:", response)

    return {
        'statusCode': 200,
        'body': 'Ingress rule revoked successfully'
    }
