import boto3
import time

print("Worker started...")

# Create SQS client
sqs = boto3.client('sqs', region_name='ap-south-1')

# Your main queue URL
queue_url = "https://sqs.ap-south-1.amazonaws.com/551336603795/task-queue"

while True:
    print("Checking for messages...")

    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=1,
        WaitTimeSeconds=5  # long polling
    )

    messages = response.get('Messages', [])

    if not messages:
        print("No messages found...")
        continue

    for message in messages:
        try:
            body = message['Body']
            print("Processing:", body)

            # 🔥 Simulate failure for testing DLQ
            if "fail" in body.lower():
                raise Exception("Simulated failure triggered")

            # Simulate real processing
            time.sleep(3)

            print("Task completed ✅")

            # ✅ Delete message ONLY on success
            sqs.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=message['ReceiptHandle']
            )

            print("Message deleted ✅")

        except Exception as e:
            print("Error occurred:", e)
            print("Message will be retried and may go to DLQ ❌")

            # ❌ DO NOT delete message
            # This allows SQS to retry and eventually move to DLQ

    print("-" * 40)