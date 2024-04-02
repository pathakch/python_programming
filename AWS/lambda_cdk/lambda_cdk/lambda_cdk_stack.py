from aws_cdk import (
    Stack,
    aws_lambda as function_lambda,
)

from constructs import Construct

class LambdaCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        demo_lambda_fn = function_lambda.Function(
            self, "DemoLambdaFunctionStack",
            function_name = "run_current_datetime",
            runtime = function_lambda.Runtime.PYTHON_3_12,
            code = function_lambda.Code.from_asset('./function'),
            handler = "demo_function.demo_function"
        )