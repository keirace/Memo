
# Cloud Computing

## Fundamentals of Cloud Computing

### Scaling

Scaling represents the ability of the resource to handle increased or decreased usage demands
- **Horizontal Scaling**
  - scaling in/out 
  - refers to adding more/less number of servers to distribute the workload

- **Vertical Scaling**
  - scaling up/down 
  - performance by adding more resources (such as CPU, RAM, or storage) to a single machine
  - always involves downtime (has to be powered off to scale)
<br>

- **Real-world scenario where vertical scaling is preferred**:

In a scenario where a business is running a database that requires high performance, such as a large relational database like Oracle or MySQL, vertical scaling might be preferred. Databases can benefit from vertical scaling because it simplifies data consistency and query execution without the complexities of managing data across multiple servers, which can introduce latency and consistency challenges.

For instance, if a company’s database application needs better performance due to larger datasets or more transactions, adding more CPU and RAM to a single server (vertical scaling) can enhance performance without requiring architectural changes, as would be needed with horizontal scaling.

### Business Drivers

- **Capacity planning**
  - strategies
    * Lead strategy - capacity to IT resource in anticipation of demand
    * Lag strategy - when reaching full cap
    * Match strategy - small increments
- **Cost reduction**
  * Expenses
    * Convert CapEx to OpEx
      * Capital - upfront
      * Operating - recurring
- **Organizational agility**

### Cloud Characteristics
for  an IT environment to be considered cloud, it must meet the following:
1. On-demand self service
2. Broad Network Access
3. Resource Pooling (multitenancy) - enables an instance of the program to serve different consumers (tenants) whereby each is isolated from the other
4. Elasticity - scalable
5. Measured Service - pay only for the service consumed

### Cloud Delivery Models

- Iaas
  - provides self-contained IT environment consisting of hardware, networking, connectivity, Operating Systems and other “raw” it resources
  - Popular IaaS providers are Amazon Web Services, Google Cloud Platform, Microsoft Azure, IBM SoftLayer, Rackspace
- PaaS
  - provides “ready-to-use” environment to deploy applications
  - Cloud consumers do not have control over or manage the underlying cloud infrastructure
  - Popular PaaS providers are Heroku, IBM BlueMix and Google App Engine
- SaaS
  - Popular SaaS offering examples are Gmail, GitHub, Google Drive

### Cloud Deployment Models

1. Public cloud
2. Community cloud
   - similar to a public cloud except that its access is limited to a specific community of cloud consumers.
3. Private cloud
4. Hybrid cloud 

# DevOps

- term that focuses on collab between dev and it ops

## The software development lifecycle (SDLC) & Challenges with Self Hosted Applications

- Cannot auto push updates, features and bug fixes until IT deploys
- Vendor and end-users are at mercy of IT team’s availability.
- low ROI due to infrastructure cost as its not elastic
- Bad UX

## Benefits of SaaS

- Better ROI
- less cost for muti-tenant SaaS
- multiple deployments a day
- Company manages the infrastructure

## Cloud
- low barrier to entry
- minimal capital
- no upfront capital expenses
- Validate ideas quickly at relatively low cost
- Scale with users
- Control your infrastructure costs

## Practices
- Key: Collab
- Development and operations teams coalesce into a functional team
- **Infrastructure as Code**
  - fundamental principle of DevOps
  - applying the same rigor of application code development to infrastructure provisioning and setup
  - Infrastructure provisioning, orchestration, and deployment should support the use of "infrastructure code"
  - All infrastructure provisioning "code" and environment configuration must be stored in version management system such as Git

```
Infrastructure as Code (IaC) is the practice of managing and provisioning computing infrastructure through machine-readable configuration files, rather than through manual hardware configuration or interactive configuration tools.

With IaC, infrastructure changes can be version-controlled just like application code, making it easier to track and manage changes over time.

Principles of Infrastructure as Code:

	1.	Idempotency:
	•	The idea that applying the same configuration multiple times results in the same infrastructure state. Regardless of how many times a script or configuration is applied, the infrastructure remains consistent and in the desired state without introducing duplicate or conflicting resources.
	2.	Version Control:
	•	All infrastructure configurations are stored in version control systems (e.g., Git). This allows teams to track changes, roll back to previous versions, and collaborate more effectively. It also ensures that infrastructure changes are auditable and documented.

```
- **Automation**
  - focuses on the setup, configuration, deployment, and support of infrastructure and the applications that run on it.
  - set up environments more rapidly in a standardized and repeatable manner. The removal of manual process is a key to a successful DevOps strategy.
  - Benefits
    - Rapid Changes
    - Improved Productivity
    - Repeatable Configurations
    - Leveraged Elasticity
    - Leveraged auto scaling
    - Automated Testing
- **Continuous Integration**
  - is a software development practice where developers regularly merge their code changes into a central repository, after which automated builds and tests are run.
  - The key goals of continuous integration are to find and address bugs quicker, improve software quality, and reduce the time it takes to validate and release new software updates.
- **Continuous Delivery** code changes are automatically built, tested, and prepared for a release to production but not deployed
- **Continuous Deployment**
- **Monitoring**
  - Feedback comes from logs, monitoring, alerting and auditing infrastructure
- **Security**

# IAM

- Features
  - Shared access to your AWS account
  - Granular permissions
  - Secure access to AWS resources for applications that run on Amazon EC2

create user -> give user security credentials -> put user into one/more groups -> give user a login profile (optional)

- can auth several ways: passwords, key pairs, and X.509 certificates
- can enforce MFA on users who access AWS console or APIs

# Computer Networking

- 2 types: LAN, WAN made of multiple LANs
  - indirectly connect via switch or router
- Data transmission rate of a link is measured in bits/second
  
## 7-layer OSI Model:

1. Application Layer - HTTP, FTP, etc.
2. Presentation Layer - audio and video codes, different image formats such as PNG, JPEG, etc.
3. Session Layer - handles data related to particular user session
4. Transport Layer - TCP/UDP
5. Network Layer - IP
6. Data Link Layer - moving packet from one node to the next
7. Physical Layer - moveing the individual bits

### NAT

- allows sharing of one Internet-routable IP address of a NAT gateway for an entire private network
- allows ISPs to support more systems with the limited availability of public IPs
- does not work well with P2P as it requires 2 hosts to communicate directly
  
## Subnet
class A /8 8 bits for network prefix, 24 bits host address
class B /16
class C /24

## VPC

- allows you to create or configure:
  - firewall
  - routing table
  - public/private subnets
  - network gateway

## Elastic Network Interfaces

- is a virtual network interface that can include the following attributes:
1. a primary private IPv4 address
2. one or more secondary private IPv4 addresses
3. one Elastic IP address per private IPv4 address
4. one public IPv4 address, which can be auto-assigned to the network
interface for eth0 when you launch an instance
5. one or more IPv6 addresses
6. one or more security groups
7. a MAC address source/destination check flag
8. a description
- Each instance in your VPC has a default network interface, and we cannot detach a primary network interface from an instance
- You can create and attach an additional network interface to any instance in your VPC. The number of network interfaces you can attach varies by instance type

## Route table

- contains a set of rules, called routes, used to determine where network traffic is directed
- each subnet must be associated with a route table
  
## Elastic IP Address

- static IPv4 address designed for dynamic cloud computing
  
## Security Group

- a security group acts as a virtual firewall for your instance to control inbound and outbound traffic
- When you launch an instance in a VPC, you can assign up to five security groups to the instance
- act at the instance level, therefore, each instance in a subnet in your VPC could be assigned to a different set of security groups