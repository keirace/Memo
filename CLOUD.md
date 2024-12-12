
# Cloud Computing

- [Computer Networking](#Computer-Networking)
- [Linux](#linux)
- [Terraform](#Terraform)
- [Cloud Storage Solution](#Cloud-Storage-Options)
- [EBS](#EBS)
- [CDN](#content-delivery-network-cdn)
- [Security](#security)
  
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

## DevOps

- term that focuses on collab between dev and it ops

### The software development lifecycle (SDLC) & Challenges with Self Hosted Applications

- Cannot auto push updates, features and bug fixes until IT deploys
- Vendor and end-users are at mercy of IT team’s availability.
- low ROI due to infrastructure cost as its not elastic
- Bad UX

### Benefits of SaaS

- Better ROI
- less cost for muti-tenant SaaS
- multiple deployments a day
- Company manages the infrastructure

### Cloud
- low barrier to entry
- minimal capital
- no upfront capital expenses
- Validate ideas quickly at relatively low cost
- Scale with users
- Control your infrastructure costs

### Practices
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

## IAM

- Features
  - Shared access to your AWS account
  - Granular permissions
  - Secure access to AWS resources for applications that run on Amazon EC2

create user -> give user security credentials -> put user into one/more groups -> give user a login profile (optional)

- can auth several ways: passwords, key pairs, and X.509 certificates
- can enforce MFA on users who access AWS console or APIs

## Computer Networking

- 2 types: LAN, WAN made of multiple LANs
  - indirectly connect via switch or router
- Data transmission rate of a link is measured in bits/second
  
### 7-layer OSI Model:

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
  
### Subnet
- class A /8 fixed 0
  - 8 bits for network prefix, 24 bits host address
- class B /16 fixed 10
- class C /24 fixed 110 
	•	Class A: 126 networks, 16,777,214 usable hosts per network
	•	Class B: 16,384 networks, 65,534 usable hosts per network
	•	Class C: 2,097,152 networks, 254 usable hosts per network
> Q: 254 usable host addresses, reserving 1 for network and 1 for broadcast address

### VPC

- allows you to create or configure:
  - firewall
  - routing table
  - public/private subnets
  - network gateway

### Elastic Network Interfaces

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

### Route table

- contains a set of rules, called routes, used to determine where network traffic is directed
- each subnet must be associated with a route table
  
### Elastic IP Address

- static IPv4 address designed for dynamic cloud computing
  
### Security Group

- a security group acts as a virtual firewall for your instance to control inbound and outbound traffic
- When you launch an instance in a VPC, you can assign up to five security groups to the instance
- act at the instance level, therefore, each instance in a subnet in your VPC could be assigned to a different set of security groups

## Version Control with Git

### Local Version Control
- Revision Control System (RCS)
- Source Code Control System (SCCS)

### Centralized Version Control
- CVS
- SVN
- Perforce

### Distribution Version Control Systems
- Git
- Mercurial
- Bazaar
- Darcs

### Short History of Git
- Linux kernel project began using a proprietary DVCS called BitKeeper in 2002 but in 2005 the relationship broke down and no longer free
- Linus Torvalds created Git in 2005 to manage Linux kernel

### Git Has Integrity
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

## Twelve-factor App
> The twelve-factor app is a methodology for building software-as-a-service apps that:
> - Use **declarative** formats for setup automation
> - Have a **clean contract** with the underlying operating system, offering **maximum portability** between execution environments;
> - Are suitable for **deployment** on modern **cloud platforms**
> - **Minimize divergence** between development and production, enabling **continuous deployment** for maximum agility;
> - And can **scale up** without significant changes to tooling, architecture, or development practices.

### Code Base
is any single repo
- There is always a one-to-one correlation between the codebase and the app:
  - if there are multiple codebases: it's a `distributed system` not an app
  - Multiple apps sharing the same code is a violation of twelve-factor. The solution here is to factor shared code into libraries which can be included through the `dependency manager`.

### Dependencies

vendoring is important - upstreams can have issues but should not affect our build
- should explicitly declare and isolate dependencies (defining version of dependency)

### Config
Store config in the environment
everything that can be configured - leave them null 

### Backing Services
- Treat backing services as attached resources
- Any service the app consumes over the network as part of its normal operation. Examples include datastores (such as MySQL or CouchDB), messaging/queueing systems (such as RabbitMQ or Beanstalkd), SMTP services for outbound email (such as Postfix), and caching systems (such as Memcached)

### Build, release, run
- Strictly separate build and run stages
- A codebase is transformed into a (non-development) deploy through these three stages

### Processes
- Execute the app as one or more stateless processes, share-nothing
- Twelve-factor processes are stateless and share-nothing. Any data that needs to persist must be stored in a stateful backing service, typically a database.
- Some web systems rely on “sticky sessions” – that is, caching user session data in memory of the app’s process and expecting future requests from the same visitor to be routed to the same process.

### Port binding
- Export services via port binding
- The twelve-factor app is completely self-contained and does not rely on runtime injection of a webserver into the execution environment to create a web-facing service. The web app exports HTTP as a service by binding to a port, and listening to requests coming in on that port.
- use non standard port for dev env (1023 and below run with root user)

### Concurrency
- Scale out via the process model
- The twelve-factor app scales out by adding more `processes` rather than making existing ones more powerful.

### Disposability
- Maximize robustness with fast startup and graceful shutdown
- keep it simple
- The twelve-factor app’s processes are disposable, meaning they can be started or stopped at a moment’s notice. This facilitates fast elastic scaling, rapid deployment of code or config changes, and robustness of production deploys.

### Dev/prod parity
- Keep development, staging, and production as similar as possible
- multiple envs
- Make the tools gap small

### Logs
- Treat logs as event streams

### Admin processes
- Run admin/management tasks as one-off processes

## Testing

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

> Q: Reserved ports are `0-1023`

## Linux

- Kernel = operating system
- No file extensions
- **Components of OS**
  - The Bootloader
  - The kernel
  - Daemons = background services
  - Desktop Env
  - Applications
  - The shell
mac is using z shell

dir
- /bin
- /boot - don't touch
- **/dev** - device, generated at boot time/on the fly
- /etc
- /home - personal dir
- /lib - code that applications use
- /media - external storage, mounted when plug in and try to access
- /mnt - not used often nowadays
- /opt - can install apps, where software compiles
- **/proc** - in memory dir, info about computer, generated at boot time/on the fly
- /root - aka admin, don't touch
- /run - don't touch
- /sbin - contains apps that only superuser will need
- /usr - stuffs that need to be shared by apps and services
- /srv - servers
- **/sys** - virtual dir
- /tmp - can interact without becoming superuser
- /var - logs @ /var/log

### Some commands

- The **redirection operator** `>` connects to a file while **pipeline operator** `|` connects the output of one command with input of a 2nd command
- Permission `rwx` = read write execute
  - owner group world 
- `&` puts a process in the background
- `du -sm` estimate file space usage in megabytes
- `df -m` report file system disk usage
- Zombie process 
  - completed execution but still has entry = Terminated state
  - occurs for child processes
```
# Viewing process
ps -ef | grep cron

# runs program in background, adding & to immediately place it in bg
# nohub - run programs in bg after logging off
nohub 60 &

# returning a process to the foreground
fg <job_id>

# kill a process that refuses to be killed
kill -9

# kill everything
kill -9 -1 

# Disk Usage
# summary of the disk usage for a specific directory
du -sh .

# Disk usage in human-readable format
du -h

# Disk Free: overall file system usage
df -m file system disk usage

apt update & upgrade

scp -i key_path file_path root@ip_address:/dest_path

# checking if the file exists
which <file>

# change owner and group
chown root:newgroup file.txt

# viewing process dynamically
top

# reboot
sudo shutdown –r now

# zombie process
ps aux | grep 'Z'
```

vi
```
ctrl f page up
ctrl b page down
number G go to page
G last page
/g global search
```

## Shell Scripts

- Shell scripts and functions are both interpreted. Not compiled.
- Shell scripts and functions are `ASCII` read by shell command interpreter
- Case Sensitive
- `#!` @ first line indicates an interpreter for execution under unix/linux
  - `#!/bin/bash`
- `if [ condition ]`
- the trap command captures an interrupt (signal) and then clean it up within the script
- echo `$varName` or echo `${varName}`

- average time in last 5 mins
- Exit status
  - 0 exit status means the command was successful without any errors
  - A non-zero (1-255 values) exit status means command was failure
  - Use shell variable `?` to get the exit status of the *previously* executed command

### CI
> practice of merging all developer working copies to a shared mainline several times a day.
> runs unit tests for every commit
- benefits
  - catches bugs early, reduce the time to deliver
  - improve the quality
- **Continuous delivery** -> manual deployment to prod
  - Automate: repeatable build, deploy, test and release
  - Frequent: delta between releases will be small, reduces the risk associated with releasing
- **Continuous deployment** -> auto deployment

mvp = minimum viable product eg api only

### Github Actions
> help automate tasks within software development life cycle
> event-driven
- **Workflows** - automated procedure inside a repo
- **Events** - triggers a workflow
```
on: [push]
```
- **Jobs** - execute on the same runner (vm), can be run in parallel (default) or sequentially
  - A workflow can have two sequential jobs that build and test code, where the test job is dependent on the status of the build job. If the build job fails, the test job will not run.
```
jobs:
```
- **Steps** - individual task that can run commands in a job
  - action or shell command
```
steps:
```
- **Actions** - standalone commands that are combined into steps to create a job
  - smallest portable building block of a workflow
  - To use an action in a workflow, you must include it as a step
```
uses: actions/checkout@v2
```
- **Runners** - is a server that has the GitHub Actions runner application installed
```
runs-on: ubuntu-latest
```
  - can use a runner hosted by GitHub, or you can host your own
- github actions uses YAML files stored in a dir `.github/workflows` inside repo
- secrets are limited to `64kb` in size

### Infrastructure as Code

- Challenges with Dynamic Inrfastructure
  - Server Sprawl - the number of servers growing faster than the ability of the team to manage
  - Configuration Drift - inconsistency across the servers
  - Snowflake servers - special servers, cannot autoscale, replicated
  - Fragile infrastructure - easily disrupted, not easily fixed, snowflake server problem
- Principles
  - Systems Can Be Easily Reproduced
  - Systems Are Disposable
  - CATTLE, NOT PETS
  - Systems Are Consistent
  - Processes Are Repeatable
  - Design Is Always Changing
- Stack - a collection of infrastructure elements that are defined as a unit, can be any size 
- Environment - multiple stacks
- What NOT to Manage in a VCS
  - Software artifacts should be stored in a repository
  - Software and other artifacts that are built from elements already in the VCS
  - Data managed by applications, logfiles
  - Passwords and other security secrets

## Terraform
> The main purpose of the Terraform language is declaring resources
> A group of resources can be gathered into a module, which creates a larger unit of configuration
> A resource describes a single infrastructure object
> A module might describe a set of objects and the relationships between them in order to create a higher-level system
> A Terraform configuration consists of a root module, where evaluation begins, along with a tree of child modules created when one module calls another

- Terraform State
  - This state is stored by default in a local file named "terraform.tfstate"
- install with brew
```
brew tap hashicorp/tap
brew install hashicorp/tap/terraform
```
- writes in HCL lang with extension `.tf`
- `terraform plan` - allows user to review changes -> refreshes the state -> might take too long
- `terraform apply`
- `terraform state`
- `terraform destroy`

## Virtualization

### Virtual Machine
> a tightly isolated software container
- each self-contained vm is completely independent
- multiple VMs on a single computer enables OS and apps to run on just 1 physical server (host)
  
### Hypervisor 
> a software decouples VMs from the host and dynamically allocates computing resources to each vm

### Key properties of VMs
  - **Partitioning**
    - run multiple OS on 1 physical machine
    - divide system resources between VMs
  - **Isolation**
    - provide fault and security isolation at the hardware level
    - preserve performance with advanced resource controls
  - **Encapsulation**
    - save the entire state of a VM to files
    - move and copy VM easily
  - **Hardware Independence**
    - provision or migrate any VM to any physical server

### Server Consolidation 
> Using server virtualization, a company can maximize the use of its server resources and reduce the number of servers required
> vulnerable to failure but improves efficiency and cuts costs

### Virtualization != Cloud 
- can do cloud using virtualization
- cloud computing describes the delivery of shared computing resources on demand thru the internet
- we can start virtualizing servers with/without cloud

### EC2
- Types
  - General Purpose
  - Compute Optimized
  - Memory Optimized
  - Accelerated Computing (GPU)
  - Storage Optimized
- Pricing Model
  - On-Demand - pay by hour
  - Spot Instances - bid unused instances
  - Reserved Instances - assigned to a specific avail zone
    - steady usage
    - 1 or 3 year term
  - Dedicated Hosts
  - Dedicated Instances
- Dedicated Instances - EC3 that run in a VPC on hardware that's dedicated to a single customer
- Dedicated Hosts - physical EC2 server

#### AMI (Amazon Machine Images)
- provides the information required to launch an EC2 instance
- can launch multiple instances from a single AMI

#### EBS
- block level storage
- data must be quickly accessible

### GCE
- Types
  - General Purpose
  - Compute Optimized
  - Memory Optimized
  - Accelerator-optimized

- Pricing Model
  - on-demand
  - spot
  - reserved
  - dedicated hosts
  - dedicated instances
- **AMI**
  - Provides the information required to launch an EC2 instance
- Amazon EBS - Elastic Block Store
  - attached to EC2 instance
  - recommended when data must be quickly accessible
- Image - Immutable  - 

### Custom Image
- **Golden Images** - secure, immutable OS images
- **Environment Parity** - Keep all dev/test/prod environment as similar as possible
- **Auto-scaling Acceleration** - Launch completely provisioned and configured instances in seconds,

### IOPS 
- are a unit of measure representing input/output operations per
second
- capped at 256 KiB for SSD and and 1024 KiB for HDD
- A single 1,024 KiB I/O operation counts as 4 operations (1,024÷256=4), while 8 contiguous I/O operations at 32 KiB each count as 1 operation (8×32=256). However, 8 random I/O operations at 32 KiB each count as 8 operations. Each I/O operation under 32 KiB counts as 1 operation.

### Security Group
- acts as a virtual firewall
- associate one or more security groups with the instance

### Instance metadata and user data
- Instance metadata is data about your instance
- can use instance metadata to access user data that's specified when launching


## Cloud Storage Options
- [Block-level Storage](Block-level-Storage)
- [Object Storage Service](Object-Storage-Service)
- [Relationnal Databases](Relational-Databases)
- [NoSQL Databases](NoSQL-Databases)

### Block-level Storage (EBS)
- Block-level storage with a disk file system (FAT32, NTFS, ext3, ext4, XFS, and so on) can be used to store files as you do on a personal computer
- A block is a sequence of bytes and the smallest addressable unit
- The disk file system manages where files are persisted on the underlying block-level storage (block address)
- can use block-level storage only in combination with a VM (EC2) instance where the OS runs

#### Why do we need EBS?
- for persistence for apps like DB
- MySQL uses system calls to access files so it can't store its files in an object store

#### Block-level Storage on AWS
1. Network Attached Storage (NAS) via EBS service
2. Instance Storage

#### Use Cases
- databases, data warehousing, big data applications
- apps that demand the highest IOPS or throughput and low latency with consistent, predictable performance

#### EBS Lifetime
- not part of EC2 instances
- attached to EC2 via a network connection
- attached to 0 or 1 EC2 at a time

#### Availability
- high avail, auto replicated within its availability zone (cannot be outside of its AZ)

#### Snapshots
- saved to Amazon S3
- stored incrementally: only the blocks that have changed are saved

#### Encryption
- provides seamless support for data-at-rest and data-in-transit between EC2 instances and EBS volumes

### Instance Store
- `temporary` block-level storage
- ideal for temporary storage of information that changes frequently such as `buffers, caches, scratch data` or data that is replicated across a fleet of instances such as a `load-balanced pool of web servers`
- located on disks that are physically attached to the host computer
- consists of 1 or more instance store volumes exposed as block devices
- size of an instance varies by instance type
- the virtual devices for instance store volumes are `ephemeral[0-23]`
- type that supports 1 instance store volume have `ephemeral0`
- type that supports 2 instance store volumes have `ephemeral0` and `ephemeral1`, and so on

#### Use Cases
- caching
- temporary processing
- applications that replicate data to several servers

#### Lifetime
- persists only during the lifetime of its associated instance
- data in the store persists if an instance reboots
- data lost in the following circumstances:
  - disk drive fails
  - instance stops
  - instance termination

#### Cost
- included in the EC2 instance price, no additional charge

#### Encryption
- No out of the box solution for data at rest

Instance store backed volume cannot be “stopped”. They can only be rebooted or terminated

### EFS
- cannot be the root volume
- supports NFSv4 and 4.1 making it easy to migrate enterprise apps to AWS
- can be in multi AZ
- highly avail and durable
- designed to meet the needs of multi-threaded
applications and applications that concurrently access data from
multiple EC2 instances and that require substantial levels of aggregate throughput and input/output operations per second (IOPS)

#### EFS Use Case
- Big Data and analytics
- Media processing workflows
- Content management
- Web serving
- Home directories

### Object Storage Service
- Each object consists of a globally unique identifier, some metadata and data

### S3 (Simple Storage Service)
- unlimited storage space
- highly available and durable
- object can be 5TB or less
- access with RESTful APIs
- strongly consistent

### Tiers/Classes
- **S3 (standard)** - hight avail & dura stored redundantly
- **S3 - IA** - For data that is accessed less frequently but requires rapid access when needed
- **Reduced Redundancy Storage** - hight avail & dura over a given year
- **Glacier** - Archival only, 3-5 hrs to retrieve

### S3 Use Cases
- ranging from simple storage repository for backup & recovery to primary storage for some of the most cutting-edge cloud-native applications in the market today and everything in between.

### S3 Buckets
- every object resides in a bucket
- unique names for diff REST endpoints
- globally unique name

#### Event Notifications
- created event
- removed event
- reduced redundancy storage object lost event
revenue - cost

#### Bucket Versioning
- By default, S3 versioning is disabled for every bucket
- A versioning-enabled bucket can have multiple versions of objects in the bucket

#### Data Lifecycle Management
- rules allow you to define actions you want amazon s3 to take during an object's lifetime such as:
  - transition objects to another storage class
  - archive objects
  - delete objects after a specified period of time

####  Object Tagging
- S3 object tags are key-value pairs 
- can create IAM policies, setup S3 lifecycle policies, and customize storage metrics
- these tags can manage transitions between storage classes and expire objects in the background

#### Encryption
- **SSE-S3** S3 will encrypt data at rest and manage the encryption keys
- **SSE-C (Customer-Provided keys)** encrypt data at rest with custom encryption keys
- **SSE-KMS** encrypt data at rest with keys in AWS Key management service

#### Cross-region replication
- auto, async copying of objects across buckets in diff AWS regions

#### Querying S3
- doesn’t offer query capabilities to retrieve specific obj
- need to know the exact `bucket name` and `key`
- can't be used as a db or search engine by itself
- can be paired with DynamoDB, Cloudsearch, RDS to index and query metadata about S3 buckets and objects

#### Not suited for file system
- flat namespace - use EFS instead

### Relational Database (RDBMS)

#### Transactions
- RDBMS must support **ACID** transactions to operate efficiently
  - Atomicity
    - all or nothing
  - Consitency
    - take from 1 state to another
  - Isolation
    - ensures that concurrent execution results in sequential
  - Durability
    - transaction/result stored permanently -> able to provide a given time and restore
log file = async

#### Backups of AWS RDS
- the restored version of the database will be a `new RDS instance` with a `new endpoint`
- 2 types
  - **automated backups**
    - take a full daily snapshot
    - enabled by default
    - stored in S3 but free
    - during backup window, might experience higher latency as storage I/O may be suspended
    - deleted when the RDS instance is deleted
  - **database snapshots**
    - manual
    - stored even after the original RDS instance deletion

#### RDS Multi-AZ Deployments
- When provisioning a multi-AZ DB instance, Amazon RDS auto creates a **primay DB instance** and synchronously replicates the data to a **standby instance in a different AZ**
- RDS performs an auto failover to the standby in case of infrastructure failure, can resume as soon as the failover is complete and using the same endpoint

#### RDS Read Replicas
- enhance performance and durability for db instances
- easy to elastically scale out beyond the capacity constraints of a single DB instance for read-heavy db workloads
- can create 1 or more replicas

> vertical scaling for persistent storage system

### NoSQL
- schema-less
- runs well on cluster
- most NoSQLs lack true ACID transactions
- Scaled out horizontally (linearly) by adding more processors

#### Value of Relation Database
- store large amounts of persistent data
- concurrency
- standard model
- ACID

#### Not good side of RDBMS
- **Impedance mismatch** - diff between relational model and in-mem data structure
- mediocre **horizontal** scaling support

#### Storing and retrieving data
- key-value (DynamoDB)
- graph
- column-family (Cassandra) 
  - think of spreadsheets
- document (MongoDB)

### CAP Theorem (FINAL)
> it is impossible for a distributed computer system to simultaneously provide more than two out of three of the following guarantees:
- **Consistency** - Every read receives the most recent write or an error
- **Availability** - Every request receives a (non-error) response – without guarantee that it contains the most recent write
- **Partition tolerance** - The system continues to operate despite an arbitrary number of messages being dropped (or delayed) by the network between nodes

#### Most NoSQL stores lack true ACID transactions

#### NoSQL Databases & Consistency
- NoSQL db offer "Eventual Consistency" in which changes are propagated to all nodes 'eventually'
- queries for data might not return updated data immediately or might result in reading data that is not accurate, a problem known as **stale reads**

#### Polyglot Persistence
- choosing the right persistence option for task at hand

#### Concurrency Control Mechanisms
- Optimistic - delay the checking
- Pessimistic - block an operation of a transaction

#### Write-Write Conflict

#### Read-Write Conflict

#### Version Stamps
- A field that changes every time the underlying data in the record changes

#### Single Server (Distribution Model)
- One machine handles all reads and writes to the database

#### Sharding (Distribution Model)
- data is partitioned across different nodes

#### Primary/Secondary Nodes Replication (Distribution Model)
- replicate data across multiple nodes

#### Peer-to-Peer Replication (Distribution Model)
- no master node in peer-to-peer replication

## Normalization & Denormalization
### Database Normalization
> relational db designing technique to ensure that data is optimal for ad-hoc querying

### Database Denormalization
> process of optimizing database by creating redundant data but could cause inconsistency

### Polyglot persistence
> choose the right persistence option

### Concurrency Control Mechanisms

## Email Service

- **Bounce**
  - fails to deliver
  - can be sync/async
  - Types:
    - **Hard Bounce** - persistent
    - **Soft Bounce** - temp
- Amazon SES supports two methods of authentication
  - Sender Policy Framework (SPF)
    - indicates to ISPs that you have authorized a service
  - DomainKeys Identified Mail (DKIM)
    - a standard that allows sending with cryptographic key

## Domain Name System
- decentralized system, maintain locally, cacheable

### Loose Coherency
### Scalability
### Reliability
### Dynamicity

### DNS Components
- Name space (TLDs)
- Name Servers
- Resolvers

### Name Space
- structure of the DNS db
- each node has a label
- root node has a **null** label

### Labels
- case-insensitive, string up to 63 bytes
- each node must have a label

### Domain Names
  - Top-Level Domains (TLDs)
    - **gTLDs** - generic
    - **ccTLDs** - country code 2 letters, 312 in active
  - N-level Domains - max depths of 127 levels
  - Subdomain eg. `coe` .northeastern

### Types of Name Servers
- Authoritative - maintains the data
- caching - stores data obtained from autho servers

### Zones
- Zone delegation

### SOA record *
- start of authority
- stores important information about a domain or zone such as the email address of the administrator
- negative TTL = record doesn't exist
- suggestion - drop TTL to 1-5 mins

### A Record (address)
- IP address

### AAAA Record
- IPv6 address

### CNAME Record
- canonical name is used in lieu of an A record
- records points to a domain

### MX Record
- mail exchange

### TXT Record
- lets a domain administrator enter text into the Domain Name System (DNS)
- USES: email spam prevention and domain ownership verification

### NS Record
- tells the internet where to go find out a domain's IP address
- typically has multiple records for backup

### CAA Record
- certification authority authorization
- if no record, anyone can issue a cert

```
dig +trace @8.8.8.8 
```

## Site Reliability Engineering (SRE)
- discipline that incorporates aspects of SE and applies to operations
- Automation

### Error Budget
- A service that’s 99.99% available is 0.01% unavailable. That permitted 0.01% unavailability is the service’s **error budget**

#### Measuring Service Risk
- way of representing risk tolerance is in terms of the acceptable level of unplanned downtime

#### Time-based availability
$$ availability = uptime / (uptime + downtime) $$

### Service Level Objectives - Terminology
service level indicator
service level objective - put a boundary for incoming API calls
Service Level Agreements (SLAs) - contracts between customers and service providers

### Collecting Indicators


## Log
- For the standard levels, we have ALL < TRACE < DEBUG < INFO < WARN < ERROR < FATAL < OFF.

### Production
- priority should not be lower that INFO

### Metrics
#### Data Source Types
- Counters
- Gauge
- Timers

### Alerting
- Level
  - Low Severity
  - Moderate Severity - email notification
  - High Severity - requires human intervention right away


## Content Delivery Network (CDN)
### Benefits
- Improving website load times (latency)
- Reducing bandwidth costs
- Increasing content availability and redundancy - non static?
- Improving website security, protect against DDoS (Distributed Denial of Service)

### Use Cases
- Static Asset Caching
- Video Streaming
- Software Distribution
- Security and DDOS Protection
- API Acceleration

### Origin Server
- server that processes and responses incoming requests
- data that's not not cached

### Edge Server
- caching and validation near users
- cannot do authentication

### Anycast protocol
- find the server closest to the user and send requests there

point of exchange

### Negative Caching
- is a technique used to improve the performance of a web application by caching the results of a request that returns error
- set different TTL for each status code

## Load Balancing, Auto Scaling & Availability Zones
### Regions
- static

### Zones
- deployment area within a region
- different zones provider has different definition
- most have 2 zones at launch time
- consisted of 1 or more discrete data center

### Load Balancer (final)
> device that acts as a reverse proxy and distributes network or application traffic across a number of servers
> has health checks, traffic can be routed away from unhealthy servers
> served as a single point of entry for all incoming traffic

#### Features
- Asymmetric load
- Distributed Denial of Service (DDoS) attack protection
- HTTP compression 

#### Request Distribution
- layer 4 Transport (IP, TCP, FTP, UDP) or 7 Application load balancing
- Standard algorithms:
  - Round Robin - equal shares but can overload instances
  - Weighted round robin
  - Least connections
  - Least response time

#### Classic Load Balancer
- sits in VPC

- have to configure the listener

#### Internal Classic Load Balancers
- The DNS name of an internal load balancer is publicly resolvable to the private IP addressed of the nodes
- can only routes requests from clients with access to the load balancer's VPC

#### AWS Classic Load Balancer Features
- sticky session binds users to a specific instance
- not all load balancers tells where the requests are coming from; need real IPs
  
### Application Load Balancer
- handle HTTP/HTTPS requests

#### Network Load Balancer
- TCP/UDP traffic

### Autoscaling
- stateless 

### Scaling Policies
- Manual Scaling
- Scheduled Scaling
- Dynamic Scaling - scale up/down based on params eg. number of users

Scale out = adding more instances

### Scaling Cooldown
- cooldown period = configurable setting for auto scaling
- not supported for scheduled scaling

## Microservices
breaks monolitic into microservices to easily manage small teams
autonomous
higher cost - multiple instances
servies exposed an API
isolated services

### Good service
- Loose Coupling - a change to one not require change to another
- High Cohesion- related behavior sit together

### Benefits
- **Technology Heterogeneity** - can choose any language, framework, os
- **Resiliency** – A service failure does not cascade into total system failure
- **Scaling** – Scale on the services that need to be scaled
- **Ease of Deployment**
- **Composability**
- **Optimizing for Replaceability**

## Event-driven Architecture
### Pub/Sub
> async and scalable messaging service
> broadcasting events

#### Types
- Pub/Sub service
  - synchronous replication to at least 2 zones
- Pub/Sub Lite service
  - lower cost, lower reliability 
  - offers zonal/regional storage
  - zonal stores in only 1 zone, regional replicate to 2nd zone asynchronously

#### Components
- Publisher (Producer) - generate the event and put in the queue
- Message
- Topic - represents a feed of messages
- Schema - data format, generally no schema, text by default
- Subscription
- Subscriber (Consumer) - has to subscribe to be notified

#### Status
- Acknowledged messages (acked)
- Unacknownledged messages (unacked)
- Negatively acknowledged messages (nacked) causes pub/sub to redeliver it immediately

#### publish and subscribe pattern
- fan in (many to one)
  - multiple `publisher applications` publish to a single `topic`
- fan out (one to many)
  - a single/multiple `publisher apps` publish to a single `topic` wherein the topic is attached to multiple `substriptions`. each subscription is connected to a <ins>single</ins> `subcriber app`.
- load balanced (many to many)
  - multiple `publisher apps` publish to a single topic. This topic is attached to a `single subscription` of which connected to <ins>multiple</ins> `subscriber apps`.

### Amazon Simple Notification Service (SNS)
#### Common scenearios
- Application and system alerts
- Push email and text messaging
- mobile push notifications
- message durability 
  - Amazon SNS porvides durable storage of all messages. It stores mulitple copies of message to disk in multiple AZs.

### Amazon Simple Queue Service (SQS)
- Standard Queues
  - Unlimited Throughput
    - nearly unlimited number of transactions per second (TPS) per API action
  - At-least-once delivery
    - occasionally more than one copy of a message is delivered
  - Best-effort ordering
    - messages might be delivered in an order different from which they were sent
- FIFO Queues
  - High Throughput
    - by default, FIFO queue supports <= 300 msg/s
  - Exactly-once processing
    - deliver once and remain until a consumer processes and deletes it.
  - First-in-first-out delivery
    - the order is strictly preserved

## Serverless Computing
> known as function as a service (FaaS)
> Reactive computing design

### Benefits
- No servers to manage
- Continuous scaling
- Never pay for idle servers
- Reduced operational costs

### Drawbacks
- Loss of Server optimizations
- No in-server state for Serverless FaaS
- Startup Latency
- Vendor Lockin

### Units of Scale
- **Virtual Machines**
  - machine as the unit of scale
  - abstracts the hardware
- **Containers**
  - application as the unit of scale
  - abstract the OS
- **Serverless**
  - functions as the unit of scale
  - abstract the language runtime

### Use Cases
- Event driven programming
- scheduled events
- on-demand lambda function invocation

### AWS Lambda

## Docker
runtime = linux
### Dockerfile
- execution steps
  - LABEL
  - ADD = copy files from local to docker
  - ENV
  - EXPOSE = does not actually publish the port
  - CMD provide defaults for an executing container. there can be only 1 CMD.
  - ENTRYPOINT parse args at runtime?

## Security
- Terms
  - **Confidentiality** only authorized
  - **Integrity** guarantee the same data
  - **Authenticity** authorized source
  - **Availibility** accessible 24/7
  - **Threat**
  - **Vulnerability**
  - **Attack Vectors** path or means by which a hacker can gain access to a computer or network server to deliver a payload or malicious outcome
  - **Risk**
  - **Security Controls**
  - **Threat agent** entity that poses a threat
  
- Types of cert
  - extended validation cert - seen in banking website
  - domain validation cert - typical one

`bcrypt` - generate a salt for each entry, has hashing round

### Cloud Security Threats
- Traffic Eavesdropping - wireshark
- Malicious Intermediary - man in the middle
- Insufficient Authorization - attacker gaining direct access to IT resources that were implemented under the assumption that they would only be accessed by trusted consumer programs
- Denial of services (DoS) - overload the resources for ransom
- Flawed implementations 

### Security Mechanisms
- Encryption
  - Symmetric same key
  - Asymmetric private and public key
- Web-based data transmission
  - SSL/TLS TLS uses asymmetric encryption (slower) only for its `key exchange`, then switches to symmetric
  - Most TLS supports **RSA** as the main asym encryption cipher, while **Triple-DES** and **AES** are supported for sym
- Hashing one way, Git uses SHA-1, Recipient applies the same hash function to the message to verify that the produced message digest is identical to the one that accompanied the message
- Digital Signature privides data auth and integrity
  - a message is assigned a digital signature prior to transmission, which is then rendered invalid if the message experiences any subsequent, unauthorized modications
  - both **hashing** and **asymmetrical encryption** are involved in the creation of a digital signature, which essentially exists as a message digest that was encrypted by a private key and appended to the original message
  - The recipient verifies the signature validity and uses the corresponding public key to decrypt the digital signature, which produces the message digest
  - The hashing mechanism can also be applied to the original message to produce this message digest
- Hardened Server Images stripping unnecessary software from a system to limit potential vulnerabilities that can be exploited by attackers
  - removing redundant programs, closing unecessary server ports, and disabling unused services, internal root accounts, and guest access are all hardening
- User Input: Users can submit arbitrary input, the application must assume that all input is potentially malicious
  - users can interfere with any piece of data transmited between the client and the server, including request params, cookies, and HTTP headers
- Attack Vectors
  - the majority of attacks against web applications involve sending crafted input to the server to cause some event that was not expected by the app's designer

### Core Defense Mechanisms
- Authentication
- Session Management 
  - issuing the user a token that identifies the session
  - in terms of attack surface, the session management mech is highly dependent on the security of its tokens, and the majority of attacks against it seek to compromise the tokens issued to other users
- Access Control
  - an application might support numerous different user roles 
  - because of the complex nature of typical access control requirements, this mech is a frequent source of security vulnerabilities that enable an attacker to gain unauthorized access to data and functionality
- Handling User Input

### Handling Hackers
- Mapping the application
- Bypassing client side controls
- Attacking authentication
- Code injection into interpreted languages
- Injecting code in SQL
- Cross-site scripting (XSS) enables attackers to inject client-side scripts into web pages viewed by other users
  - may be used by attackers to bypass access controls such as same-origin policy
- Cross-site request forgery (CSRF) forces end user to execute unwanted actions on a web application in which they're currently authenticated
  - specifically targets state-changing requests, not theft of data, since the attacker has no way to see the reponse to the forged request

a password has to be hashed with salt, each entry must be unique

SQL injection = #1 attack
Cross-site scripting - eg. using iframe to put a mimicking site to record creds

## Architecturing for the cloud
### Lift & Shift
- moving an application to the cloud without making any changes to the application itself
- the application is simply moved from one environment to another, with the same architecture and configuration

### On-premises vs Cloud
cloud computing differs from a traditional on-premises environment in several key ways
- **global and scalability**: cloud computing allows for the rapid scaling of resources to meet changing demands, whereas
- **options for cost optimization**: cloud computing offers a variety of pricing models and options for cost optimization, such as reserved instances and spot
- **built-in security**: cloud computing provides a range of built-in security features, such as encryption, firewalls, and access
- **flexible**: cloud computing allows for the use of a variety of different services and tools, whereas on-premises
- **managed services**
- **various operating models**

### IT Assets as Provisioned Resources
- In a traditional computing environment, capacity are provisioned based on an estimate of a theoretical maximum peak. This can result in periods where expensive resources are sitting idle or occasions of insufficient capacity to meet demand.
- With cloud computing, resources are provisioned on demand, and the cost is only incurred when the resources are actually being used. Components can be instantiated within seconds. You can treat these as temporary resources, and they can be scaled up or down as needed. Introducing the ability to fail fast and iterate quickly.

### Global, Available and scalable capacity
- for global applications, you can reduce latency to end users around the world by using Content Delivery Networks (CDNs).

### Architecturing for cost
- when provisioning cloud computing environment, <ins>optimizing for cost</ins> is a <ins>fundamental design</ins> tenant for architects
- when selecting a solution, you should not only focus on the <ins>functional architecture</ins> and feature set, <ins>but on the cost profile</ins> of the solutions you select


### Scalability
- <ins>scale in a linear manner</ins> when <ins>adding extra resources results</ins> in at least a <ins>proportional increase in ability to serve additional load</ins>
- there are 2 ways to scale: <ins>horizontal scaling</ins> (add more servers) and <ins>vertical

### Scaling Vertically
- can eventually reach a limit, and it is not always a cost-efficient or highly available approach
- Very easy to implement and can be sufficient for many use cases in the short term

### Scaling Horizontally
- a great way to build internet-scale applications that leverage the elasticity of cloud computing.
- not all architectures are designed to distribute their workload to multiple resources

### Stateless Application
- when user interact with application, they will often perform a series of interactions that form a session
- a session is unique data for users that persists between requests while they are interacting with the application
- stateless applications can scale horizontally because of any available resource can service any request
- those services do not need to be aware of the presence of their peers - all that is required is a way to distribute the workload to them

### Distribute load to multiple nodes
- to distribute load to multiple nodes in your environment, you can choose either a <ins>push or pull</ins> model
- with a <ins>push</ins> model, you can use elastic load balancing (ELB) to distribute a workload. ELB routes incoming application requests across multiple EC2 instances.
- alternatively, you can use <ins>Amazon Route 53<ins> to implement a <ins>DNS round robin</ins> distribute traffic across multiple nodes. In this case, DNS responses return the IP addresses of multiple nodes, and the client can choose which node to use.
- dont use RDS, if you use a very dynamic auto scaling group, DNS can change very quickly

### Stateless components
- store session is database or external cache
- store files in Object Storage (S3) or a distributed file system (EFS)

### Stateful components
- databases are stateful. In addition, many legacy applications were designed to run on a single server by relying on local compute resources. 
- Other use cases might require client devices to maintain a connection to a server for extended periods of time. For example, real-time multiplayer gaming must offer multiple players a consistent view of the game world with very low latency.
- You might still be able to scale those components horizontally by distributing the load to multiple nodes with <ins>session affinity</ins>. In this model, you bind all the transactions of a session to a specific compute resource. But this model does have some limitation, existing session do not directly benefit from the newly launched compute nodes. More importantly, session affinity cannot be guaranteed, if the compute node that is handling a session fails, the session will be lost.

### Implement Session Affinity
- For HTTP and HTTPS traffic, you can use the sticky sessions feature of an Application Load Balancer to bind a user’s session to a specific instance
- With this feature, an Application Load Balancer will try to use the same server for that user for the duration of the session

### Distributed Processing
- Use cases: the processing of very large amounts of data
- Devide the data into smaller chunks and process them in parallel

### Disposable Resources Instead of Fixed Servers
- Another issue with fixed, long-running servers is <ins>configuration drift</ins>. Changes and software patches applied through time can result in untested and heterogeneous configurations across different environments. You can solve this issue with <ins>immutable infrastructure</ins>. Immutable infrastructure is a design principle that ensures that the configuration of a server is fixed and unchangeable. This is achieved by creating a new server image for each change, and then using that image to launch a new server. The old server is then terminated. This enables resources to always be in a consistent (and tested) state and makes rollbacks easier to perform. This is more easily supported with stateless architecture.

### Bootstrapping
- You can set up new EC2 instances with user <ins>data scripts</ins> and <ins>cloud-init directives</ins>
- When you launch an AWS resource such as an EC2 instance or Amazon Relational Database Service (Amazon RDS) DB instance, you start with a default configuration.
- You can then execute automated bootstrapping actions, which are scripts that install software or copy data to bring that resource to a particular state
- You can parameterize configuration details that vary between different environments (such as production or test) so that you can reuse the same scripts without modifications

### Golden Images
- Certain AWS resource types, such as EC2 instances, Amazon RDS DB instances, and Amazon Elastic Block Store (Amazon EBS) volumes, can be launched from a golden image, which is a snapshot of a particular state of that resource.
- When compared to the bootstrapping approach, a golden image results in faster start times and removes dependencies 

### Hybrid
- You can also use a combination of the two approaches: some parts of the configuration are captured in a golden image, while others are configured dynamically through a bootstrapping action

### Service Discovery
- Service discovery is the process of finding and accessing services in a distributed system
- For an Amazon EC2-hosted service, a simple way to achieve service discovery is through <ins>ELB</ins> because each load balancer gets its own hostname, you can consume a service through a stable endpoint. This can be combined with DNS and private Amazon route 53 zones, so that the particular load balancer's endpoint can be consumed at any time.
- Another option is to use <ins>service registration and discovery method</ins> to allow retrieval of the endpoint IP addressed and port number of any service.
- if load balancers are not used, service discovery should also allow options such as health checks. Amazon Route 53 supports auto naming to make it easier to provision instances for microservices. Auto naming lets you create DNS records based on a configuration you define.

### Asynchronous Integration
- another form of loose coupling between services
- It involves one component that generates events and another that consumes them
- The two components do not integrate through direct point-to-point interaction but usually through an intermediate durable storage layer, such as a queue or a streaming data platform

### Databases
- it is not uncommon for applications to run on top of a polyglot data layer on cloud, choosing the best database for each specific use case

### Database Scalability
- <ins>Read replicas</ins> are separate database instances that are <ins>replicated asynchronously</ins>. As a result, they are subject to <ins>replication lag</ins> and might be missing some of the latest transactions.
- For read-heavy applications, you can also horizontally scale beyond the capacity constraints of a single db instance by creating one or more read replicas.
- Read replicas can not accept any write queries
- Sharding is another technique to scale databases. Sharding involves splitting the data across multiple database instances, each of which is responsible for a subset of the data. This can be done based on a variety of criteria, such as the range of values in a particular column or the geographic location of the data. Sharding can be done manually or automatically. Automatic sharding is typically done through a process called <ins>schemaless design</ins>, where the schema of the database is not defined upfront but is instead determined dynamically based on the data being stored. This can make it easier to scale the database horizontally, but it can also make it more difficult to manage the database and ensure data consistency.
- Application designers need to consider which queries have tolerance to slightly stale data. They can be executed on read replicas, while other queries that require the latest data can be executed on the primary database instance.

### High Availability
- <ins>Multi-AZ deployments</ins> are a common technique to ensure high availability of databases. In a multi-AZ deployment, the database is deployed across multiple Availability Zones (AZs ) within a region. This can help ensure that the database remains available even if one AZ becomes unavailable due to a failure or maintenance.
- In case of failure of the primary node, Amazon RDS performs an automatic failover to the standby node. This ensures that the database remains available and that the application can continue to operate. When a failover is performed, there is a short period during which the primary node is not accessible.
- Resilient applications can be designed for graceful failure by offering reduced functionality during this period. This can be achieved by implementing a <ins>read-only mode</ins> by using read replicas.
- Amazon Aurora provides multi-master capability to enables reads and writes to be scaled across multiple AZs and supports cross-region replication.

### NoSQL
- trade some of the query and transaction capabilities of relational databases for the ability to scale horizontally and handle large amounts of unstructured data

### Single point of failure
- <ins>Single point of failure</ins> is a component that, if it fails, will cause the entire system to fail. This can be a single server, a single database, or a single network connection. Single points of failure can be avoided by implementing redundancy and failover mechanisms.

### Redundancy
- redundancy can be implemented in either standy or active mode
- in <ins>standby mode</ins>, the redundant component is not used until the primary component fails, typically used for databases and other components that require a high degree of consistency and reliability
- in <ins>active redundacy</ins>, requests are distributed across multiple redundant compute components, when one of them fails, others can absorb a larger share of workload
- active redundancy can achieve better usage and affect a better population when there's a failure

### Detect failure
- You can use services such as ELB and Amazon Route 53 to configure health checks and mask failure by routing traffic to healthy endpoints
- You can replace unhealthy nodes automatically using Auto Scaling or by using the Amazon EC2 auto-recovery

### Caching
- stores previously calculated data for future use
- improves application performance and increase the cost efficiency
- can be applied at multiple levels, such as in memory, in database, or in front of the database

### Application data caching
- when the result set is not found in the cache, the application can calculate it, or retrieve the data from the database and store it in the cache, or slowly mutating third-party content and store it in the cache
- when the result is found in the cache, the application can return the cached result, which improves the latency for end users and reduces load on back-end systems