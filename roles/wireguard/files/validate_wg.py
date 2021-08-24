#!/usr/bin/env python3
import os
import subprocess
t = 10
t2 = 20


def validate_vpn(vpn):
    server = vpn['local ip']
    print(f'Testing ICMP to {server}..')
    ping = os.system(f'ping -c 1 -W {t} {server} &> /dev/null')
    if ping != 0:
        service = vpn['local service']
        print(f'ICMP test failed. Restarting {service} service..')
        os.system(f'systemctl restart {service}')
        print('Done!\nTesting ICMP again..')
        ping2 = os.system(f'ping -c 1 -W {t2} {server} &> /dev/null')

        if ping2 != 0:
            print(f'{server} is still unreachable even after service restart\n')
        else:
            print(f'{server} is reachable now after service restart\n')
    else:
        print(f'{server} is currently reachable\n')


server_name = os.uname()[1]
wg_service = f"wg-quick@{server_name}_wg"
wg_file = f"{server_name}_wg.conf"
os.chdir("/etc/wireguard")
get_ip = subprocess.run([f'grep -i address {wg_file} | head -1'], shell=True, check=True, stdout=subprocess.PIPE,
                        universal_newlines=True)
output = get_ip.stdout.split()
ip = output[2].split("/")[0]

all_vpn = [
    # {'name': 'lighthouse', 'service': 'nebula'},
    {'local ip': ip, 'local service': wg_service},
]

for i in all_vpn:
    validate_vpn(i)

