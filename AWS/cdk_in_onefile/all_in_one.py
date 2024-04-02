import aws_cdk
from aws_cdk import (
    Stack,
    aws_lambda as function_lambda
)
from constructs import Construct

class ChangedDirStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        demo_lambda_fn = function_lambda.Function(
            self, "DemoLambdaFunctionStack",
            function_name = "changed_dir_fn",
            runtime = function_lambda.Runtime.PYTHON_3_12,
            code = function_lambda.Code.from_asset('./function'),
            handler = "demo_function.changed_dir_fn"
        )
app = aws_cdk.App()
ChangedDirStack(app, "ChangedDirStack")
app.synth()