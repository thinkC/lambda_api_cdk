from aws_cdk import core
import aws_cdk.aws_ec2 as ec2

class BasicVpcStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create a VPC
        vpc = ec2.Vpc(
            self,
            "MyVpc",
            # Specify the subnet configuration as an array
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="PublicSubnet",
                    subnet_type=ec2.SubnetType.PUBLIC,
                ),
                ec2.SubnetConfiguration(
                    name="PrivateSubnet",
                    subnet_type=ec2.SubnetType.PRIVATE,
                ),
            ],
            )
        # Create an Internet Gateway
        igw = ec2.CfnInternetGateway(self, "MyIGW")

        # Attach the Internet Gateway to the VPC
        vpc_gateway_attachment = ec2.CfnVPCGatewayAttachment(
            self,
            "MyIGWAttachment",
            vpc_id=vpc.vpc_id,
            internet_gateway_id=igw.ref,
        )
app = core.App()
BasicVpcStack(app, "BasicVpcStack")
app.synth()

