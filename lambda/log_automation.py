"""AWS Lambda example for exporting CloudWatch Logs to Amazon S3.

Set these environment variables on the Lambda function:
- LOG_GROUP_NAME: CloudWatch Logs group to read
- S3_BUCKET_NAME: private S3 bucket used for archival
- S3_PREFIX: optional object prefix, defaults to ec2-logs
- LOOKBACK_MINUTES: optional lookback window, defaults to 5

This is a learning-project example. Review permissions and pagination,
retention, volume, and failure handling before production use.
"""

import json
import os
from datetime import datetime, timedelta, timezone

import boto3

logs = boto3.client("logs")
s3 = boto3.client("s3")

LOG_GROUP_NAME = os.environ["LOG_GROUP_NAME"]
S3_BUCKET_NAME = os.environ["S3_BUCKET_NAME"]
S3_PREFIX = os.environ.get("S3_PREFIX", "ec2-logs").strip("/")
LOOKBACK_MINUTES = int(os.environ.get("LOOKBACK_MINUTES", "5"))


def lambda_handler(event, context):
    end_time = datetime.now(timezone.utc)
    start_time = end_time - timedelta(minutes=LOOKBACK_MINUTES)

    start_ms = int(start_time.timestamp() * 1000)
    end_ms = int(end_time.timestamp() * 1000)

    events = []
    next_token = None

    while True:
        params = {
            "logGroupName": LOG_GROUP_NAME,
            "startTime": start_ms,
            "endTime": end_ms,
            "interleaved": True,
        }
        if next_token:
            params["nextToken"] = next_token

        response = logs.filter_log_events(**params)
        events.extend(response.get("events", []))
        new_token = response.get("nextToken")

        if not new_token or new_token == next_token:
            break
        next_token = new_token

    if not events:
        print("No new log events found in the configured lookback window.")
        return {
            "statusCode": 200,
            "message": "No new log events found",
            "events_exported": 0,
        }

    timestamp = end_time.strftime("%Y/%m/%d/%H%M%S")
    object_key = f"{S3_PREFIX}/{timestamp}-cloudwatch-logs.json"

    payload = {
        "log_group": LOG_GROUP_NAME,
        "exported_at": end_time.isoformat(),
        "lookback_minutes": LOOKBACK_MINUTES,
        "events": events,
    }

    s3.put_object(
        Bucket=S3_BUCKET_NAME,
        Key=object_key,
        Body=json.dumps(payload, default=str, indent=2).encode("utf-8"),
        ContentType="application/json",
        ServerSideEncryption="AES256",
    )

    print(f"Exported {len(events)} log events to s3://{S3_BUCKET_NAME}/{object_key}")

    return {
        "statusCode": 200,
        "message": "Logs exported successfully",
        "events_exported": len(events),
        "s3_key": object_key,
    }
