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
                | |L====J |       / |/ |   ||   Rotate 
               /  /'-..-' /    .'`  \  |   ||   EIP 
              /   |  :: | |_.-`      |  \  ||   Every
             /|   `\-::.| |          \   | ||   Round   
           /` `|   /    | |          |   / ||
         |`    \   |    / /          \  |  ||
        |       `\_|    |/      ,.__. \ |  ||
        /                     /`    `\ ||  ||
  
It is a tool that:  
1. Disassociates an EC2 instances's EIP
2. Releases the EIP from the AWS EIP Pool
3. Allocates a new EIP to the AWS EIP Pool
4. Associates the new EIP to the EC2 instace
5. Does "stuff" from the newly associated EIP
  
## To-do List:
* Collect every EIP the EC2 instance sees
* Create a loop to do this en masse
* Create a way to do this in every region (from a single script?)
* Come up with a way to analyze the data
