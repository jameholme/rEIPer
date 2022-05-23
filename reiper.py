#!/usr/bin/env python3

import json
import boto3
import requests

AWS_REGION = "us-east-1"
EC2_CLIENT = boto3.client('ec2', region_name=AWS_REGION)
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
INSTANCE_ID = ""

####################################################################
# Disassociates an EC2 instances's EIP
instance = EC2_RESOURCE.Instance(INSTANCE_ID)

response = EC2_CLIENT.describe_addresses(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': ['REIPER']
        }
    ]
)

public_ip = response['Addresses'][0]['PublicIp']

response = EC2_CLIENT.disassociate_address(
    PublicIp=public_ip,
)

print(f'EIP {public_ip} diassociated from the instance {INSTANCE_ID}')

####################################################################
# Releases the EIP from the AWS EIP Pool
response = EC2_CLIENT.describe_addresses(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': ['REIPER']
        }
    ]
)

public_ip = response['Addresses'][0]['PublicIp']
allocation_id = response['Addresses'][0]['AllocationId']

EC2_CLIENT.release_address(
    AllocationId=allocation_id
)
print(f'EIP {public_ip} has been released')

####################################################################
# Allocates a new EIP to the AWS EIP Pool
allocation = EC2_CLIENT.allocate_address(
    Domain='project',
    TagSpecifications=[
        {
            'ResourceType': 'elastic-ip',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'REIPER'
                },
            ]
        },
    ]
)

####################################################################
# Associates the new EIP to the EC2 instace
response = EC2_CLIENT.describe_addresses(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': ['REIPER']
        }
    ]
)

public_ip = response['Addresses'][0]['PublicIp']
allocation_id = response['Addresses'][0]['AllocationId']

response = EC2_CLIENT.associate_address(
    InstanceId=INSTANCE_ID,
    AllocationId=allocation_id
)

print(f'EIP {public_ip} associated with the instance {INSTANCE_ID}')

####################################################################
# Does "stuff" from the newly associated EIP
# Writes the new EIP to a file
response = EC2_CLIENT.describe_addresses(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': ['REIPER']
        }
    ]
)

public_ip = response['Addresses'][0]['PublicIp']
with open("eip",'a') as f:
    f.write(public_ip)
