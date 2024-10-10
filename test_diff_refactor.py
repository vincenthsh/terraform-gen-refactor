import unittest
import diff_refactor  # import the module you want to test
import textwrap


class TestDiffRefactor(unittest.TestCase):
    def setUp(self):
        self.example_resource_move = {
            textwrap.dedent(
                """
                -resource "aws_security_group" "node" {
                +resource "aws_security_group" "this" {
                  name        = "${var.name_prefix}-security-group"
                  description = "${var.name_prefix} security group"
                  vpc_id      = var.vpc_id
                @@ -45,7 +45,7 @@ data "aws_subnet" "main" {
                  id = var.subnet_id
                }

                -resource "aws_eip" "node" {
                +resource "aws_eip" "this" {
                  domain = "vpc"
                }

                @@ -73,10 +73,10 @@ resource "aws_route53_record" "atlantis" {
                  name    = var.hostname_atlantis
                  ttl     = 80
                  type    = "A"
                -  records = [aws_eip.node.public_ip]
                +  records = [aws_eip.this.public_ip]
                }

                -data "cloudinit_config" "node" {
                +data "cloudinit_config" "this" {
                  gzip = false
                  part {
                    # https://cloudinit.readthedocs.io/en/latest/topics/format.html#user-data-script
                @@ -84,7 +84,7 @@ data "cloudinit_config" "node" {
                    content = templatefile("${path.module}/config/cloud-init.sh.tpl", {
                      name_prefix                     = var.name_prefix
                      ebs_volume_id                   = aws_ebs_volume.data.id
                -      allocation_id                   = aws_eip.node.id
                +      allocation_id                   = aws_eip.this.id
                      volume_mount                    = local.volume_mount
                      datadog_api_key_arn             = var.datadog_api_key_arn
                      datadog_host_tags               = var.datadog_host_tags
                @@ -93,18 +93,18 @@ data "cloudinit_config" "node" {
                  }
                }
                """
            ): textwrap.dedent(
                """
                moved {
                  from = aws_security_group.node
                  to   = aws_security_group.this
                }


                moved {
                  from = aws_eip.node
                  to   = aws_eip.this
                }
                """
            ),
        }
        self.example_module_move = {
            textwrap.dedent(
                """
                -module "atlantis" {
                +module "atlantis_test" {
                  source      = "../../../modules/atlantis"
                  name        = "atlantis-test"
                """
            ): textwrap.dedent(
                """
                moved {
                  from = module.atlantis
                  to   = module.atlantis_test
                }
                """
            ),
        }

    def test_generate_resource_move(self):
        for input, expected_output in self.example_resource_move.items():
            result = diff_refactor.generate_resource_move(input)
            self.assertEqual(result, expected_output)

    def test_generate_module_move(self):
        for input, expected_output in self.example_module_move.items():
            result = diff_refactor.generate_module_move(input)
            self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()
