Plugings which we need:

1. AWS EC2 as we are running our python script on ec2.
2. Aws Setup -> to talk with aws cli
3. Boto3 needs to be installed on jenkins server
4. CLoud Should be configured under manage jenkins -> Configure cloud -> add access key and secret key to authenticate with AWS.

AWS Secrets Manager Credentials ProviderVersion
pipeline:aws setup
Amazon ec2

Ned to create aws acces key and secret keys and give them to jenkins to communicate with AWS

Then add a role to that ec2 instance with aws secrte manager permisiion to list out the secrets.

Finally tags are very important to pick up the secrets by jenkins
ex: jenkins:credentials:type 
value:string

