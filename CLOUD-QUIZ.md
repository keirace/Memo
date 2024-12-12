Q: **Class C**: 254 usable host addresses, reserving 1 for network and 1 for broadcast address

Q: **Class A**: /8 2^7 Network Addresses, 2^24 Host addresses

Q: Reserved ports are `0-1023`

**Q: Real-world scenario where vertical scaling is preferred**:

> In a scenario where a business is running a database that requires high performance, such as a large relational database like Oracle or MySQL, vertical scaling might be preferred. Databases can benefit from vertical scaling because it simplifies data consistency and query execution without the complexities of managing data across multiple servers, which can introduce latency and consistency challenges. 
> For instance, if a company’s database application needs better performance due to larger datasets or more transactions, adding more CPU and RAM to a single server (vertical scaling) can enhance performance without requiring architectural changes, as would be needed with horizontal scaling.

Q: rename: `mv`

Q: Exit status
  - `0` successful
  - `1-255` failure
  - `?` exit status of the *previously* executed command

Q: - `>` connects to a file while `|` connects with input of a 2nd command

Q: Average time in last 5 mins
    - img of a `top` command, look for load average: 1 min, **5 mins**, 15 mins
  ```
  Load Avg: 1.82, 2.26, 2.62  CPU usage: 4.32% user, 4.32% sys, 91.34% idle
  ```
  - answer: 2.26

Q: What should not be managed in VCS?
- **Configuration files** (e.g., `/etc/hosts`, `/etc/passwd`)
- **Log files** (e.g., `/var/log/*`)
- **Software packages** (e.g., `/usr/local/bin/*`)

Q: ___ is a collection of infrastructure elements that are defined as a unit and can be managed as a single entity.
- answer: **Stack**



internal lb
http data lb layer
