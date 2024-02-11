# REIPER
```
                                           .""--.._
                                           []      `'--.._
                                           ||__            `'-,
                                         `)||_ ```'--..        \
                     _                    /|//}        ``--._   |
                  .'` `'.                /////}              `\ /
                 /  .""".\              //{///                 V
                /  /_  _`\\            // `||
                | |(X)(X)||          _//   ||
                | |  /\  )|        _///\   ||
                | |L====J |       / |/ |   ||    
               /  /'-..-' /    .'`  \  |   ||   
              /   |  :: | |_.-`      |  \  ||   
             /|   `\-::.| |          \   | ||      
           /` `|   /    | |          |   / ||
         |`    \   |    / /          \  |  ||
        |       `\_|    |/      ,.__. \ |  ||
        /                     /`    `\ ||  ||
```
  
#### REIPER currently:
1. Disassociates an EC2 instances's EIP
2. Releases the EIP from the AWS EIP Pool
3. Allocates a new EIP to the AWS EIP Pool
4. Associates the new EIP to the EC2 instace
5. Does "stuff" from the newly associated EIP  
  5a. Currently records the EIPs to a file 
  
#### Requirements:
* AWS Account with appropriate permissions to interact with the AWS API, VPC, EC2, and S3 Resources
* EC2 Instance with an EIP and the AWS CLI configured
* Python3 + Pip
  * Boto3
  * Requests
   
#### Usage:  
`python reiper.py [-h] [-region] [-instance-id]`

#### Arguments:
`-h` Show this help message and exit
`-region` The AWS Region the EC2 Instance resides in
`-instance-id` The Instance ID of the EC2 Instance
  
#### Idea List:
* Loop it?
* Create a way to do this in every Region
  * Put a REIPER in each Region
* Come up with a way to analyze the data in a meaningful way
  * OpenSearch in AWS? Can be used to create Dashboards and Visualizations
* Compare the EIPs Collected by the REIPERs against a threat intelligence tool
  * This could tell us who last used this EIP and what they used it for
