import argparse
import re


def generate_refactor(tfplan_output):
    resource_action_pattern = re.compile(r'# (.*)((?:random|aws)_[^.]*)\.(.*) will be (created|destroyed)')
    matches = resource_action_pattern.findall(tfplan_output)

    if not matches:
        print("No regex matches in the Terraform plan output")
        exit(1)

    # Group By resource type
    resources = {}
    for prefix, resource_type, resource_name, action in matches:
        full_address = f'{resource_type}.{resource_name}'
        if prefix:
            full_address = f'{prefix}{full_address}'

        if resource_type not in resources:
            resources[resource_type] = {"created": [], "destroyed": []}
        resources[resource_type][action].append(full_address)

    # # to debug: pretty print full resources dict
    # import json
    # with open('refactor.json', 'w') as f:
    #     f.write(json.dumps(resources, indent=2))

    result = []
    # Calculate the refactor plan
    for resource_type, actions in resources.items():
        if len(actions["created"]) != len(actions["destroyed"]):
            result.append(f'# NOTE: unmatched resources for {resource_type}')
            for destroy_resource_name in actions["destroyed"]:
                result.append(f'# destroy {destroy_resource_name}')
            for create_resource_name in actions["created"]:
                result.append(f'# create {create_resource_name}')

            if len(actions["destroyed"]) > 0:
                result.append(f'# CAREFUL: Guesses for destroyed {resource_type}')
                for i, destroy_resource_name in enumerate(actions["destroyed"]):
                    candidate = actions["created"][i] if i < len(actions["created"]) else "N/A"
                    result.append(f'moved {{\n  from = {destroy_resource_name}\n  to = {candidate}\n}}\n')
            else:
                result.append("# No destroy actions found, ignoring\n")
        elif len(actions["created"]) == 1 and len(actions["destroyed"]) == 1:
            create_resource_name = actions["created"][0]
            destroy_resource_name = actions["destroyed"][0]
            result.append(f'# rename {destroy_resource_name}')
            result.append(f'moved {{\n  from = {destroy_resource_name}\n  to   = {create_resource_name}\n}}\n')
        else:
            result.append(f'# NOTE: multi-match for {resource_type}')
            result.append(f'# {resource_type} - create:')
            for create_resource_name in actions["created"]:
                result.append(f'# {create_resource_name}')
            for i, destroy_resource_name in enumerate(actions["destroyed"]):
                result.append(f'moved {{\n  from = {destroy_resource_name}\n  to = {actions["created"][i]}\n}}\n')

    return "\n".join(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Read a Terraform plan file.')
    parser.add_argument('filename', type=str, help='The filename of the Terraform plan to read')
    args = parser.parse_args()

    if not args.filename:
        parser.print_help()
        exit(1)

    try:
        with open(args.filename, 'r') as f:
            tfplan_output = f.read()
    except FileNotFoundError:
        print("Please run 'terraform plan -no-color >tfplan' before running this script")
        exit(1)

    print(generate_refactor(tfplan_output))
