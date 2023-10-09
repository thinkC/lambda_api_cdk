from aws_cdk import core
import aws_cdk.aws_lambda as _lambda
import aws_cdk.aws_apigateway as apigateway
import aws_cdk.aws_iam as iam

class LambdaApiCdkStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
                # Create Lambda function
        lambda_function = _lambda.Function(
            self,
            "MyLambdaFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="lambda.handler",
            code=_lambda.Code.from_asset("lambda"),
        )
        # Define an API Gateway
        api = apigateway.RestApi(
            self,
            "MyApi",
            default_cors_preflight_options={
                "allow_origins": apigateway.Cors.ALL_ORIGINS,
                "allow_methods": apigateway.Cors.ALL_METHODS,
            },
        )

        # Create a Lambda integration for the API Gateway
        lambda_integration = apigateway.LambdaIntegration(lambda_function)
        # Create a resource and method on the API Gateway
        api.root.add_resource("hello").add_method(
            "GET",
            lambda_integration,
        )

        # Allow the Lambda function to be invoked by the API Gateway
        lambda_function.add_permission(
            "ApiGatewayInvokePermission",
            principal=iam.ServicePrincipal("apigateway.amazonaws.com"),
        )
