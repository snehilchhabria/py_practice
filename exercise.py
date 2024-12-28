# Python Assignment
def validate_instance_tags(tags):
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

    for tag_key, tag_values in mandatory_tags.items():
        if tag_key in tags:
            if not tag_values or tags[tag_key] in tag_values:
                print(f"Tag '{tag_key}' with value '{tags[tag_key]}' exists and is valid.")
            else:
                print(f"Tag '{tag_key}' exists but value '{tags[tag_key]}' is not valid.")
        else:
            print(f"Tag '{tag_key}' does not exist.")

tags = {
    "BackupType": "",
    "carlyle:os-type": "linux",
    "Name": "ExampleName",
    "carlyle:owner": "John Doe",
    "carlyle:primary-poc": "Jane Smith",
    "carlyle:environment": "pro",
    "carlyle:application": "ExampleApp"
}

validate_instance_tags(tags)
