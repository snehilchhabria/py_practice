# # Python


# tagging_policy = {
#         "mandatory_tags": {
#             "EC2": {
#                 "BackupType": ["OrgStandard", "OrgStandardRDS", "LocalOnly", "None", "MigratedLegacy"],
#                 "carlyle:os-type": ["linux", "windows"],
#                 "Name": [],
#                 "carlyle:owner": [],
#                 "carlyle:primary-poc": [],
#                 "carlyle:environment": ["dev", "qa", "uat", "staging", "prodint", "prod", "test"],
#                 "carlyle:application": [],
#             }
#         }
#     }
# mandatory_tags = tagging_policy["mandatory_tags"]["EC2"]

# # def find_closest_match(key, mandatory_keys):
# #     closest_matches = difflib.get_close_matches(key, mandatory_keys, 1, 0.7)
# #     return closest_matches[0] if closest_matches else None

# def validate_instance_tags(tags):
#     tag_keys = set(tags.keys())
#     mandatory_keys = set(mandatory_tags.keys())

#     missing_keys  = mandatory_keys - tag_keys
#     errors = [f"Tag '{key}' missing." for key in missing_keys]

#     for key in mandatory_keys & tag_keys:
#         value = tags[key]
#         valid_values = mandatory_tags[key]

#         if value == "":
#             errors.append(f"tag '{key}' empty and should have a value")
#         elif valid_values and value not in valid_values:
#             errors.append(f"value for tag '{key}' is invalid")

#     if errors:
#         print("\n".join(errors))
#     else:
#         print("All Tags are correct")


#     # flag = True
#     # for key in tags:
#     #     if key in mandatory_tags:
#     #         if not mandatory_tags[key] or tags[key] in mandatory_tags[key]:
#     #             continue
#     #             # print(f"Tag '{key}' exists with valid value '{tags[key]}'")
#     #         else:
#     #             print(f"Tag '{key}' exists but referred with invalid value '{tags[key]}'. Valid values are: {mandatory_tags[key]}")
#     #             flag = False
#     #     else:
#     #         closest_match = find_closest_match(key, mandatory_tags.keys())
#     #         if closest_match:
#     #             flag = False
#     #             print(f"Tag '{key}' does not exist, did you mean'{closest_match}'")
#     #         else:
#     #             pass
#     #     if flag == True:
#     #         print("All correct")

# # Example usage
# example_tags = {'carlyle:environment': 'dev', 'carlyle:application': 'keepesr', 
#     'BackupType': 'OrgStandard','carlyle:os-type':'linux',
#     'carlyle:owner':'asasd', 'carlyle:primary-poc':'','abs':'not exists', 'Name':''}

# validate_instance_tags(example_tags)













# mandatory_tags = {
#     "BackupType": ["OrgStandard", "OrgStandardRDS", "LocalOnly", "None", "MigratedLegacy"],
#     "carlyle:os-type": ["linux", "windows"],
#     "Name": [],
#     "carlyle:owner": [],
#     "carlyle:primary-poc": [],
#     "carlyle:environment": ["dev", "qa", "uat", "staging", "prodint", "prod", "test"],
#     "carlyle:application": [],
# }

# def validate_instance_tags(tags):
#     tag_keys = set(tags.keys())
#     mandatory_keys = set(mandatory_tags.keys())

#     missing_keys = mandatory_keys - tag_keys
#     errors = [f"Tag '{key}' missing." for key in missing_keys]

#     for key in mandatory_keys & tag_keys:
#         value = tags[key]
#         valid_values = mandatory_tags[key]

#         if valid_values:
#             if value == "":
#                 errors.append(f"Tag '{key}' is empty and should have a value.")
#             elif value not in valid_values:
#                 errors.append(f"Value for tag '{key}' is invalid.")

#     if errors:
#         print("\n".join(errors))
#     else:
#         print("All Tags are correct.")

# # Example usage
# example_tags = {
#     'carlyle:environmen': 'dev',
#     'carlyle:application': '',
#     'BackupType': '',
#     'carlyle:os-type': 'windows',
#     'carlyle:owner': 'asasd',
#     'carlyle:primary-poc': '',
#     'abs': 'not exists',
#     'Nam': ''
# }

# validate_instance_tags(example_tags)



















# tagging_policy = {
#         "mandatory_tags": {
#             "EC2": {
#                 "BackupType": ["OrgStandard", "OrgStandardRDS", "LocalOnly", "None", "MigratedLegacy"],
#                 "carlyle:os-type": ["linux", "windows"],
#                 "Name": [],
#                 "carlyle:owner": [],
#                 "carlyle:primary-poc": [],
#                 "carlyle:environment": ["dev", "qa", "uat", "staging", "prodint", "prod", "test"],
#                 "carlyle:application": [],
#             }
#         }
#     }
# mandatory_tags = tagging_policy["mandatory_tags"]["EC2"]

# def validate_instance_tags(tags):
#     tag_keys = set(tags.keys())
#     mandatory_keys = set(mandatory_tags.keys())

#     missing_keys = mandatory_keys - tag_keys
#     errors = [f"Tag '{key}' missing." for key in missing_keys]

#     for key in mandatory_keys & tag_keys:
#         value = tags[key]
#         valid_values = mandatory_tags[key]

#         if value == "" and valid_values:
#             errors.append(f"Tag '{key}' is empty and should have one of the following values: {', '.join(valid_values)}.")
#         elif valid_values and value not in valid_values:
#             errors.append(f"Value for tag '{key}' is invalid should have one of the following values: {', '.join(valid_values)}.")

#     if errors:
#         print("\n".join(errors))
#     else:
#         print("All Tags are correct.")

# # Example usage
# example_tags = {
#     'carlyle:environment': 'ev',
#     'carlyle:application': 'keepesr',
#     'BackupType': '',
#     'carlyle:os-type': 'linux',
#     'carlyle:owner': 'asasd',
#     'carlyle:primary-poc': '',
#     'abs': 'not exists',
#     'Nam': ''
# }

# validate_instance_tags(example_tags)












# # Define the tagging policy with required tags for EC2
# tagging_policy = {
#     "mandatory_tags": {
#         "EC2": {
#             "BackupType": ["OrgStandard", "OrgStandardRDS", "LocalOnly", "None", "MigratedLegacy"],
#             "carlyle:os-type": ["linux", "windows"],
#             "Name": [],
#             "carlyle:owner": [],
#             "carlyle:primary-poc": [],
#             "carlyle:environment": ["dev", "qa", "uat", "staging", "prodint", "prod", "test"],
#             "carlyle:application": [],
#         }
#     }
# }

# # Extract the mandatory tags for EC2
# mandatory_tags = tagging_policy["mandatory_tags"]["EC2"]
# flag = True

# def validate_instance_tags(tags):
#     # Identify the keys in the provided tags
#     provided_keys = set(tags.keys())
#     # Identify the keys that are mandatory
#     required_keys = set(mandatory_tags.keys())
    

#     # Determine which mandatory keys are missing
#     missing_keys = required_keys - provided_keys
#     if(missing_keys):
#         flag = False
#         print("Tag '{key}' is missing" for key in missing_keys)
#     # Initialize a list to collect error messages
#     # error_messages = [f"Tag '{key}' is missing." for key in missing_keys]

#     # Validate each provided tag
#     for key in required_keys & provided_keys:
#         value = tags[key]
#         valid_values = mandatory_tags[key]

#         # Check if the tag is empty and should have a value
#         if value == "" and valid_values:
#            print(f"Tag '{key}' is empty and should have one of these values: {', '.join(valid_values)}.")
#            flag = False
#         # Check if the tag value is invalid
#         elif valid_values and value not in valid_values:
#             flag = False
#             print(f"Value for tag '{key}' is invalid and should be one of these: {', '.join(valid_values)}.")

#     # Print the error messages or confirm that all tags are correct
#     if flag:
#         print("All Tags are correct.")

# # Example usage
# example_tags = {
#     'carlyle:environment': 'dev',
#     'carlyle:application': 'keepesr',
#     'BackupType': 'OrgStandard',
#     'carlyle:os-type': 'linux',
#     'carlyle:owner': 'asasd',
#     'carlyle:primary-poc': '',
#     'abs': 'not exists',
#     'Nam': ''
# }

# validate_instance_tags(example_tags)













# # Define the tagging policy with required tags for EC2
# tagging_policy = {
#     "mandatory_tags": {
#         "EC2": {
#             "BackupType": ["OrgStandard", "OrgStandardRDS", "LocalOnly", "None", "MigratedLegacy"],
#             "carlyle:os-type": ["linux", "windows"],
#             "Name": [],
#             "carlyle:owner": [],
#             "carlyle:primary-poc": [],
#             "carlyle:environment": ["dev", "qa", "uat", "staging", "prodint", "prod", "test"],
#             "carlyle:application": [],
#         }
#     }
# }

# mandatory_tags = tagging_policy["mandatory_tags"]["EC2"]
# flag = True

# def validate_instance_tags(tags):
#     provided_keys = set(tags.keys())
#     required_keys = set(mandatory_tags.keys())
    
#     missing_keys = required_keys - provided_keys
#     if missing_keys:
#         global flag
#         flag = False
#         for key in missing_keys:
#             print(f"Tag '{key}' is missing.")
    
#     # Validate tag
#     for key in required_keys & provided_keys:
#         value = tags[key]
#         valid_values = mandatory_tags[key]

#         # Check if the tag is empty and should have a value
#         if value == "" and valid_values:
#             print(f"Tag '{key}' is empty and should have one of these values: {', '.join(valid_values)}.")
#             flag = False
#         # Check if the tag value is invalid
#         elif valid_values and value not in valid_values:
#             flag = False
#             print(f"Value for tag '{key}' is invalid and should be one of these: {', '.join(valid_values)}.")

#     if flag:
#         print("All Tags are correct.")

# # Example usage
# example_tags = {
#     'carlyle:environment': 'devcls',
#     'carlyle:application': 'keepesr',
#     'BackupType': 'OrgStandard',
#     'carlyle:os-type': 'linux',
#     'carlyle:owner': 'asasd',
#     'carlyle:primary-poc': '',
#     'abs': 'not exists',
#     'Name': ''
# }

# validate_instance_tags(example_tags)













# Define the tagging policy with required tags for EC2
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
    required_keys = set(mandatory_tags.keys())
 
    # Check if all required keys are present
    if required_keys.issubset(tags.keys()):
        print("All required keys are present.")
    else:
        missing_keys = required_keys - set(tags.keys())
        print(f"Missing keys: {missing_keys}")
 
    # Validate tag values
    for key in required_keys & tags.keys():
        value = tags[key]
        valid_values = mandatory_tags[key]
        if not value and valid_values:
            print(f"Tag '{key}' is empty and should have one of these values: {', '.join(valid_values)}.")
        elif valid_values and value not in valid_values:
            print(f"Value for tag '{key}' is invalid and should be one of these: {', '.join(valid_values)}.")
 
# Example usage
example_tags = {
    'carlyle:environment': 'dev',
    'carlyle:application': 'keepesr',
    'BackupType': 'OrgStandard',
    'carlyle:os-type': 'linux',
    'carlyle:owner': 'asasd',
    'carlyle:primary-poc': '',
    'abs': 'not exists',
    'Nam': ''
}
 
validate_instance_tags(example_tags)
