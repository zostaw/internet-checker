# internet-checker

The program will test connection to defined hosts.
A notification will popup and e-mail will be sent (if possible).

## Prerequisites

1. python 3.10.5 (or higher)
2. smtp configured on your machine

## Run

1. Define your hosts.yaml for status check (by default google.com will be pinged). One can find an example file in examples/hosts.json

2. Execute:

```bash
python internet-status.py email
```

## options

"-f", "--file": path to hosts.json file - it must have an dictionary "hosts" with list of servers for which the status should be checked
    if param is not provided - google.com will be pinged

"-n", "--notification-rule": defines rule for when notification should be sent, available options:
    "UP" - send notification if any host is available
    "DOWN" - send notification if any host is unavailable
    if param is not provided -  status will be sent in any case

"email": e-mail address on which a notification will be sent
