# VM Availability  (VM SLA)
![Pasted image 20241203142538](https://github.com/user-attachments/assets/2421553a-0bf6-47f8-8f2e-56f1fda044dd)

##### Fault Domain
##### Update Domain
##### Availability Sets
##### Availability Zones
![Pasted image 20241215094507](https://github.com/user-attachments/assets/8db19f22-b865-4a2f-a0e8-fe4f0c1f0282)

# Scaling
Scale Set
Load Balancer

# APP Services (PaaS)
APP Services (same as beanstalk)
APP Services VNet integration 
APP Services access restrictions

# APP Service Environment 
- Special type of app service deployed directly to a dedicated VNet
- VNet can be configured like any other VNet - Subnets, NSGs, etc
- Created on dedicated hardware
- Quite expensive...
##### Uses:
- Elevated security - complete isolation
- Very high scale requirements (More than App services)

# ACI
Azure container Instance (same as ECS)
# AKS
Azure Kubernetes Service (same as EKS)

# Azure functions Cold start issue
![Pasted image 20241203155732](https://github.com/user-attachments/assets/e7afa02b-4993-42c6-8e29-fd4f80b5694f)
## Functions Plans
- Consumption Plan: 
	- Pay only for what you actually use
	- Limit of 1.5GB RAM
	- Has Cold Start
- Premium:
	- Pay for pre-warmed instances (hosts)
	- Pay for scale-out instances
	- No cold starts
	- No memory limit (up to host RAM)
	- Better performance
	- VNet integration
	- Predictable price, but of course more expensive
- Dedicated:
	- The Functions run on an existing App Service
	- Great if server is under-utilized
	- No additional costs
	- Make sure Always On setting in the App Service is activated to avoid disabling functions
	- No Auto-Scale is the major downside

![Pasted image 20241203160557](https://github.com/user-attachments/assets/5856d872-d9e1-402d-91d3-1499dae63cbf)
![Pasted image 20241203161035](https://github.com/user-attachments/assets/cf028f9c-4cbb-4986-b85f-d11053e92e0b)
# Load Balancer
Operates at layer 4 (Network layer)
![Pasted image 20241208155944](https://github.com/user-attachments/assets/feebd8b4-87fa-499e-8b0f-ad95e790ca01)
# Application Gateway
Operates at layer 7 (Application layer)
![Pasted image 20241208162429](https://github.com/user-attachments/assets/b2b53ab3-1717-43b8-86f1-94594a66446b)
It has two types
- Standard_V2
- WAF_V2 (Additional WAF, & double the price)
##### WAF (Web Application Firewall)
- Protects web apps against common attacks
	ie. Cross-site scripting, SQL injection, etc.
- Protection rules based on OWASP Core Rule Set
- Updates continuously
- Works in Detection or Prevention mode
![Pasted image 20241208163032](https://github.com/user-attachments/assets/0e2fbe4d-2e0e-40e1-a073-2e29fba0d06f)
# VM Security 
1) JIT (Just in time) access
2) VPN
3) Jump box (Bastion host concept)
4) Bastion (service)
### Service Endpoint
A lot of managed services expose public IP (ie. Azure SQL Server, App Services, Storage and more)
Sometimes these resources are accessed only from resources in the cloud (i.e.. Database in the backend might pose a security risk)

- Service Endpoint solves this security risk
- Creates a route from the VNet to the managed service
- The traffic never leaves Azure backbone
	• Although the resource still has a public IP
• Access from the internet can be blocked
• Is free!
![Pasted image 20241208131447](https://github.com/user-attachments/assets/5b918c29-6a69-4ffe-b063-e97466e6c8bb)

### Private Links
Similar to service endpoints, a solution to the same problem
- Not free
- The traffic doesn't leave the VNet, unlike service endpoints, which leaves the VNet but uses azure network.

![Pasted image 20241208132100](https://github.com/user-attachments/assets/de52d5eb-b6f3-4895-8e11-e0d304f566ac)
# Databases & Storages
## Azure SQL Database
##### Features
- Managed SQL Server on Azure
- Single database on a single server
- Automatic backups, updates, scaling
- Good compatibility with on-prem SQL Server
	- Not all features are supported
##### Availability
- Backup is stored in a geo-redundant storage
- Active geo-replication
- SLA: 99.9% - 99.995%, depends on tier and redundancy (second highest SLA in Azure)
##### Compute Tiers
- Provisioned (Can be reserved)
- Serverless (Can't be reserved)
##### Security
- IP firewall rules
- Service Endpoints
- SQL & Azure AD Authentication
- Secure communication (TLS)
- Data encrypted by default (TDE)
##### Backup
- Full: Every week
- Differential: Every 12-24 hrs
- Transaction Log: Every 5-10 mins

Backup Retention period has two tiers:
- Regular Backup: Keeps data for 7-35 days
- Long term backup: up to 10 years
## Elastic Pool
- Based on Azure SQL
- Allows storing multiple databases on single server
- Great for databases with low average utilization and infrequent spikes
- Cost effective
- Purchase the compute resources you need, not the database
## Managed instance
- Closer to the on-prem SQL Server
- Near 100% compatible with on-prem SQL
- Can be deployed to VNet
- Business model close to on-prem one
###### Main differences than other DBs:
- No active geo-replication
- SLA: 99.99%
- Supports built-in functions
- Runs CLR code (Others can not)
- No auto scaling & tuning (as it's managed)
- No availability zone
- No serverless tier
- No Hyperscale
## Azure MySQL
##### Availability
- Backup is stored in a geo-redundant storage
	- In General Purpose and Memory Optimized tiers
- SLA: 99.99%
##### Security:
- IP firewall rules
- Service Endpoints
- Private Endpoints
- Regular & Azure AD Authentication
- Secure communication (TLS)
- Data encrypted by default
##### Backup
Depends on the service tier:
- Basic
	- Full backup: daily
- General Purpose up to 4GB
	- Full backup: once a week
	- Differential backup: twice a day
	- Transaction log backup: every 5 minutes
- General Backup up to 16 GB
	- Full backup: Once created
	- Differential backup: once a day
	- Transaction log backup: every 5 minutes

Backup retention period:
- 7-35 days, no native long term retention support.
##### Pricing
Pricing based on:
1) Tier:
	- Basic - Require light compute and 1/0 performance
	- General Purpose - Most business workloads
	- Memory Optimized - Require in-memory performance
2) Compute power (No. of VCores)
## Azure PostgreSQL
##### Availability
- Backup is stored in a geo-redundant storage
	- In General Purpose and Memory Optimized tiers
- SLA: 99.99%
##### Security:
- IP firewall rules
- Service Endpoints
- Private Endpoints
- Regular & Azure AD Authentication
- Secure communication (TLS)
- Data encrypted by default
##### Backup
Depends on storage size:
- General Purpose up to 4GB:
	- Full backup: once a week
	- Differential backup: twice a day
	- Transaction log backup: every 5 minutes
- General Purpose up to 16GB:
	- Full backup: Once created
	- Differential backup: thrice a day
	- Transaction log backup: every 5 minutes

Backup retention period:
- 7-35 days, no native long term retention support.
## Cosmos DB
- **Fully managed *NoSQL*** database
- Amazing performance - <10ms for 99% of operations
- Globally distributed
- Fully automatic management - updates, scaling, fixes etc.
- Multiple APIS:
	SQL, Mongo, Gremlin, Azure Table, Cassandra (per account)
- Can be distributed across many regions (configurable)
- API automatically picks the closest one When using write replication SLA is 99.999% (Highest SLA in Azure)
- Managed automatically, no code changes required
##### Security
- IP firewall rules
- Service Endpoints
- Private Endpoints
- Azure AD Authentication
- Secure communication (TLS)
- Data encrypted by default
##### Partitions
- Partitions are the basic scale unit in Cosmos DB
- Distribution and scale are per partitions
- Make sure items are divided as evenly as possible
- It's extremely important to select the right partition property
- ***Cannot be modified***
##### Consistency levels
***Traditionally***:
- Relational DB - Strong consistency: Call returns only after successful commit in all replicas (High availability)
- NoSQL DB - Eventual consistency: Call returns immediately, commit in replicas happens later (Low latency)
***Cosmos DB has 5 consistency levels***: 
- Strong (As in regular relational DB)
	![Pasted image 20241209133854](https://github.com/user-attachments/assets/6bda6020-6770-477c-94e1-a76a09e2f2b5)
- Bounded Staleness
	![Pasted image 20241209133926](https://github.com/user-attachments/assets/0becf7f6-7578-448b-887c-270ac8835690)
- Session
	![Pasted image 20241209134341](https://github.com/user-attachments/assets/4a56bea0-2c79-4f3d-9017-a7b8e6f007e4)
- Consistent Prefix
	![Pasted image 20241209134125](https://github.com/user-attachments/assets/440306d9-0745-4b7d-9360-d7e8710b09ba)
- Eventual (As in regular NoSQL DB)
	![Pasted image 20241209134210](https://github.com/user-attachments/assets/f8411d0e-9b4a-4255-921d-14c8464d1ac3)

***Note:*** Cosmos DB consistency level is configured on the account level, & can be *relaxed to lower consistency* on the request level.
##### Operations:
- Provisioned - Predefined number of RU/s, can be changed manually later. Offers reserved capacity up to 65% discount
- Auto Scale - Set the maximum RU/s, Cosmos scales up to this number. Good for unpredictable loads
- Serverless - Pay for what you use. No SLA
##### Pricing
Pricing based on:
- Operations type: (Provisioned, Auto Scale, Serverless)
- Write Regions
- No. of provisioned RU/s
## Azure Redis
##### Features
- Managed Redis on Azure
- Provides lightning-fast in-memory, distributed cache
- Great for short-lived, frequently accessed data
	ie. shopping cart, stock quotes
- Fully compatible with OSS Redis (community edition) and Enterprise Redis - depends on service tiers
##### Security 
- IP firewall rules
- Service Endpoints
- Private Endpoints
- Secure communication (TLS)
##### Tiers
- Basic
	Based on a single VM, no SLA, no distribution. Good for dev/test
- Standard
	Based on two VMs, replicated. SLA- Up to 99.9%
- Premium
	High-performance, better throughput, lower latency. SLA- Up to 99.95%
- Enterprise
	Based on Redis Enterprise, offers additional features (RediSearch, RedisBIoom and more). SLA — Up to 99.99%
- Enterprise Flash
	Uses non-volatile memory. Reduces storage cost. SLA - Up to 99.99%
##### Pricing
Based on:
- Tier
- Memory
## Azure Storage
- Massively scalable
- Accessible via HTTP or HTTPS
- Client libraries for almost every language
##### Types
- Blobs: Object Store
- Files: File shares for cloud and on-prem deployments
- Queues
- Tables: NoSQL data store
- Disks: Storage volumes for Azure VMS
### Azure Blob Storage
##### Features:
- Object store (Blob = Binary Large Object)
- Great for files, videos, documents, large texts etc.
- Up to 190TB per file
- Extremely cost effective
- Massively scalable
- Great availability options
- Extremely easy to use
- Usually used in conjunction with SQL / NoSQL database
##### Security:
- IP firewall rules
- Service Endpoints
- Private Endpoints
- Shared Access Signatures
- Access Keys & Azure AD Authentication
- Secure communication (TLS)
- Data encrypted by default
##### Storage Tiers
![Pasted image 20241209144820](https://github.com/user-attachments/assets/71562867-fb60-40fb-95f0-7fc188cab03c)
- Retrieval time is the same in Hot and Cool tiers
- Archive tier does not support ZRS, GRS and RA-GRS redundancy
- Using SLA improves to 99.99% (Hot) and 99.9% (cool)
- Tier is set at account level, can be modified per blob
- Moving between tiers can be automated by lifecycle rules
##### Redundancy
![Pasted image 20241209144616](https://github.com/user-attachments/assets/81234e7a-4961-4416-a35f-6fcb2c242fd5)
## Selecting the right storage solution
![Pasted image 20241209151014](https://github.com/user-attachments/assets/90c04f47-b511-472e-bbc6-b547a693a363)

# Messaging 
## Storage Queue
- Part of Azure Storage Account
- The simplest queue implementation
- Create queue → Send Message → Receive message
- No special pricing for queue, included in Storage Account
- Same for availability
## Events Grid (Similar to SNS)
- Allows building event-based architectures
- Publishes events to interested parties
- No queue / no order
- Strong integration with many Azure services
- Cost effective, simple pricing
- No tiers, HA is built in
- SLA: 99.99%
- Max event size:  1 MB
- Performance:
	- 10,000,000 events / sec
	- 5,000 events / sec / topic
- Latency: Subsecond end-to-end latency in the 99th percentile
- Pricing is based on number of operations only, & first 100k operations are free
![Pasted image 20241211130304](https://github.com/user-attachments/assets/21f70339-e476-4edf-b7e1-ab38c75415c1)
![Pasted image 20241211130149](https://github.com/user-attachments/assets/9216e9cf-9110-4127-b5ba-e1a91e857d56)
## Service Bus
##### Features:
- Supports point-to-point (Queue) and pub/sub (Topic) scenarios. "Combines both previous two scenarios"
- Fully managed, full blown message queueing service
- SLA: 99.9% 
- Can be configured for geo-disaster recovery
- Durable
- Compatible with AMQP protocol, which is used with IoT Services.
- Compatible with JMS 2.0 API (Premium only), which is widely used with Java based systems.
##### *SOME* Advanced features:
- Message sessions (guarantees FIFO)
- Dead-letter queue
- Scheduled delivery
- Transactions
- Duplicate detection
##### Security:
- IP Firewall rules
- Service endpoints
- Private endpoints
##### Tiers:
- Basic: Only queues & scheduled messages, no topics
- Standard: Made to fit almost any requirement
- Premium: For apps that need larger message size & increased security using resource isolation. 
![Pasted image 20241211153300](https://github.com/user-attachments/assets/0330cbcc-1aa9-43a3-b5a7-9c7df3997b0d)
##### Pricing
Based on:
	- Tier
	- No. of operations
## Event Hubs
- Big Data streaming platform and event ingestion service
		***Note***: No "messaging" in the description
- It's mainly a managed Kafka implementation
- Can receive millions of events per second
<img width="759" alt="Pasted image 20241211154844" src="https://github.com/user-attachments/assets/70c6091b-1661-4e2e-809e-000c94027a97" />

##### Pricing:
Based on:
- Tier
- Ingress traffic
-  Throughput unit (TU)
	One TU equals:
	- Ingress (Input) - IMB/sec or 1000 events/sec
	- Egress (Output) - 2MB/sec or 4096 events/sec
	***Note:*** TUs are Repurchased, & billed by the hour
## Selecting the right messaging solution
![Pasted image 20241211163312](https://github.com/user-attachments/assets/0c3fc822-0bd6-4d24-b2f0-66d90ed2b31c)
# Azure AD
Central identity and access management cloud service. Used to manage access to thousands of apps.
### Tenants
- Also called Directory
- A specific instance of Azure AD containing accounts and groups
- A tenant can be assigned to multiple subscriptions
- It is NOT part of the subscription hierarchy, thus it's not a resource.
	- Exists beside the subscription
	- For new subscriptions, a new tenant is created automatically
![Pasted image 20241212104529](https://github.com/user-attachments/assets/25a5065c-d3c4-4940-af8d-1688c9175810)
## Role Based Access Control (RBAC)
Create roles with specific authorization policies, & directly assign them to users, or remove the role from the user.
![Pasted image 20241212115730](https://github.com/user-attachments/assets/9bce6107-1283-4f92-a3e4-a2329f9117ec)
### Users & Groups
- Manages and stores the users that are part of the tenant
- Groups the users in Groups
	- Examples: IT Admins, Developers, etc.
	- Allows defining roles to groups instead of each user
### Azure Roles
- **Owner**: Can perform any action on the resource, including assigning roles to it
- **Contributor**: Can perform any action on the resource, but cannot assign roles to it
- **Reader**: Can only view data, but cannot change anything
It's always better to assign roles to groups and not individual users for easier maintenance
### Managed Identities
- Similar to AWS IAM Roles
- Used to assign Azure AD identity to Azure resource
- The resource can connect to other Azure resources using this identity
- No need to handle credentials (usernames, passwords etc.)

- Mainly **assigned** to ***App services, VMs, Event Grids, Functions***, but there are more resources that support it.
- Mainly **authorizing** resources such as ***SQL, Event Hubs, Service Bus, Storage, Key Vault***, but there are more resources that can be authorized to by it.
###### Types:
- System assigned: 
	Managed by Azure, tied to the resource's lifecycle (when the resource is deleted - so is the identity)
- User assigned:
	Managed by the user. Can be assigned to multiple resources, not tied to any lifecycle
##### Azure AD Licenses
![Pasted image 20241212113228](https://github.com/user-attachments/assets/50325eb3-5643-4223-94c7-7f23d9f5470f)
## Azure AD B2C
- Identity-as-a-service for your application
- A Business-to-Customer (B2C) service
- Enables integrating identity services in your app
##### Azure AD vs Azure AD B2C
![Pasted image 20241212131918](https://github.com/user-attachments/assets/d1579d60-8b02-4848-ad22-eb0be43878f6)

- Basically, it's a service used for identity authentication related ACTIONS, it doesn't hold the users details.
- ***Note:*** Azure AD B2C is quite complex to set up, and has a lot of moving parts
##### Features:
- MFA
- Conditional Access
- Audit Log
- Custom policies
- Custom pages
- And more...
## Azure AD connect
Connects & sync on-prem active directories with Azure active directory 
##### Modes:
- Password Hash Sync
	The passwords are copied to Azure AD, Authentication happens in the cloud.
- Pass-Through
	Passwords stay on-prem, Azure AD passes data to on-prem for validation.
# Monitoring
Monitoring is based on two types of data:
- Metrics: 
	Numeric values describing resource's aspect at a specific point in time
	- Examples: CPU, Disk, Response Time
- Logs
	Events that occurred in the system, can be textual & numeric
	- Examples: System started, Error occurred
Monitoring section in most resources:
![Pasted image 20241212142504](https://github.com/user-attachments/assets/08a61828-319b-4677-ad80-8fc404e6a836)
## Insights
- A collection of metrics, statistics and insights about the resource
- Specific to resource type
- Generated automatically
- Code-based services (App Services, apps on VMs) can integrate Application Insights into the code and gain a lot of data about app usage, performance, etc.

- Insights of a storage account, note the failures, performance, availability, and capacity options.
![Pasted image 20241212144619](https://github.com/user-attachments/assets/29aba8c9-5bbe-4f82-8a26-254b062b73fd)
- Another example for insights for a Virtual machine, notice how the metrics are generated automatically and specified for each type of resource.
![Pasted image 20241212144804](https://github.com/user-attachments/assets/d7b668cd-368a-4341-bee7-e75df899b66c)
## Monitoring Dashboard
When using the monitoring section in a resource page, the filters we set for viewing won't be saving & will need to be reentered upon each visit.
- Monitoring Metrics are saved in dashboards:
![Pasted image 20241212143208](https://github.com/user-attachments/assets/19dda924-a8f1-4cf6-9793-9cb29c7009dc)

We can customize the dashboard as we like.
- Customizing a Dashboard:  
![Pasted image 20241212143330](https://github.com/user-attachments/assets/27db9a59-45f7-401b-ac5f-e966c4d3d7f6)

- Another Ready dashboard
![Pasted image 20241212143444](https://github.com/user-attachments/assets/39ed11d4-ec85-45fa-8361-20313db0e92f)
## Alerts
##### Alert components
- Condition: When to trigger the alert (i.e.. CPU goes above 90%)
- Actions: What to do? Usually send notifications. Notifications are sent to Action Groups.
- Details: Contents of notification
##### Pricing:
- Per metrics measured
- Per notification type
## Azure Monitor (Service)
- A central location for all the monitoring aspects of Azure's resources
- Provides access to metrics, logs, insights and more
- Has additional capabilities not found in the individual resources
## Log Analytics Workspace
- Logging system
- A central location for storing, organizing and analyzing logs
- Aggregates logs from all connected, monitored resources
- Uses specialized query language to query logs
- Located in a designated region
	Better be the same region of the resources to save costs
# Security
## KeyVault
- Safely stores secrets of various types
- Very restricted access - needs Azure AD authentication
- Supports Hardware Security Modules (for enhanced security)
- Easily manageable
- Accessed via REST API
- Very cost effective (1,000,000 operations will be ~ 3$)
## Security Center
- A central location for monitoring and alerting security-related issues
- Displays a summarized list of problems found in the subscription's resources
- In some cases, allow a single-click fix
# Disaster Recovery
## DR concept 
##### DR Plan Choice
- Hot:
	- Failover to secondary site happens automatically with no downtime
	- No data loss
	- Requires duplicate infrastructure
	- The most expensive method
- Cold:
	- Failover to secondary site takes some time
	- Might be manual
	- Some data might be lost
	- Less expensive
##### RPO & RTO
- RPO
	- Recovery Point Objective.
	- How much data we allow ourselves to lose in case of a disaster.
	- Usually measured in minutes.
	- Low RPO might be needed in case of a massive reporting system.
- RTO
	- Recovery Time Objective.
	- How much downtime we can tolerate in case of a disaster.
	- Usually measured in minutes as well.
	- Low RTO might be needed in case of a global chat.
##### DR Implementation
1) Restore the data to nearest relevant point (if not synced
in real time)
2) Activate the compute resources in the second region (if not active)
3) Modify routing to the resources in the second region (auto or manual)
## DR in Azure
### DR of Data
##### RPO=0 (no data loss in case of disaster)
We need database that always syncs with the secondary region, databases capable of doing so are:
- Azure SQL (with Geo-Replication and Failover Group)
- Cosmos DB (with multi-region Cosmos account)
- Azure Storage (with GRS redundancy)
##### RPO>0 (some data loss in case of disaster)
- Ensure DB's backup frequency is compliant with the RPO

- Azure MySQL has backup occurrence every 5 minutes.
- If we replicated the backup to another region, we can later create a new Azure MySQL DB in the second region when needed.
- This is much cheaper because we don't have an active DB.
![Pasted image 20241212160916](https://github.com/user-attachments/assets/d89693c4-145f-450c-8efb-d7ac173685a9)
### DR of Compute
##### RTO=0 (no downtime in case of disaster)
- Full replication of all necessary resources.
- Full replication of the Data
##### RTO>0 (some downtime in case of disaster)
**Either**:
- Have non-active (passive) compute resources on standby in secondary region
- Create the compute resources when disaster occurs in secondary region
### DR Re-routing 
**Major three methods**:
1) Inform the users about the new address of the app (in the secondary region)
2) Manually change DNS record to point to the secondary region
3) Use automatic routing
	- Traffic Manager
	- Front Door
#### Traffic Manager
- DNS-based traffic load balancer
- Enables traffic distribution across global Azure regions
- Provides high availability and responsiveness
- Pricing is *majorly* based on DNS queries 
##### Used algorithms for routing:
![Pasted image 20241212162137](https://github.com/user-attachments/assets/2abf68a1-cd96-4741-824c-8a0f18d71389)
**Note:** Priority algorithm is the one that is mostly used for DR re-routing
#### Front Door
- Global entry point for web apps
- Works on Layer 7 (HTTP/HITPS)
- Multiple routing methods.
- Similar to Application Gateway but in global scale.
- Pricing is based on inbound & outbound traffic.
##### Features:
- URL-path based routing
- Session affinity
- SSL Offloading
- Web Application Firewall (WAF) integration
- URL Rewrites
- HTTP/2 support
#### Traffic routing or Front Door?
- Generally, if HTTP-related capabilities are needed, go with Front Door
	Examples:
	- URL-path based routing
	- SSL Offloading
	- Web Application Firewall
- Otherwise , go with Traffic Manager, usually cheaper
