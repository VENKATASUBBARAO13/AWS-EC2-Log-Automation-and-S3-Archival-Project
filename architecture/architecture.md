# Architecture

## AWS Serverless Log Automation Pipeline

```text
┌──────────────────────┐
│   Amazon EC2         │
│  Linux Application   │
└──────────┬───────────┘
           │ log files
           ▼
┌──────────────────────┐
│  CloudWatch Agent    │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ CloudWatch Logs      │
│ /aws/ec2/server-logs │
└──────────┬───────────┘
           │
           │ read log events
           ▼
┌──────────────────────┐       ┌──────────────────────┐
│     AWS Lambda       │◄──────│   EventBridge        │
│ Python + Boto3       │       │ Scheduled trigger    │
└──────────┬───────────┘       └──────────────────────┘
           │
           │ PutObject
           ▼
┌──────────────────────┐
│      Amazon S3       │
│  Central Log Archive │
└──────────────────────┘

             IAM
   ┌─────────┼─────────┐
   ▼         ▼         ▼
  EC2      Lambda      S3
  Role      Role     Access
```

### Components

- **EC2:** produces the source server/application logs.
- **CloudWatch Agent:** collects selected log files.
- **CloudWatch Logs:** centralizes the collected events.
- **EventBridge:** invokes the Lambda function on a schedule.
- **Lambda:** retrieves recent CloudWatch events and creates an archive object.
- **S3:** stores the resulting log archive.
- **IAM:** controls access between the services.
