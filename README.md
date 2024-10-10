# Utility scripts

These are utlity scripts that really should be JS or TS.

## Gen Refactor

Generate a terraform refactor configuration file based on the git diff of a terraform configuration file.

Currently only supports:

1. Renaming resources
1. Renaming modules

References:

- [Terraform refactoring](https://developer.hashicorp.com/terraform/language/modules/develop/refactoring#moved-block-syntax)

### Usage

```bash
git diff HEAD~ HEAD -- ./terraform/modules/atlantis/iam.tf | scripts/not-yet-typescript/gen_refactor.py > ./terraform/modules/atlantis/iam-refactor.tf
```

>[!NOTE]
> Just use `git diff -- <file-path>` if you haven't committed your changes yet.
>
> use `git diff --name-only | grep .tf` to get a list of changed terraform config files.

### Testing

```bash
python3 -m unittest test_gen_refactor.py
```
