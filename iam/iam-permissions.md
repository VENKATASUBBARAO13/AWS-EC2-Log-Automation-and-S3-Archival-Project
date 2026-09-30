# IAM Permissions

The Lambda execution role needs permission to read the selected CloudWatch Log Group and write objects to the destination S3 bucket.

## Example Lambda policy

Replace the placeholders with your own AWS account, Region, log-group ARN, and bucket ARN.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ReadCloudWatchLogs",
      "Effect": "Allow",
      "Action": [
        "logs:FilterLogEvents",
        "logs:DescribeLogStreams",
        "logs:DescribeLogGroups"
      ],
      "Resource": "arn:aws:logs:<REGION>:<ACCOUNT_ID>:log-group:/aws/ec2/server-logs:*"
    },
    {
      "Sid": "WriteLogArchiveToS3",
      "Effect": "Allow",
      "Action": [
        "s3:PutObject"
      ],
      "Resource": "arn:aws:s3:::<BUCKET_NAME>/ec2-logs/*"
    }
  ]
}
```

The Lambda role should also include the AWS-managed basic execution policy required to write Lambda execution logs to CloudWatch Logs.

## EC2 role

For the CloudWatch Agent, attach an EC2 instance role with the permissions required by the CloudWatch Agent. Using an IAM role avoids storing AWS access keys on the instance.

## Security notes

- Replace all placeholders before deployment.
- Scope S3 permissions to the required bucket/prefix.
- Scope CloudWatch permissions to the required log group where practical.
- Never commit access keys, secret keys, tokens, or private credentials.
