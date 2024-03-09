import boto3
ec2 = boto3.resource('ec2')

instances = ec2.create_instances(
        ImageId="ami-0e670eb768a5fc3d4",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="window_practice_instance"
    )

    