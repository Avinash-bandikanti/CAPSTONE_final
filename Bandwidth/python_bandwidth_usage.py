import psutil
#it gives the system info
import matplotlib.pyplot as plt
# Define the network interface to moniter
interface='eth0'
# Retrieve the network usage statistics for the specified interface
net_io_counters=psutil.net_io_counters()
# interface_counters=net_io_counters_get(interface)
print(net_io_counters)
# Calculate the amount of data received and sent in MB
bytes_received=net_io_counters.bytes_recv/1024/1024
bytes_sent=net_io_counters.bytes_sent/1024/1024
# Create a bar chart of the network usage
plt.bar(['Received','sent'],[bytes_received,bytes_sent])
plt.ylabel('Bandwidth usage (MB)')
plt.title('Network usage for interface {}'.format(interface))
plt.show()