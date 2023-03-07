from scapy.all import *
import matplotlib.pyplot as plt1
# Capture packets for 30 seconds
packets=sniff(timeout=30)
# Extract the protocol type from each packet
protocols =[pkt.sprintf('%IP.proto%') for pkt in packets]
# count the occurrences of each protocol type
counts={}
for proto in protocols:
    if proto not in counts:
        counts[proto]=1
    else:
        counts[proto]+=1
# plot the counts as a bar chart
plt1.bar(range(len(counts)),list(counts.values()),align='center')
plt1.xticks(range(len(counts)),list(counts.keys()))
plt1.xlabel('Protocol')
plt1.ylabel('Count')
plt1.show()