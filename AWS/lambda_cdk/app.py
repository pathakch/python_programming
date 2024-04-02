import aws_cdk as cdk

from lambda_cdk.lambda_cdk_stack import LambdaCdkStack

app = cdk.App()
LambdaCdkStack(app, "LambdaCdkStack")

app.synth()