
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
    * Capital - upfront
    * Operating - recurring
- **Organizational agility**

### Cloud Characteristics

1. On-demand self service
2. Broad Network Access
3. Resource Pooling (multitenancy)
4. Elasticity - scaling
5. Measured Service - pay only for the service consumed

### Cloud Delivery Models

- Iaas
- PaaS
- SaaS

### Cloud Deployment Models

1. Public cloud
2. Community cloud
   - similar to a public cloud except that its access is limited to a specific community of cloud consumers.
3. Private cloud
4. Hybrid cloud 

# DevOps

- term that focuses on collab between dev and it ops

## Challenges with Self Hosted Applications

- Cannot auto push updates, features and bug fixes until IT deploys
- low ROI due to infrastructure cost as its not elastic
- Bad UX

## Benefits of SaaS

- Better ROI
- less cost for muti-tenant SaaS
- multiple deployments
- Company manages the infrastructure

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
  
- 7-layer OSI Model:
1. Application Layer
2. Presentation Layer
3. Session Layer
4. Transport
5. Network
6. Data Link
7. Physical

Subnet
class A /8 8 bits network prefix 24 bits host address
class B /16
class C /24

