# rename aws_cloudcontrolapi_resource.required-tags-reports_handshakes_view_A03CB127
moved {
  from = aws_cloudcontrolapi_resource.required-tags-reports_handshakes_view_A03CB127
  to   = aws_cloudcontrolapi_resource.required-tags-reports_handshakes_view
}

# rename aws_cloudwatch_log_group.required-tags-reports_config-lambda_log-group_612EF1DA
moved {
  from = aws_cloudwatch_log_group.required-tags-reports_config-lambda_log-group_612EF1DA
  to   = aws_cloudwatch_log_group.required-tags-reports_config-lambda_log-group
}

# NOTE: multi-match for aws_config_conformance_pack
# aws_config_conformance_pack - create:
# aws_config_conformance_pack.required-tags-reports_custom-required-tags-dev1
# aws_config_conformance_pack.required-tags-reports_custom-required-tags-prd
# aws_config_conformance_pack.required-tags-reports_custom-required-tags-stg
moved {
  from = aws_config_conformance_pack.required-tags-reports_custom-required-tags-dev_21E116B1
  to = aws_config_conformance_pack.required-tags-reports_custom-required-tags-dev1
}

moved {
  from = aws_config_conformance_pack.required-tags-reports_custom-required-tags-prd_8C83DBC6
  to = aws_config_conformance_pack.required-tags-reports_custom-required-tags-prd
}

moved {
  from = aws_config_conformance_pack.required-tags-reports_custom-required-tags-stg_956BCB23
  to = aws_config_conformance_pack.required-tags-reports_custom-required-tags-stg
}

# rename aws_iam_policy.required-tags-reports_config-lambda_service-role_RolePolicy_C42ED74A
moved {
  from = aws_iam_policy.required-tags-reports_config-lambda_service-role_RolePolicy_C42ED74A
  to   = aws_iam_policy.required-tags-reports_config-lambda_service-role_RolePolicy
}

# rename aws_iam_role.required-tags-reports_config-lambda_service-role_05B4D0C1
moved {
  from = aws_iam_role.required-tags-reports_config-lambda_service-role_05B4D0C1
  to   = aws_iam_role.required-tags-reports_config-lambda_service-role
}

# rename aws_lambda_function.required-tags-reports_config-lambda_fn_A4B30528
moved {
  from = aws_lambda_function.required-tags-reports_config-lambda_fn_A4B30528
  to   = aws_lambda_function.required-tags-reports_config-lambda_fn
}

# rename module.prd-foo-docdb_03006172.random_password.master[0]
moved {
  from = module.prd-foo-docdb_03006172.random_password.master[0]
  to   = module.docdb_05536A7B.random_password.master[0]
}
