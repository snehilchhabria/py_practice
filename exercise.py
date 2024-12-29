# Python

tagging_policy = {
        "mandatory_tags": {
            "EC2": {
                "BackupType": ["OrgStandard", "OrgStandardRDS", "LocalOnly", "None", "MigratedLegacy"],
                "carlyle:os-type": ["linux", "windows"],
                "Name": [],
                "carlyle:owner": [],
                "carlyle:primary-poc": [],
                "carlyle:environment": ["dev", "qa", "uat", "staging", "prodint", "prod", "test"],
                "carlyle:application": [],
            }
        }
    }
mandatory_tags = tagging_policy["mandatory_tags"]["EC2"]

def validate_instance_tags(tags):

    for key in tags:
        if key in mandatory_tags:
            if not mandatory_tags[key] or tags[key] in mandatory_tags[key]:
                print(f"Tag '{key}' exists with valid value '{tags[key]}'")
            else:
                print(f"Tag '{key}' exists but with invalid value '{tags[key]}'")
        else:
            print(f"Tag '{key}' does not exist in the tagging policy")

# Example usage
example_tags = {'carlyle:environment': 'de', 'carlyle:application': 'keepesr', 
    'BackupType': 'OrgStandard','tcgcloud:exception-ec2-instance-size': '9','carlyle:os-type':'linux',
    'carlyle:owner':'asasd','Names':'', 'carlyle:primary-poc':'', 'abc' :'', 'Name':''}

validate_instance_tags(example_tags)
