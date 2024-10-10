# Utility scripts

These are utlity scripts that really should be JS or TS.

## Diff Refactor

Generate a terraform refactor configuration file based on the git diff of a terraform configuration file.

Currently only supports:

1. Renaming resources
1. Renaming modules

References:

- [Terraform refactoring](https://developer.hashicorp.com/terraform/language/modules/develop/refactoring#moved-block-syntax)

### Diff Refactor Usage

```bash
git diff HEAD~ HEAD -- ./terraform/modules/atlantis/iam.tf | diff_refactor.py > ./terraform/modules/atlantis/iam-refactor.tf
```

>[!NOTE]
> Just use `git diff -- <file-path>` if you haven't committed your changes yet.
>
> use `git diff --name-only | grep .tf` to get a list of changed terraform config files.

### Diff Refactor Testing

```bash
python3 -m unittest test_diff_refactor.py
```

## Plan Refactor

Generate a terraform refactor configuration file based on the terraform plan output.

> [!WARNING]
> Use git diff for better results, unless you use CDKTF and didn't write moved statements in your CDKTF code...

This is a lot more complicated and requires manual tuning once the script completed.

### Plan Refactor Usage

```bash
terraform plan -no-color > tfplan
plan_refactor.py tfplan > refactor.tf
```

### Plan Refactor Testing

```bash
python3 -m unittest test_plan_refactor.py
```
