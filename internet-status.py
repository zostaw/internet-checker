import os
import numpy as np
from argparse import ArgumentParser
import json

def check_router_connection(wifi_network):
    # to be defined, it should ensure it's up
    pass

def ping_internet(hosts = ["google.com"], alert_trigger=None, email=None):
    # method verifies internet connection by ping-testing defined machines
    # it will send notification and attempt to send e-mail if any of the test nodes is available
    # hosts is list of hosts that should be pinged to verify connection
    #     it takes values of hostname or IP
    # alert_trigger defines whether method should notify when connection is lost or acquired
    #     it takes values: "UP" or "DOWN"

    status = []

    # check the response
    for id, host in enumerate(hosts):
        resp = os.system("ping -c 1 " + host)
        status.append([host, "UP" if not resp else "DOWN"])
    status = np.array(status)

    # if None, the program will continue to notify no matter what status
    # if alert_trigger is UP, notification will be sent only if at least one status is UP
    # analogicaly if alert_trigger is DOWN, notification will be sent only if at least one status is DOWN
    if alert_trigger is not None and alert_trigger not in status[:,1]:
        return

    # macos
    title = "Internet connection status"

    notify = f'''
    osascript -e 'display notification "{status}" with title "{title}"'
    '''
    os.system(notify)

    if email:
        mail = f'''
        echo "{status}" | mail -s "{title} on $HOSTNAME" {email}
        '''
        os.system(mail)

if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("email", help="provie e-mail to send alert", default=None)
    parser.add_argument("-f", "--file", default="hosts.json",
                    help="file containing list of hosts to check availability")
    parser.add_argument("-n", "--notification-rule", default=None,
                    help="specify if should notify on 'UP' status or 'DOWN'")

    args = parser.parse_args()

    try:
        with open(args.file, "r") as hosts_file:
            hosts = json.load(hosts_file)["hosts"]
            print(hosts)
    except:
        print(f"Hosts list could not be loaded from file {args.file}")
        print("Default host list will be used: [\"google.com\"]")
        ping_internet(alert_trigger=args.notification_rule, email=args.email)
    else:
        ping_internet(hosts = hosts, alert_trigger=args.notification_rule, email=args.email)

