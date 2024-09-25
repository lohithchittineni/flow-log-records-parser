## flow-log-records-parser
### Assumptions:

- Supports default log format version 2

- For protocols using mappings for only ICMP, TCP, UDP, IPv4, IPv6, GRE

- Not every flow log will map directly to a tag, so tag counts and combination counts may not match

- Both the lookup table file and flow record logs file are always formatted correctly

### How to run:
Need python version >=3.10

`python3 main.py <flow_log textfile> <lookup table textfile>`

Example:

`python3 main.py flow.txt table.txt`

Output is shown in output.txt

### References:
https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html

https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml

https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-records-examples.html