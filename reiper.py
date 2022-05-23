#!/usr/bin/env python3

import boto3
import requests
import json

AWS_REGION = ""
EC2_CLIENT = boto3.client('ec2', region_name=AWS_REGION)
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
INSTANCE_ID = ""
INSTANCE = EC2_RESOURCE.Instance(INSTANCE_ID)

def ACTION():
# Creates a web request and saves the response to a file
    url0 = "https://ifconfig.me"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
    for i in range(1):
        r0 = requests.get(url0, timeout=10)
        print("url0: " + str(url3) + ": " + str(r0))
        with open("/home/ec2-user/REIPER-IPs.html",'ab') as f:
            f.write(r0.content + b"\n")

def REIPER():
    try:
# Check to see if an EIP is already assigned to the EC2 Instance
        response = EC2_CLIENT.describe_addresses(
            Filters=[
                {
                    'Name': 'tag:Name',
                    'Values': ['REIPER']
                }
            ]
        )
        PUBLIC_IP = response['Addresses'][0]['PublicIp']
        print(str(PUBLIC_IP) + " already assigned to " + str(INSTANCE_ID))
# If an EIP is already assigned do action below
        ACTION()
# Disassociate the EIP from the EC2 Instance
        response = EC2_CLIENT.describe_addresses(
            Filters=[
                {
                    'Name': 'tag:Name',
                    'Values': ['REIPER']
                }
            ]
        )
        PUBLIC_IP = response['Addresses'][0]['PublicIp']
        response = EC2_CLIENT.disassociate_address(
            PublicIp=PUBLIC_IP,
        )
        print(f'EIP {PUBLIC_IP} diassociated from the instance {INSTANCE_ID}')
# Releases EIP from the AWS Account
        response = EC2_CLIENT.describe_addresses(
            Filters=[
                {
                    'Name': 'tag:Name',
                    'Values': ['REIPER']
                }
            ]
        )
        PUBLIC_IP = response['Addresses'][0]['PublicIp']
        allocation_id = response['Addresses'][0]['AllocationId']
        EC2_CLIENT.release_address(
            AllocationId=allocation_id
        )
        print(f'EIP {PUBLIC_IP} has been released')
# Allocates EIP to the AWS Account
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
# Attaches EIP to the EC2 Instance
        response = EC2_CLIENT.describe_addresses(
            Filters=[
                {
                    'Name': 'tag:Name',
                    'Values': ['REIPER']
                }
            ]
        )
        PUBLIC_IP = response['Addresses'][0]['PublicIp']
        allocation_id = response['Addresses'][0]['AllocationId']
        response = EC2_CLIENT.associate_address(
            InstanceId=INSTANCE_ID,
            AllocationId=allocation_id
        )
        print(f'EIP {PUBLIC_IP} associated with the instance {INSTANCE_ID}')

# If EIP is not assigned and errors out with an Index Error do action below
    except IndexError:
        print("No EIP assigned to " + str(INSTANCE_ID))
# Allocates EIP to the AWS Account
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
# Attaches EIP to the EC2 Instance
        response = EC2_CLIENT.describe_addresses(
            Filters=[
                {
                    'Name': 'tag:Name',
                    'Values': ['REIPER']
                }
            ]
        )
        PUBLIC_IP = response['Addresses'][0]['PublicIp']
        allocation_id = response['Addresses'][0]['AllocationId']
        response = EC2_CLIENT.associate_address(
            InstanceId=INSTANCE_ID,
            AllocationId=allocation_id
        )
        print(f'EIP {PUBLIC_IP} associated with the instance {INSTANCE_ID}')
# Now that an EIP is attached to the EC2 do action below
        ACTION()
# Disassociate the EIP from the EC2 Instance after action is done
        response = EC2_CLIENT.describe_addresses(
            Filters=[
                {
                    'Name': 'tag:Name',
                    'Values': ['REIPER']
                }
            ]
        )
        PUBLIC_IP = response['Addresses'][0]['PublicIp']
        response = EC2_CLIENT.disassociate_address(
            PublicIp=PUBLIC_IP,
        )
        print(f'EIP {PUBLIC_IP} diassociated from the instance {INSTANCE_ID}')
# Releases EIP from the AWS Account
        response = EC2_CLIENT.describe_addresses(
            Filters=[
                {
                    'Name': 'tag:Name',
                    'Values': ['REIPER']
                }
            ]
        )
        PUBLIC_IP = response['Addresses'][0]['PublicIp']
        allocation_id = response['Addresses'][0]['AllocationId']
        EC2_CLIENT.release_address(
            AllocationId=allocation_id
        )
        print(f'EIP {PUBLIC_IP} has been released')
# Allocates EIP to the AWS Account
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
# Attaches EIP to EC2
        response = EC2_CLIENT.describe_addresses(
            Filters=[
                {
                    'Name': 'tag:Name',
                    'Values': ['REIPER']
                }
            ]
        )
        PUBLIC_IP = response['Addresses'][0]['PublicIp']
        allocation_id = response['Addresses'][0]['AllocationId']
        response = EC2_CLIENT.associate_address(
            InstanceId=INSTANCE_ID,
            AllocationId=allocation_id
        )
        print(f'EIP {PUBLIC_IP} associated with the instance {INSTANCE_ID}')

REIPER()
