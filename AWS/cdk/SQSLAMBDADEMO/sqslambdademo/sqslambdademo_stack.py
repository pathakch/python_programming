from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_iam as iam,
    aws_sqs as sqs,
    aws_lambda as lambda_,
    aws_lambda_event_sources as lambda_event_sources 
)

class SqslambdademoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        queue = sqs.Queue(
            self, "SqslambdademoQueue",
            visibility_timeout=Duration.seconds(300),
        )

        #create our lambda function
        sqs_lambda = lambda_.Function(self, "SQSLambda",handler = 'lambda_handler.lambda_handler',
                                      runtime = lambda_.Runtime.PYTHON_3_10,
                                      code = lambda_.Code.from_asset('lambda'))
        
        #create our event source
        sqs_event_source = lambda_event_sources.SqsEventSource(queue)

        # add sqs event source to lambda 
        sqs_lambda.add_event_source(sqs_event_source)
