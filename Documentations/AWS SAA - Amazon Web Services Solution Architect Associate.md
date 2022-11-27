# Part1: Basics & Concepts

## Cloud types:
Using Cloud Servers provide much more efficiency than on-Premises data centers, regarding cost, reliability & time.
### - Public Cloud & Private Cloud
Public cloud is Publicly shared among customers, while Private cloud is for only one customer
![Pasted image 20221109155939](https://user-images.githubusercontent.com/109697567/200851078-db999f92-50f4-4754-b526-a30fc7a2152a.png)

### - Hybrid cloud
A mix between public cloud & on-premises Private Cloud, to provide privacy & security for specific services while the other services are on Public cloud.
- It's a more complex solution as the organization has to manage multiple platforms.
- Suitable for effectiveness, backup, disaster recovery, development & testing.
### - Multi cloud
The use of multiple & different cloud computing & storage services in a single structure. Mostly because some services are better than others in a specific use.
### - Hybrid Multi Cloud
Using Hybrid cloud concept but with multiple vendors. 

## "Automation & Orchestration" Concept
- Automation concept is making the cloud processes automatic, like deployment, provisioning, upgrading, testing, etc.
- Orchestration concept is the idea of expanding your infrastructure.
## "Vendor lock-in" Concept
Using a specific cloud vendor in a major way & concentrating on its services makes it difficult to move to another vendor if required.


## AWS Cloud Services
![Pasted image 20221016203143](https://user-images.githubusercontent.com/109697567/200851567-a14762b4-7de7-4781-a033-4b74541c12f2.png)

## IAM - Identity & Access Management
IAM allows creating & managing multiple identities, authentication & authorization for AWS account.
So The same AWS account can have multiple users with different permissions, instead of only logging in as a ROOT User
### IAM Features:
- Shared access to AWS account
- Granular Permissions:
	Specific & strict permissions as desired.
- Secure access to AWS resources for AWS applications 
- Multi-factor authentication
- Identity Federation:
	The process of delegating a user authentication responsibility to a trusted external party. *ex:* Logging in by google authentication.
- Identity information logs
- PCI Compliance:
	Credit Card Compliance.
- Integrated with many AWS Services
- Eventually Consistent details & permissions
- Free to use
- AWS STS "AWS Secure Token Service":
	Temporary Sessions.

### IAM Identities
- Federated Users
- IAM User
- IAM Group
- IAM Role:
	IAM Role is a set of permissions, acts as a badge for a determined temporary time "STS - Security Token Service".


### IAM Console
### *_USERS:*

### Creating IAM User :
![Pasted image 20221019205435](https://user-images.githubusercontent.com/109697567/200852774-85c5e4d5-eef3-4ce5-bd19-b214dd05be7e.png)

### Setting Permissions or adding the user to a Group :
![Pasted image 20221019224718](https://user-images.githubusercontent.com/109697567/200853212-ea5ee1db-edfe-4781-9b56-668829901943.png)
### User details
![ezgif com-gif-maker](https://user-images.githubusercontent.com/109697567/201072140-3fda1335-eda2-4cfa-bad3-67ec2ecbb131.gif)
### Access Key
- A secret key that is download as .csv file, to login using it instead of username & password.
- If the access key or the file is lost, the access can be denied from the console, by selecting status to inactive.
![Pasted image 20221020014900](https://user-images.githubusercontent.com/109697567/200855856-2b1660ce-ec28-4190-9f75-5929b43136b6.png)

### *_ACCOUNT SETTINGS:*

### Password Policy
Having restrictions over passwords in the system
![Pasted image 20221020015357](https://user-images.githubusercontent.com/109697567/200855949-dab439c2-4ea5-4429-aa60-c8d9bd49ad10.png)
![Pasted image 20221020015627](https://user-images.githubusercontent.com/109697567/200856160-2c05dff0-7e09-4c78-81a7-dfb8f0473af3.png)

*Note:* When applying a new password policy, only new users will be affected, & the old users will only be affected after password expiry "Enable passwords expiration".

### IAM Best Practice
![Pasted image 20221020232823](https://user-images.githubusercontent.com/109697567/200856466-5ba41a25-b03d-4a30-90b4-052604d218dc.png)

## Creating Billing Alarms
Using the Root User, limiting bills to as low as 1$ & setting Billing alarms can be done through the Budgets tab in the Billing Dashboard.
This can be set to be a continuous **"Recurring budget"** or an **"Expiring Budget"**.
This is very important step to avoid unexpected bills over the budget plan.

## VPC - Virtual Private Cloud
- The Virtual Private Cloud, is a virtual data center in the cloud, confined to an AWS region & isolated from other VPCs b default.
- The client has full control over his VPC & is secured from other clients with other VPCs on the same cloud.
- A VPC is confined to a single AWS Region

### VPC Components 
- ##### CIDR Block
Each created VPC has  a main CIDR Block created with it & this main cannot be removed or changed, only the VPC can be totally deleted.
VPC Address Pool can be expanded by adding up to 4 secondary CIDR Blocks, with some limitations.
- ##### Subnets
Multiple subnets can be configured per VPC, not overlapping & strict for each *Availability Zone*, meaning they cannot stretch between multiple AZs.
- ##### Implied Router
AWS provides an implied virtual outer for the VPC, connecting all subnets to one another. This router is accessible or manageable only by AWS not the client.
- ##### Route Tables
 The client only edits the routing tables provided by the Implied Router
 - ##### Internet Gateway "IGW"
 Default VPCs are automatically assigned with Internet Gateway, created new VPCs doesn't, & must be assigned to an Internet Gateway Manually.
 Internet Gateway is fully managed by AWS not the client, horizontally scaled, redundant & highly available, & supports IPv4 & IPv6.
 Only one IGW can be assigned to a VPC at a time.
- ##### Virtual Private Gateway "VGW"
  An encrypted Gateway over the internet to establish connection to On-Premise with the cloud "For Hybrid Clouds".
  Only one VGW can be assigned to a VPC at a time.
- ##### Security Groups
- ##### Network Access Control Lists "Network ACL"
![Pasted image 20221025014904](https://user-images.githubusercontent.com/109697567/200856677-0264d399-5873-4213-a96f-029d700de759.png)
### VPC Console
By default there will a VPC on each region, this can be viewed from the VPC dashboard. 
From the VPC Console You can manage & view the info of current VPCs or create new VPCs, & manage all the VPC components listed before.
![Pasted image 20221024230911](https://user-images.githubusercontent.com/109697567/200856768-a6fb0c84-0b09-42a5-a9b5-cddc7a060af1.png)

## Public Subnet vs Private Subnet
Public Subnet is a subnet created in a VPC with IGW attached and its associated routing table contains a default route pointing at the VPC's IGW, meaning it has internet access, while private subnets doesn't have internet access.
Public Subnets is used for the applications & services that will need internet access, while Private Subnets is mainly for databases.
![Pasted image 20221031004509](https://user-images.githubusercontent.com/109697567/200856868-6a73eec2-b1b4-4fe3-b9a2-51e7f8099f82.png)

## Hybrid Cloud Connectivity Options in AWS
##### 1- VPN Connection
- Not reliable
- Over the internet connection
- Quick to deploy
- Secure
- Cost effective
##### 2- AWS Direct Connect Connection "DX"
- Long deployment times
- Reliable good performance
- Not secure by default as VPN Connection
*Note:* It's applicable to use "IPSec"/VPN on top of the DX to get the benefits of the DX with more reliable security.
Both Connections above are terminated on the "VGW" from the VPC end, & on the Customer Gateway from the On-Premises end.

## EC2 - Elastic Compute Cloud
EC2 is a service acting as Virtual Machines, with resizable computing capacity in the cloud, & fully manageable by the client with the root access.
EC2 can be provisioned on shared hosts (Between other AWS Client's EC2 instances) or dedicated hosts. There is a 20 EC2 instances soft limit per account. {{Soft limits is limits that can be changed, opposite of Hard Limits}}
EC2 is launched in a subnet in the availability zone.

### EC2 Instances Types:
##### 1- EBS Volumes - Elastic Block Store
- EBS volumes are volumes that keeps the data persistent & not lost after turning of the EC2.
- The EBS Volumes are always outside the EC2 instance but **in the same availability zone.**
- The EC2 volume holding the data is reached through internet access as its remote.
- EC2 instances with an EBS root volume are called EBS-Backed EC2 Instances.
##### 2- Instance-Store
- Also known as Block Storage, these volumes are in the same physical server as the EC2, & are not persistent.
- Access to Instance-store volumes are much faster than EBS Volume.
-  EC2 instances with an instance-store volume are called Instance-Store Backed EC2 Instances.

### EC2 SSH Keys
- No Password needed for login, only 2 Keys Pairs
- Public key is stored in AWS, Private key is a key the client keeps.
- The Private key is downloaded only at instance creation, if not or lost the instance should be terminated & start a new one.
### Methods of Connection
##### 1- SSH - Secure Shell Login for EC2 instances
##### 2- EC2 Instance Connect "Browser Based SSH Connection"

###### EC2 connecting by SSH client steps are shown in the console after trying to connect:
![Pasted image 20221031012059](https://user-images.githubusercontent.com/109697567/200857121-427a5bf5-ea49-4a1c-a9c6-dc11dd727afd.png)
![Pasted image 20221031012400](https://user-images.githubusercontent.com/109697567/200857171-dc7050f2-83b0-498e-a5cb-21df72a4573a.png)
*Note:* instead of typing the SSH key in the command, use the option -K for storing it in memory & option -A for the agent forwarding. 
![Pasted image 20221111065442](https://user-images.githubusercontent.com/109697567/201266337-b006c88e-0e45-4632-b8db-4095ad3e4720.png)
### Private, Public & Elastic IP Addresses 
![Pasted image 20221031014312](https://user-images.githubusercontent.com/109697567/200857220-2cb7281b-5258-439a-97f0-d2ef243fde0b.png)
*Note:* EIP has a soft limit of 5 per VPC "Can be changed by sending a ticket"

### NAT - Network Address Translation.
**No EC2 instance will launch without having a Private IP Address.** However it needs either Public IP Address or Elastic IP Address to simply be able to connect to it, as the EC2 is logged onto through the internet as every AWS service.
The EC2 Private IP Address is translated to its corresponding Public IP Address by NAT - Network Address Translation.
![Pasted image 20221031014808](https://user-images.githubusercontent.com/109697567/200857316-159c1a72-19ee-44a3-afb3-e9a5a1bbdd66.png)
EIP is mostly used to hold a specific IP for firewalls, so it is referred to as **whitelisting**.

### Monolithic vs Multi Tier, & Microservices
Monolithic is using one instance for the whole application & the entire application is built as a single code project, making it harder to scale & troubleshoot. It's more advisable to use multi tier instances for multiple parts of the project or the application.
![Pasted image 20221103010515](https://user-images.githubusercontent.com/109697567/200857450-e74b170d-9773-4cea-a7f8-5d19f298b6d5.png)
Microservices approach is dividing the tiers even more to be able to launch it on containers instead of VMs, as it's has more efficiency & speed.
![Pasted image 20221103041823](https://user-images.githubusercontent.com/109697567/200857510-5c6185df-2b3a-4976-a22f-bdaf49a0d814.png)

## Security Groups
- Security Groups are virtual firewalls applied on the ENI "Elastic Network Interface" of the EC2 instance.
- Traffic going into the ENI is called inbound traffic, & traffic from the ENI is called outbound traffic.
- Security Groups have only permit rules. no deny rules. If no permits are found it is considered as am implied deny.
- Can add up to 16 (5 default maximum) Security Groups per EC2 instance.
- Security Groups are stateful, meaning that if the traffic is allowed either if its inbound or outbound, the opposite direction response is automatically allowed even if no permit rules were found.
![Pasted image 20221031231048](https://user-images.githubusercontent.com/109697567/200858159-50800cf5-62a4-461b-a96e-eb1f2da305ca.png)

### Source & Destination Ports
Security Groups are basically settings for sources & destinations.
**vip.note:** Ephemeral Range is the set of ports of the client.
![Pasted image 20221031233103](https://user-images.githubusercontent.com/109697567/200858227-51a75904-2042-49d5-af92-bc7fe4b76c3c.png)
*Example:* In a working environment you want the SSH Logins to only be able to occur from a set of specific IPs,
![Pasted image 20221031233719](https://user-images.githubusercontent.com/109697567/200858305-7b2d9a8b-e39e-4793-acf9-ea3f8c6b25bd.png)

## NACLs - Network Access Control Lists
- NACL functions at a subnet level, so it's applied to all EC2 instances inside the subnet.
- It's applied at the implied router
- NACLs are **Stateless** "one way only".
- It includes permit & deny rules.
- Each NACL rule has a sequence number, rules are elevated from lowest to highest sequence number.
- Once a rule is found either permit or deny the process is stopped "no reading for rest of the rules", if none are found it ends with explicit deny.
- Traffic going into Subnet is called inbound traffic, & traffic from the Subnet is called outbound traffic.

**Security Group Vs NACL, NACL is applied to all EC2 inside the subnet**
![Pasted image 20221101011630](https://user-images.githubusercontent.com/109697567/200858369-1960439d-6b59-4b0e-b91d-a6c24b584bb6.png)
![Pasted image 20221101010350](https://user-images.githubusercontent.com/109697567/200858473-8400953f-d06d-48d9-88b3-bb090e1147bd.png)
*Note:* As Network ACL acts on the Subnet not the VPC, **its Dashboard is on the VPC Dashboard,** unlike the security groups which is on the EC2 Dashboard.

## Encryption
It's basically locking sensitive data or over network packets to prevent leakage of sensitive information, this locking is done with encryption keys of different kinds.

### 1- Encryption in-Transit using Asymmetric Keys
- Encryption between two ends, using a Public key & a Private key.
- Requires Key generator to create the key pair.
- The key owner holds the private key & shares the public key with clients.
**ie:** Owner encrypts with the private key & the client decrypts with the public key, & vice versa.

### 2- Encryption in-Transit using Symmetric Keys
- Uses the same key & encryption algorithm for encryption/decryption.
- It's more efficient than using the asymmetric key.
- The asymmetric encryption can be used to exchange symmetric keys.

### KMS - AWS Key Management Services
It's an *AWS managed* Key management service that allows customers to create & manage cryptographic keys.
- Controls keys usage & permissions for keys' access.
- integrated with many AWS services.
- Highly durable "Low loss" & highly available.
- Integrated with CloudTrail.
- It's a Regional service, meaning that created keys in RegionA will only work for RegionA, although the VPC is over multiple regions.
- $1/Month for each key customer created, or free for keys created by AWS services.
- CMKs - Customer Master Keys are the primary resources in the KMS.

#### CMKs - Customer Master Keys
- CMKs are used to provide either encrypted keys or plain keys.
- KMS provides encrypting data up to 4 Kbytes, bigger files require manual encrypting using CMKs generated keys.
- CMKs never leave KMS.
- KMS doesn't store customer data keys generated by CMKs, either encrypted or not.
- The encrypted Key held by customer can be sent to KMS to decrypt it to plain text again to be able to use it for decryption.
- There are both AWS-managed CMKs, or Customer-Managed CMKs
![Pasted image 20221101053243](https://user-images.githubusercontent.com/109697567/200858572-6bcdb521-0a49-47c3-ad5f-bd40c0b8de86.png)
Keys managed by AWS are known by the name of *aws/service_name* 
**Example:** creating an EC2 instance & encrypting EBS Volume:
![Pasted image 20221101054012](https://user-images.githubusercontent.com/109697567/200858659-e183d1f7-f56d-43df-b2bd-fbb2a354adcb.png)

**Note:**  AWS-managed CMKs have automatic key rotation of 3 years, while Customer-Managed CMKs have 1-year optional rotational period "If Chosen".

## AWS S3 -Simple Storage Service / Object Storage
- It's Object Storage based, Data & Meta-Data stored as whole objects & not divided into objects "as in Block Storage".
- Cheaper than Block Storage "as EBS Volumes"
-  Better scalability & durability.
- Cannot be mounted as a drive or a directory to an EC2 instance.
- Ideal for data growth storage as there is no limit on amount of data or metadata in an object, only the maximum size of a file is 5 Tbyte
- S3 Storages are called S3 Buckets, & the Buckets are confined to the Region & outside the VPC, backing up it to another regions must be done manually.
- The S3 Buckets' names are Globally Unique.
- There are no actual folders within a bucket, however this can be mimicked and attach a folder name to objects for work organization.
![Pasted image 20221101060601](https://user-images.githubusercontent.com/109697567/200858734-a6ce799d-7255-4082-a80d-2a4d0d7f4c13.png)

## Programmatic Access to AWS
Programmatic access for any IAM user isn't done by username & password, it requires an access key (Access Key ID & Secret Access Key) to access AWS Programmatically "**ex:** the windows cmd".
- The Secret Access Key is only shown at creation & must be saved. 
**Note:** Make sure you have AWS CLI installed on your OS terminal.
![Pasted image 20221101202112](https://user-images.githubusercontent.com/109697567/200858809-40d52a10-497f-4cf8-b91c-8fc7c6e0dc9e.png)
**Logging in by programmatic access using the log in keys:**
![Pasted image 20221102110038](https://user-images.githubusercontent.com/109697567/200858939-c5314e77-350c-4ced-bf86-1329bda8fe63.png)

## IAM Policies
- it's attached to an identity "IAM user, IAM role, etc." or a resource "item in a S3 Bucket".
- Policies are AWS-Managed, Customer-Managed, or inline Policy "for one user".
- More than one policy may be attached to an identity.
- By default all requests are denied for an identity, an explicit allow overrides this.
- an explicit deny overrides all allows.
- Policies are stored as JSON documents in AWS.

![Pasted image 20221102233310](https://user-images.githubusercontent.com/109697567/200859226-fd4774c1-acc6-4a1d-8b45-1ac2bac1e58e.png)

## SQS - Amazon Simple Queue Service (Message Queue Concept)
- Message Queues provide asynchronous communication & coordination for the application components.
- Messages are stored in queue reliably until they re processed, then get deleted.
- this allows scaling different parts of the project & increase its reliability.
- Message sending Tiers is called Message Produces, while message receiving Tiers is called Message Consumers.
- Using SQS is referred to as Decoupling process, as it decouples different tiers. 
![Pasted image 20221103012822](https://user-images.githubusercontent.com/109697567/200859377-e23e3e7a-5d3e-4faf-9ea3-c45a0f94bf51.png)

## SNS - Amazon Simple Notification Service
- SNS is a fast & fully managed notification service.
- Publisher is the sender "Producer" & Subscriber is the receiver "Consumer".
- Publishers publish messages to a SNS Topic, Subscribers receive messages from the SNS Topics they are subscribed to.
- Publisher must have the permissions to send in the SNS Topic "IAM Policies".
- Subscribers can be users, emails, SMSs, services & many other formats.
- SNS is reliable & stores multiple data copies across multiple AZs.
- SNS supports HTTPS in-transit.

![Pasted image 20221103014434](https://user-images.githubusercontent.com/109697567/200859449-f4fb80d3-3c56-4e0f-8234-26952278915b.png)

**Note:** Message size in SQS & SNS shouldn't exceed 256 Kbytes, indicating that the messages either in queue "SQS" or instant "SNS" won't include the data or the object itself, only a message about the data.

## CDN - Content Delivery Network (Amazon CloudFront)
- Amazon CloudFront Provides highly available cache to compensate using multiple resources for less latency "**ex:** Accessing data from S3 buckets through different countries"
- using CloudFront is more economically efficient than using different Buckets.
- These Cache Locations are called Edge Locations.
![Pasted image 20221103030233](https://user-images.githubusercontent.com/109697567/200859517-5740e0c2-2478-4a47-9fc4-df78dd78be47.png)

## Amazon Route 53
- Amazon Route 53 is AWS's DNS.
- Acts similar to the Public DNS for example.
- It supports public hosted zones for internet facing workload/applications, or private hosed zones for private workloads/on VPC applications.
- The DNS that have the domain name is called the Authoritative of the domain name.
![Pasted image 20221103032121](https://user-images.githubusercontent.com/109697567/200859583-e324ab9d-6d2a-4a78-ae6d-e2d24956b668.png)

## OLTP & OLAP
#### OLTP - On-Line Transactional Processing
- Uses detailed & Current data to store the transactional data
- Characterized by high volume of simple transactions & short queries.
#### OLAP - On-Line Analytical  Processing
- Stores analytical data & reports
- Characterized by relatively low transactions volume & very complex queries involving aggregations.

## RDS - Amazon Relational Database Service 
- it supports a set of databases services as MS SQL, MySQL, Maria DB, Oracle, PostgreSQL & Amazon Aurora.
- RDS Launches the database inside the VPC.
- It's advised to be put inside a private subnet.
- RDS is fully managed Database, so no customer or root access to it by default.
- If the instance control is required "root access", it's available to use EC2 instances for a self-managed database.
- A security group can be attached to the RDS database.
- RDS instance can be launched in a standalone mode "single AZ" or Multi-AZ mode (Primary instances for read/write & Standby RDS instances for instant data replication only).
- It supports auto scaling.

## High Availability & Fault Tolerance
- High availability describes the availability of the application, while Fault tolerance describes how much the application performance is affected by faults.
- High availability is done by Load Balancers.
- Higher Fault tolerance means higher cost, due to increase of resources.
![Pasted image 20221103042616](https://user-images.githubusercontent.com/109697567/200859632-0ad6166f-a411-4e40-9088-8b4c2930742d.png)

## Scalability & Elasticity
- Scalability refers to system's ability to handle the growth of load by adding resources.
- This scaling can be vertical scaling or horizontal scaling.
- Elasticity describes the system ability to provision & deprovision resources **automatically** to ensure that resources matches the need.
- Auto scaling groups can be configured for EC2 instances

![Pasted image 20221103043119](https://user-images.githubusercontent.com/109697567/200859709-cc84e90c-9afd-4851-90fa-87e2878137ac.png)

## CloudWatch
- CloudWatch is the center of real time monitoring & visibility in AWS.
- It's a metric data repository "per resource".
- Has the ability to add a custom metrics.
- Provides statistics & logs.
- Monitors alarms can be set & can trigger actions

## CloudTrail
- Any actions "APIs" taken by IAM users, roles or AWS services are recorded in CloudTrail.
- Events can be viewed & downloaded.
- It helps in governance & auditing the account.
- Events history are maintained for 90 days.
- Logs can be stored in a S3 Bucket for more than 90 days if desired, this is encrypted by default.
- CloudTrail is integrated with SNS.
- A trail created in the console is a multi-region trail, use the command interface to make a region trail.

### Logs Events types
#### 1- Management event
- Provide visibility into management & operations on resources.
- Free of charge.
- Enabled  by default.
#### 2- Data event 
- Provide visibility into resource level operations "objects in a bucket".
- Chargeable.
- Disabled by default.
#### 3- Insights Events
- Logs events for unusual API write activates in the account.
- Chargeable.
- Disabled by default.

### Log File Integrity Validation
- The ability of CloudTrail to determine whether a log file was modified, changed or deleted after delivering the logs to an S3 Bucket.
- This is beneficial in forensics investigations.
- Using a validation log file, you can accurately determine whether a log file was changed or not, & if so shows the user credentials involved in this activity.
- This is done by creating a hash for every log file delivered.

## Disaster Recovery - RPO & RTO
- #### RPO - Recovery Point Objective
RPO is the acceptable data to be lost after the restoration point "Backup point" due to a disaster.
- #### RTO - Recovery Time Objective
RTO is the acceptable time taken after the disaster to get active again & go back to last restoration point taken.
- RPO & RTO determines the cost of Disaster Recovery, less RPO & RTO means more cost with more efficient Disaster Recovery.
![Pasted image 20221109072525](https://user-images.githubusercontent.com/109697567/200859792-7bc9d1b9-29e9-4bd4-885e-c7f6424986fe.png)
AWS Approach in Disaster Recovery could be explained as having a DR Site fore disaster recovery, & it should be in a different region or away form the main production site. If the production went down, the cloud service is redirected to the DR Site, & it's advised to be automated redirection. 

### Disaster Recovery Approaches
Graded from lower cost & recovery speed to the higher cost & recovery speed as follows : 
##### 1- Backup & Restore
- Copies AMLs & backup data & store it in a different region.
- no active DR sites until the disaster happens.
##### 2- Pilot Light
- Keep the minimal needs of the infrastructure only "**ex:** Databases".
- Continuous data replication between the two sites.
##### 3- Warm Standby
- Keep a scaled down version of the production environment.
- The second site can be scaled up after the disaster if needed.
##### 4- Multi Site
- Keep full running version of the production environment.
- Active/Active Sites.
![Pasted image 20221109104352](https://user-images.githubusercontent.com/109697567/200860019-25a7675d-483e-4e56-a3ec-b6e87f6972f8.png)

# Part 2: VPC Deep Dive
## NAT Deep Dive & NAT services 
Suppose a scenario of which the EC2 in a private instance & need to update its data from an S3 Bucket, the bucket is accessible by a public IP on the internet, & same goes for all of AAWS Services. As the EC2 is in a private subnet it won't be able to connect to the S3 to get the update unless changed to a public subnet, removing the purpose which the EC2 is in a private subnet in the first place.. so the solution is refused.
There are two NAT Services that can fix the issue proposed:
#### 1- NAT Instance
- Its an EC2 instance AMI, so it's fully managed & secured by the client.
- NAT instance is launched in a public subnet.
- The routing table of the private subnet requiring internet access should be given a default route pointing to the NAT Instance ID
- The NAT instance has a translation table, having the source/destination IP & port, as well as the mapping IP & port.
- All Ports in the translation table are from the ephemeral range.
- The instance is given private or elastic IP address.
- The Mapping IP is the translated public IP in the NAT translation table of the Private/Elastic IP Address in the public subnet.
![Pasted image 20221110134611](https://user-images.githubusercontent.com/109697567/204100897-a689250c-5232-4226-ba0c-8676bb81b2e9.png)
#### 2- NAT Gateway
- NAT Gateway is a fully managed highly available service, scaling by up to 45 Gbps per gateway.
- NAT Gateways work only with Elastic IP Addresses.
- It cannot be associated with a security group.
- More preferred than instances due to its high availability.
- Although it's highly available, but it exists only in one availability zone.
![Pasted image 20221110134611](https://user-images.githubusercontent.com/109697567/204100927-adc7e210-278b-4f18-9ee1-01c0f2cf8966.png)
#### AZ Independent Architecture For High Availability
Multiple NAT Gateways are deployed over multiple Availability Zones "one per each", & have the route table of the private subnets in each AZ to its NAT Gateway.
So if a NAT Gateway went down the routing table redirects the packet to the other NAT Gateway in another AZ in the same network, & if an AZ went down, the other NAT Gateways keep functioning.
![Pasted image 20221110144124](https://user-images.githubusercontent.com/109697567/204100940-24c8b5b4-fabf-4cd6-92f0-4e578c278c28.png)
#### How they work:
The packet goes from the private subnet to the NAT instance/NAT Gateway in the public subnet, which redirects it to the IGW with a new public IP from the translation table in the IGW, sending it over the internet.

![Pasted image 20221110144738](https://user-images.githubusercontent.com/109697567/204100950-926f1638-67f8-4e06-93b3-84bbee21b5ee.png)

#### Console Applications:
###### 1- Creating NAT Instance
- Create an ordinary EC2 instance, with a NAT instance image which can be found in **Community AMIs**. 
- Make sure to add HTTP & HTTPS ports to the security group if it will be needed.
- **A very important note** when creating a NAT instance is **disabling the Source/Destination Check**. This is because by default the EC2 instance can  work as a source or a distention but not as an intermediate stage, this is controlled by the Source/Destination Check.

![Pasted image 20221111063112](https://user-images.githubusercontent.com/109697567/204100954-f63dcd97-e914-42cd-8849-2316d47fc8fe.png)
###### 2- Logging in to a Private Subnet's EC2 Instance using NAT Instance
- A private Subnet doesn't have internet access, so you can't access it remotely.
- To log in to a private subnet, log in to a NAT public instance & log in to the private one from it.
- Remember to add the NAT ID to the private subnet route table, with destination 0.0.0.0/0
- Access the Public EC2 instance then the Private one
- Use command **yum update -y** to se if the instance will update or not, to test connectivity.
![Pasted image 20221111073339](https://user-images.githubusercontent.com/109697567/204100966-cdc8b13a-ae18-4f6e-a83f-7b9c486ae0c9.png)
###### 3- Creating NAT Gateway
- Created from the VPC Console
- Created with an Elastic IP Address
- No Source/Destination Check, No Security Groups, etc.. As it's an AWS fully managed service
###### 4- Logging in to a Private Subnet's EC2 Instance using NAT Gateway
- Same as before, but instead of adding NAT Instance ID in the target in the routing table, add NAT Gateway ID with destination 0.0.0.0/0

***Notice that*** using the NAT Instance or NAT Gateway for accessing the private subnet made us allow SSH Port for accessing it. Despite this technique working properly, its not preferred in a production environment as the NAT shouldn't get SSH requests to access it, meaning that we should remove the SSH Port from  NAT Instance, & you can't SSH request on a NAT Gateway anyways.
	*What is the alternative?* Bastion Host

### Bastion Host
it's an EC2 instance with no applications, allowing SSH(22) "for Linux Bastion" or RDP(3389) "for Windows Bastion", & it has all required security applications. Bastion Host is the ONLY way to access the subnets from the internet.
Thus It's a regular EC2 Instance with Security Hardening "Strict & Heavy security" created & set by you. ***BASTION HOST IS NOT A SERVICE!***
- Bastion Hosts are launched in Public subnets
- You can set the Bastion Host to only allow SSH or RDP from the corporate IP Addresses range instead of any remote access, this is done from the Bastion Host Security Group.
- Remote accessing can be done by using a remote desktop, so the admins log in from home to the remote desktop in corporate, & then to the Bastion Host.
- For high availability, multiple Bastion Hosts can be set across different subnets & apply auto scaling between them.
- Bastion Hosts are used only for accessing the subnets, & not sending from inside a subnet to the internet. AWS recommends NAT Gateways for outgoing requests.
![Pasted image 20221124215306](https://user-images.githubusercontent.com/109697567/204100980-5b73c8c3-aa98-414f-acd9-3cfdb5316bcc.png)

### Proxy Server
- Proxy Servers are used for URL Filtering
- Created in Public Subnets
- It's created in the EC2 instance & works similar to NAT Instances
- If an EC2 in a private subnet required Proxy servers, the Proxy is initiated in a public subnet & the redirection happens similar to how NAT Instances did.
###### Reverse Proxy Server
it is a service that is used for caching. When accessing the application/website linked with a Reverse Proxy, the URL resolves to the R-proxy, filtering the traffic & then sending it to the application server, & it deals with the response from the application server the same way, caching the operation. So if the same request came again, it will response automatically as it's cached.

## Connecting VPCs together 
### VPC Peering
By default, VPCs cannot communicate directly with each other without using internet access(No Network between them). 
VPC Peering connection allows routing between two VPCs.
- Highly available & fully managed by AWS.
- The two VPCs can be from the same account or different account, & they can be in the same AWS region or not.
- The two VPCs cannot have overlapping CIDR ranges "not even in one subnet".
- Subnets routing tables must be edited & have the new VPC range added to it.
- The routing tables contain the CIDR Block Network Range.
- Transitive Peering is not allowed "No intermediate routing to VPCs".
- No Edge to Edge Routing "No intermediate routing to VPN/Direct connections".
![Pasted image 20221125215929](https://user-images.githubusercontent.com/109697567/204100991-2233a5dd-1cfc-49fa-a671-f32a635c4566.png)
*Note :* For any to any connection, the no. of required peering connections is N(N-1)/2

### AWS Transit Gateway
Upon increasing the no. of VPCs required to be connected together, more VPC Peering connections are required, & if on-premises is to be connected to the VPCs, no. of VPNs & DX will increase as will.
Here comes the use of Transit Gateway, as it can simplify communication requirements as the VPCs grow.
- Regional resource.
- Highly available & fully managed by AWS.
- Supports IPv4 & IPv6
- VPCs cannot have overlapping CIDR ranges "not even in one subnet".
- It allows intermediate routing through editable routing tables.
- If multiple regions is to be connected, a transit gateway peering can take place between the two AWS Transit Gateways.
- The routing tables contain the Subnets IP Addresses.
![Pasted image 20221125225925](https://user-images.githubusercontent.com/109697567/204101019-8cfadba7-6561-4fb0-a4b2-a294904e4089.png)
*Note:* Remember to edit the routing table either when using peering connection or Transit Gateway, setting each of them as the destination.

### VPC Peering & Transit Gateway in Console
##### 1- Peering Connection
- Check that the security groups & NACLs allow the connection & Ping Request.
- Upon creating Peering connection, the other VPC will get a pending request to accept or refuse.
- The peering connection request is accepted from the *Peering connection* table.
- After this step, if you tried to ping, time out will occur as the routing table is not set up yet.
- In the routing table, make sure to set the *Destination* as the other CIDR Network, & the *Target* as the peering connection.
- Edit both routing tables for both subnets containing EC2s you will use for the ping test.
##### 2- Transit Gateway
- For using Transit Gateway, first make sure to remove the peering connection from the routing tables to get rid of any black holes.
- When creating the Transit Gateway you will find the attachment type desired.
- After choosing the VPC, a new list will appear for you to choose which subnets to work with, as it's for subnet level.
- Edit the route tables after creating the Transit Gateway, make sure to set the *Destination* as the other CIDR Network, & the *Target* as the Transit Gateway.
 
## VPC Endpoints
Used for making applications/instances on private subnets connect to AWS services "as S3 Buckets" without a public end point "no internet access".
*ie:* Traffic going from the private subnet to the service does not go through the internet.
- They are virtual devices, that are redundant, scalable, & highly available.
- They allow VPC workloads to connect to supported AWS services without leaving the AWS network, thus no need of NAT instances or gateways.
- It has two types : **Gateway or Interface Endpoints***. "usage of each is according to the service."
*Note:* Only S3 & DynamoDB uses Gateways Endpoints, while services inside the VPC use Interface Endpoints.
![Pasted image 20221125233953](https://user-images.githubusercontent.com/109697567/204101037-8f3f1291-85e8-4614-b00a-a6975358256a.png)

##### 1- Gateway Endpoints
- Set as a target in the subnet's routing table
- Redundant & highly available.
- Only one is required per VPC, but each gateway reaches a service.
- You can configure multiple gateways for different services.
- Region Specific.
- No Security Groups.
##### 2- Interface Endpoints
- It's an interface with a private IP Address in a subnet you choose.
- Services that use this endpoint are known to be *Powered by AWS Private Link*.
- Supports IPv4
- Regional Specific.
- You can add Security Groups.
- No Routing is done, instead it's based on DNS resolution to the service.
*Note:* Remember to create an IAM Role for the instance with the permissions required for dealing with services, otherwise the endpoint will ensure the connection but the commands won't work.

### Controlling Access to services with VPC Endpoint Policies
- By default, an endpoint allows full access to the designated service.
- *Endpoint Policies* can be used to control who access what in the designated service
- The Policies exists for both kinds of endpoints.
*Notice:* No NACLs or Security Groups, its done through permission policies.

###  Accessing VPC Endpoints from Remote Networks using Proxy Server
One of the uses of Proxy servers, is that if we created it in a private subnet & connect the subnet with VPN or DX connection to an on-premises site, the proxy can be used to redirect the traffic from the site to the VPC Endpoints, making AWS services reachable from the site without internet traffic.
![Pasted image 20221126164858](https://user-images.githubusercontent.com/109697567/204101045-925a738f-511c-4afc-bd05-df4422f2c897.png)

## IPv6 Egress-only internet Gateway
All IPv6 addresses are public, thus any IPv6 address you need is allocated from AWS not you.
*What if you need a private instance allocated with IPv6?*
- Egress Only Gateway allows outbound IPv6 traffic, but prevents initiated inbound traffic from the internet to the VPC, so it was designed to satisfy private subnets requirements.
- It's attached to the VPC, & created under the VPC Console.
- It's stateful.
- cannot be associated by a security group. But notice that if this is required, the security groups & NACLs support IPv6, so you can add security roles as desired.
- It's assigned through the routing table as the target.
- A routing table can have both IPv4 & IPv6.

![Pasted image 20221127015503](https://user-images.githubusercontent.com/109697567/204120128-7754a9d3-9318-4c80-9c32-67d07a57d4fc.png)

## VPC Flow Logs
It's a feature allowing logging to the IP traffic going to & from the network interfaces in the VPC.
- It provides Source IP/Port, Destination IP/Port, and status (Accepted or Rejected).
- You can create a flow log per VPC, per subnet, or per ENI "Elastic Network Interface".
- Flow logs can be published to Amazon CloudWatch logs, *or* Amazon S3 Buckets.
- To create a flow log for any of the 3 levels, it's created in the Console under the desired level as in picture.
![Pasted image 20221127023122](https://user-images.githubusercontent.com/109697567/204120138-8c6bbdae-6459-446f-85dd-53ae6017ad85.png)

## Hybrid Cloud Connectivity

### VPN
Connecting a corporate data center to an AWS private subnet is done via static or dynamic routing. This is done using a *Customer Gateway* for the corporate level, & *VGW* for the cloud level.
- It uses IPSec to establish a secure connection.
	Internet Protocol Security "IPSec" is a secure network layer protocol suite that can authenticate & encrypt data packets between host & gateway.
- Internet-based connection, so quality & latency depends on the internet traffic.
- Routing is either static or dynamic.
- VPN encryption scope is not end-to-end encryption.
- The VGW IP address the corporate will connect to is public IP address, & the customer gateway IP address is also public.
- The customer gateway is the side that initiates connection.
- After initiating, two public IP addresses are assigned to the VGW "Not highly available as the customer gateway still has one IP address".
![Pasted image 20221127041838](https://user-images.githubusercontent.com/109697567/204120149-88bccdbf-dec0-4aed-b6d3-344034a5dbac.png)

#### VPN setup on Console
- Done under the VPC Console, VIRTUAL PRIVATE NETWORK (VPN) tab.
- You will notice that you have the option to create customer gateway, this is not a creation of course but it's defining the customer gateway that already exists on the corporate side.
![Pasted image 20221127042608](https://user-images.githubusercontent.com/109697567/204120154-aa970bbd-3956-46d5-bc99-08aba0b26601.png)
- Choose the option create virtual private gateway, to setup your VGW.
- The created VGW is detached, go to actions & attach it to a VPC.
![Pasted image 20221127042930](https://user-images.githubusercontent.com/109697567/204120171-02a3c6f5-0f1c-46f8-bf90-97b4d63d5992.png)
- Choose Site-to-Site VPN Connections, & create your VPN as desired.
- Download the configuration file & send it to the corporate to set up the customer gateway, as it is the one that initiates the connection not the VGW.

### AWS Direct Connect "DX"
- Requires an AWS Router, that is assigned to the internet provider in the customer country.
- the sub interfaces between the corporate & the ISP uses VLANs.
- Only Dynamic Routing is supported.
- Requires virtual interfaces "VIF"
- Private VIF is for VPC connections, & public VIF is for AWS public endpoints "for services".
- Provides low latency & consistent performance.
- Supports link aggregation up to 4 "Using multiple links as one logical link for higher speed & bandwidth".
- Customer can request a dedicated connection of speed 1-10Gbps.
- Customer can request a hosted connection with starting speed 50Gbps.
![Pasted image 20221127053917](https://user-images.githubusercontent.com/109697567/204120175-535ff2a7-05d2-457e-9b75-384f2c5f482e.png)

##### DX High availability options
DX Connection is not cost efficient, so setting up multiple DX links for high availability might not be the best option.
- You can use VPN connection as your high availability solution, this is obviously is not fault tolerant.
For higher fault tolerance "no economic limitings":
- You can use multiple DX links.
- You can use multiple DX links & multiple customer gateway.
![Pasted image 20221127055212](https://user-images.githubusercontent.com/109697567/204120182-89f63cb9-af37-444f-8a23-d9f4b00132ea.png)
*Note:* Remember that all of the connections after the DX router in the ISP cage is managed by AWS & stated as redundant & highly available. Thus no editing in these connection shall be considered.

#### Direct Connect Gateway
DX is a link to a specific region, if the region went down customer won't have access to the VPC without internet connection. Customer can use VPN connection after the DX router to reach the VGW assigned to the VPC. This makes the customer goes back to encrypting & secure connections again, dealing with ***public VIF***. *Another better & more efficient way is DX Gateway.*

Direct Connect Gateway allows reaching any VGW in the account, using a single ***private VIF***.
It can associate either with VGWs in VPCs, or with a transit gateway that has multiple VPC attachments in one region.
*Note:* DX Gateway won't establish any connection between the VPCs & each other. 
![Pasted image 20221127065015](https://user-images.githubusercontent.com/109697567/204120183-bc5e4c8a-776b-427f-90dc-696c707faa86.png)
##### Multiple Region DX Connections
DX Gateway can be associated with a transit gateway, so no multiple DX links will be needed across different regions. A ***Transit VIF*** will be needed for Transit Gateways connections "after the ISP as the public & private VIF".
![Pasted image 20221127070202](https://user-images.githubusercontent.com/109697567/204120189-e399b014-7919-48f8-93fb-639a8350e238.png)
*Note:* All kinds of DX connections are not considered secure "although the data link is dedicated to the customer", as the data is not encrypted. This can be overcome by using IPSec upon the DX connection, as stated before in Part 1.
