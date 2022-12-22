"""
script : main
Author : Sanju Abraham Varughese
Purpose : Analysing the dchp log file and creation of csv file with vendor deatils
usage : python main.py
"""
import Source.csv_file as c
import csv
my_hosts = []
oui_id = {
    "C8:4B:D6": "Dell Inc",
    "18:68:CB": "Hangzhou Hikvision Digital Technology",
    "C0:25:A5": "Dell Inc",
    "A4:4C:C8": "Dell Inc",
    "BC:5F:F4": "ASrock",
    "B8:27:EB": "Raspberry Pi"
}

ipaddr=[]
mac=[]
vend=[]
hname=[]
CSV_FINAL_FILE="./nodes.csv"
if (__name__ == '__main__'):
    print(f"This module is called {__name__} and executes as a standalone script")
    # Open the logfile for read
    logfilename = "./dhcpd.log"
    logfile = open(logfilename, "r")
    # Iterate through every line in the log fil
    for line in logfile:
        # Parse the line type
        interesting_bit = line[34:]
        list_of_values = interesting_bit.split(" ")
        # Handle each line type 
        if list_of_values[0] == "DHCPACK" and list_of_values[1] == "on":
            dhcpack_values = [ele.strip('(').strip(')') for ele in list_of_values]
            ipv4 = dhcpack_values[2]
            mac_address = dhcpack_values[4].upper()
            oui= mac_address[0:8]
            vendor_values = [val for key, val in oui_id.items() if oui in key]
            vendor=str(vendor_values)[1:-1]
            # Check to see if this host was previously identified
            if mac_address in my_hosts:
                pass
            else:
                # Add this new host to the my_hosts list
                ipaddr.append(ipv4)
                mac.append(mac_address)
                vend.append(vendor)
                host_name = dhcpack_values[5].upper()
                # Some sentences do not have a host name
                if host_name == "VIA":
                    host_name = "No Hostname"
                hname.append(host_name)
                my_hosts=list(zip(ipaddr,mac,vend,hname))
                hosts_lists = list(set(map(tuple, my_hosts)))
    logfile.close()
    c.csv_file(CSV_FINAL_FILE,hosts_lists)
else:
    print(f"This module is called {__name__} and is being called by another script")