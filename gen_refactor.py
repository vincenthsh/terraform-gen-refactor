#!/usr/bin/env python3
import sys
import re


def generate_resource_move(git_diff):
    # Regular expression to parse the git diff
    pattern = r'\-resource "(.+)" "(.+)" {\n\+resource "(.+)" "(.+)" {'

    matches = re.findall(pattern, git_diff)
    if not matches:
        pass

    configs = []
    for match in matches:
        from_resource = match[0] + "." + match[1]
        to_resource = match[2] + "." + match[3]
        config = f"\nmoved {{\n  from = {from_resource}\n  to   = {to_resource}\n}}\n"
        configs.append(config)

    return "\n".join(configs)


def generate_module_move(git_diff):
    # Regular expression to parse the git diff
    pattern = r'\-module "(.+)" {\n\+module "(.+)" {'

    matches = re.findall(pattern, git_diff)
    if not matches:
        pass

    configs = []
    for match in matches:
        from_module = "module." + match[0]
        to_module = "module." + match[1]
        config = f"\nmoved {{\n  from = {from_module}\n  to   = {to_module}\n}}\n"
        configs.append(config)

    return "\n".join(configs)


if __name__ == "__main__":
    git_diff = sys.stdin.read()
    print(generate_resource_move(git_diff))
    print(generate_module_move(git_diff))
