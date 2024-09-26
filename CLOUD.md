
# Cloud Computing

## Fundamentals of Cloud Computing

### Scaling

Scaling represents the ability of the resource to handle increased or decreased usage demands
- **Horizontal Scaling**
  - scaling in/out 
  - refers to adding more/less number of servers to distribute the workload
  - preferable for stateless 

- **Vertical Scaling**
  - scaling up/down 
  - performance by adding more resources (such as CPU, RAM, or storage) to a single machine
  - always involves downtime (has to be powered off to scale)
<br>

- **Q: Real-world scenario where vertical scaling is preferred**:

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

# Version Control with Git

## Local Version Control
- Revision Control System (RCS)
- Source Code Control System (SCCS)

## Centralized Version Control
- CVS
- SVN
- Perforce

## Distribution Version Control Systems
- Git
- Mercurial
- Bazaar
- Darcs

## Short History of Git
- Linux kernel project began using a proprietary DVCS called BitKeeper in 2002 but in 2005 the relationship broke down and no longer free
- Linus Torvalds created Git in 2005 to manage Linux kernel

## Git Has Integrity
- has integrity (checksum)
- use SHA-1 hash 40-char hex
```
// origin = alias for git repo !avoid for this course
git remote add alias <url>

//  show you which remote server you have configured
git remote -v

// download the data to local repo but does not merge
git fetch
```

# Twelve-factor App
> The twelve-factor app is a methodology for building software-as-a-service apps that:
> - Use **declarative** formats for setup automation
> - Have a **clean contract** with the underlying operating system, offering **maximum portability** between execution environments;
> - Are suitable for **deployment** on modern **cloud platforms**
> - **Minimize divergence** between development and production, enabling **continuous deployment** for maximum agility;
> - And can **scale up** without significant changes to tooling, architecture, or development practices.

## Code Base
is any single repo
- There is always a one-to-one correlation between the codebase and the app:
  - if there are multiple codebases: it's a `distributed system` not an app
  - Multiple apps sharing the same code is a violation of twelve-factor. The solution here is to factor shared code into libraries which can be included through the `dependency manager`.

## Dependencies

vendoring is important - upstreams can have issues but should not affect our build
- should explicitly declare and isolate dependencies (defining version of dependency)

## Config
Store config in the environment
everything that can be configured - leave them null 

## Backing Services
- Treat backing services as attached resources
- Any service the app consumes over the network as part of its normal operation. Examples include datastores (such as MySQL or CouchDB), messaging/queueing systems (such as RabbitMQ or Beanstalkd), SMTP services for outbound email (such as Postfix), and caching systems (such as Memcached)

## Build, release, run
- Strictly separate build and run stages
- A codebase is transformed into a (non-development) deploy through these three stages

## Processes
- Execute the app as one or more stateless processes, share-nothing
- Twelve-factor processes are stateless and share-nothing. Any data that needs to persist must be stored in a stateful backing service, typically a database.
- Some web systems rely on “sticky sessions” – that is, caching user session data in memory of the app’s process and expecting future requests from the same visitor to be routed to the same process.

## Port binding
- Export services via port binding
- The twelve-factor app is completely self-contained and does not rely on runtime injection of a webserver into the execution environment to create a web-facing service. The web app exports HTTP as a service by binding to a port, and listening to requests coming in on that port.
- use non standard port for dev env (1024 and below run with root user)

## Concurrency
- Scale out via the process model
- The twelve-factor app scales out by adding more `processes` rather than making existing ones more powerful.

## Disposability
- Maximize robustness with fast startup and graceful shutdown
- keep it simple
- The twelve-factor app’s processes are disposable, meaning they can be started or stopped at a moment’s notice. This facilitates fast elastic scaling, rapid deployment of code or config changes, and robustness of production deploys.

## Dev/prod parity
- Keep development, staging, and production as similar as possible
- multiple envs
- Make the tools gap small

## Logs
- Treat logs as event streams

## Admin processes
- Run admin/management tasks as one-off processes

# Testing

- Tests serves as good documentation
- Tests allow for safe refactoring
- Types
  > Unit testing > Integration testing > Functional Testing > Manual Testing
  - Unit Tests
    - should not require access to any external systems, using mocked data
    - allows testing in isolation
    - fast & reliable but takes time to build and requires maintenance
  - Integration Tests
    - verify that interaction between multiple component (applications, services, modules, etc.) is working as expected
      - Challenges
        - difficult to test all critical paths
        - hard to find the source of errors
        - requires time and commitment from multiple component owners
  - Performance/Load/Stress Testing
    - Simulate a heavy load on a server
    - Load testing is also a way to perform a `functional test` on websites, databases, LDAPs, webservices etc.
    - Load testing verifies the system’s behavior under expected user load, while stress testing evaluates performance under extreme conditions.
