#!/usr/bin/env python3
import os
from aws_cdk import core

from lambda_api_cdk.lambda_api_cdk_stack import LambdaApiCdkStack
from basic_vpc_stack import BasicVpcStack
from lambda_api_cdk.ecs_stack import EcsStack

app = core.App()
LambdaApiCdkStack(app, "lambda-api-cdk")
vpc_stack = BasicVpcStack(app,"BasicVpcStack")
EcsStack(app, "EcsStack",
                        env=core.Environment(account  = os.environ["CDK_DEFAULT_ACCOUNT"],
                                             region   = os.environ["CDK_DEFAULT_REGION"]))
app.synth()
