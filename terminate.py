import boto3
client=boto3.client('ec2')
response = client.terminate_instances(
    InstanceIds=['i-027257f4cb699c14b']
)