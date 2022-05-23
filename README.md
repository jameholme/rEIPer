# REIPER
                                           .""--.._
                                           []      `'--.._
                                           ||__      DNS   `'-,
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
  
1. Disassociates an EC2 instances's EIP
2. Releases the EIP from the AWS EIP Pool
3. Allocates a new EIP to the AWS EIP Pool
4. Associates the new EIP to the EC2 instace
5. Does "stuff" from the newly associated EIP
  
## Idea List:
* Create a loop to do this en masse
* Collect every EIP the EC2 Instance sees
  * Instead of storing the EIP data locally, send it to S3 Bucket(s)
* Create a way to do this in every Region
  * Put a REIPER in each Region
* Come up with a way to analyze the data in a meaningful way
  * OpenSearch in AWS? Can be used to create Dashboards and Visualizations
* Compare the EIPs Collected by the REIPERs against Grey Noise
  * Use Grey Noise tags to identify who last owned the EIP
  * Use Grey Noise tags to identify if an EIP has been used Maliciously and if so, how?
