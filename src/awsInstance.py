
def processInstance(instance: object):
    print(instance["InstanceType"])
    print(instance["State"]["Name"])
    try:
        print(instance["PrivateIpAddress"])
    except:
        print("No Private IP")