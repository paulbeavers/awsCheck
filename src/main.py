
import os
import json
import subprocess
import awsInstance

proc = subprocess.Popen('aws ec2 describe-instances', shell=True, stdout=subprocess.PIPE)
proc.wait()
instanceString = proc.stdout.read()

instanceJSON = json.loads(instanceString)

for reservation in instanceJSON["Reservations"]:
    for instance in reservation["Instances"]:
        awsInstance.processInstance(instance)
