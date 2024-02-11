#!/usr/bin/env python3

import argparse
import boto3
import requests

def action():
    # Creates a web request and saves the response to a file (this action can be modified to do ...other things...)
    url0 = "https://ifconfig.me"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
    for i in range(1):
        r0 = requests.get(url0, timeout=10)
        print("url0: " + str(url0) + ": " + str(r0))
        with open("REIPER-IPs.html",'ab') as f:
            f.write(r0.content + b"\n")

def reiper(region, instance_id):
    ec2_client = boto3.client('ec2', region_name=region)
    ec2_resource = boto3.resource('ec2', region_name=region)

    try:
        instance = ec2_resource.Instance(instance_id)
        # Check to see if an EIP is already assigned to the EC2 Instance
        response = ec2_client.describe_addresses(
            Filters=[
                {
                    'Name': 'tag:Name',
                    'Values': ['REIPER']
                }
            ]
        )
        public_ip = response['Addresses'][0]['PublicIp']
        print(f"{public_ip} assigned to {instance_id}")
        # If an EIP is already assigned, do action below
        action()
        # Disassociate the EIP from the EC2 Instance
        ec2_client.disassociate_address(PublicIp=public_ip)
        print(f'EIP {public_ip} disassociated from the instance {instance_id}')
        # Releases EIP from the AWS Account
        allocation_id = response['Addresses'][0]['AllocationId']
        ec2_client.release_address(AllocationId=allocation_id)
        print(f'EIP {public_ip} has been released')
    except IndexError:
        print(f"No REIP assigned to {instance_id}")
        # Allocates EIP to the AWS Account
        allocation = ec2_client.allocate_address(
            Domain='vpc',
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
        response = ec2_client.describe_addresses(
            Filters=[
                {
                    'Name': 'tag:Name',
                    'Values': ['REIPER']
                }
            ]
        )
        public_ip = response['Addresses'][0]['PublicIp']
        allocation_id = response['Addresses'][0]['AllocationId']
        ec2_client.associate_address(InstanceId=instance_id, AllocationId=allocation_id)
        print(f'EIP {public_ip} associated with the instance {instance_id}')
        # Now that an EIP is attached to the EC2, do action below
        action()
        # Disassociate the EIP from the EC2 Instance after action is done
        ec2_client.disassociate_address(PublicIp=public_ip)
        print(f'EIP {public_ip} disassociated from the instance {instance_id}')
        # Releases EIP from the AWS Account
        ec2_client.release_address(AllocationId=allocation_id)
        print(f'EIP {public_ip} has been released')

def parse_arguments():
    parser = argparse.ArgumentParser(description='REIPER - Rotates EIPs')
    parser.add_argument('-region', dest='region', required=True, help='AWS region')
    parser.add_argument('-instance-id', dest='instance_id', required=True, help='EC2 instance ID')
    return parser.parse_args()

def main():
    args = parse_arguments()
    reiper(args.region, args.instance_id)

if __name__ == "__main__":
    main()
