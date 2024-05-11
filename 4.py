import boto3
import csv

#writer = csv.writer(file)
csvfile= open('profiles1.csv', 'w', newline='') 
writer = csv.writer(csvfile)
field = ["Account_id", "Region","VPC ID","CIDR Block"]
writer.writerow(field)  

# Initialize the EC2 client
ec2_client = boto3.client('ec2', region_name='ap-south-1')  # Replace with your desired region
iam = boto3.resource('iam')
current_user = iam.CurrentUser()
acc_id = (current_user.arn.split(':')[4])
print(acc_id)
#id = boto3.client('sts').get_caller_identity().get('Account')
#name =   boto3.client('organizations').describe_account(AccountId=id).get('Account').get('Name')
#org = boto3.client('organizations')
#account_name = org.describe_account(AccountId=acc_id)
#print(account_name)

#print(response)
# Describe all VPCs
#response = ec2_client.describe_vpcs()
#print(response)

response1 = ec2_client.describe_regions(
)

#print(response1)
for Region in response1['Regions']:
    Region = Region['RegionName']
    #print(f"Region: {Region}")
    ec2_tmp = boto3.client('ec2', region_name=Region) 
    vp_response = ec2_tmp.describe_vpcs()
    #print(vp_response)
    for vpc in vp_response['Vpcs']:
      vpc_id = vpc['VpcId']
      cidr_block = vpc['CidrBlock']
      print(f"Account_id: {acc_id}, Region: {Region}, VPC ID: {vpc_id}, CIDR Block: {cidr_block}")
      writer.writerow([acc_id, Region, vpc_id, cidr_block])

    #vpc_id = vpc['VpcId']
    #cidr_block = vpc['CidrBlock']
   # RegionName = Region['region']
    #print(f"VPC ID: {vpc_id}, CIDR Block: {cidr_block}")
  #  print(f"Region: {RegionName}")

# Extract relevant information
#for vpc in response['Vpcs']:
 #   vpc_id = vpc['VpcId']
  #  cidr_block = vpc['CidrBlock']
   # print(f"VPC ID: {vpc_id}, CIDR Block: {cidr_block}")
