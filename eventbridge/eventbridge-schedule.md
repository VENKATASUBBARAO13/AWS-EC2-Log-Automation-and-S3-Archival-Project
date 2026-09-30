# EventBridge Schedule

Use an Amazon EventBridge Scheduler or scheduled EventBridge rule to invoke the Lambda function periodically.

## Example

```text
rate(5 minutes)
```

The schedule is only an example. Choose an interval based on log volume and the required archive frequency.

## Configuration

1. Create a scheduled EventBridge rule/schedule.
2. Select the Lambda function as the target.
3. Allow EventBridge to invoke the Lambda function.
4. Enable the schedule.
5. Check Lambda CloudWatch Logs after an invocation.
6. Verify the expected object appears in the S3 bucket.

## Test

You can also invoke the Lambda function manually from the Lambda console with an empty JSON event:

```json
{}
```
