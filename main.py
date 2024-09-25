import sys
from collections import defaultdict

lookuptable_dict = {}
tag_dict = {}
comb_dict = {}
protocol_map = {
    1: "icmp",
    4: "ipv4",
    6: "tcp",
    17: "udp",
    41: "ipv6",
    47: "gre",
}

def read_flow_log(flow_log_filepath):
    with open(flow_log_filepath, 'r') as file:
        for line in file:
            yield line.strip("\n")


def process_flow_log_line(log_line: str):
    log_line_list = log_line.split(" ")
    protocol = log_line_list[7].lower()
    port = log_line_list[6]
    
    protocol_string = protocol_map[int(protocol)]
    if protocol_string in lookuptable_dict:
        if port in lookuptable_dict[protocol_string]:
            tag_dict[lookuptable_dict[protocol_string][port]] += 1
    
    if protocol_string not in comb_dict:
        comb_dict[protocol_string] = defaultdict(int)
    comb_dict[protocol_string][port] += 1


def read_lookup_table(lookup_table_filepath):
     with open(lookup_table_filepath, 'r') as file:
        # Skip the first line (header)
        next(file)
        for line in file:
            yield line.strip("\n")

def process_lookuptable_record(row):
    port, protocol, tag = row.split(",")
    if protocol not in lookuptable_dict:
        lookuptable_dict[protocol] = {}
    
    lookuptable_dict[protocol][port] = tag
    tag_dict[tag] = 0


def generate_output_file():
    
    with open("output.txt", "w+") as file:
        file.write('Tag Counts: \n')
        file.write('Tag,Count \n')

        for tag, count in tag_dict.items():
            file.write(f"{tag},{count}\n")
        
        file.write("\nPort/Protocol Combination Counts: \n")
        file.write("Port,Protocol,Count \n")

        for protocol, port_dict in comb_dict.items():
            for port, count in port_dict.items():
                file.write(f"{port},{protocol},{count} \n")


if __name__ == "__main__":
    
    flow_log_filepath = sys.argv[1]
    table_csv_filepath = sys.argv[2]

    for row in read_lookup_table(table_csv_filepath):
        process_lookuptable_record(row)

    # print(lookuptable_dict)
    for line in read_flow_log(flow_log_filepath):
        process_flow_log_line(line)

    generate_output_file()