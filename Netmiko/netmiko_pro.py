from netmiko import ConnectHandler
# Define the device information
device={
    'device_type':'linux',
    'ip':'192.168.149.128',
    'username':'avinash',
    'password':'abhi123'
}
# Create a Netmiko SSH connection to the device
connection=ConnectHandler(**device)
# send the show process cpu command and capture the output
cpu_output=connection.send_command('cat /proc/cpuinfo')
# send the show memory statistics command and capture the output
mem_output=connection.send_command('free -h')
# close the netmiko SSH connection
connection.disconnect()
# print the CPU and memory output
print('CPU Information')
print(cpu_output)
print('\nmemory Information')
print(mem_output)