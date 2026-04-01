import boto3

print("🚀 Starting producer...")

# Create session with region
session = boto3.Session(region_name="ap-south-1")
sqs = session.client('sqs')

# Your queue URL
queue_url = "https://sqs.ap-south-1.amazonaws.com/551336603795/task-queue"

print("Using Queue:", queue_url)

try:
    # Send message
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody='fail this task'  # 🔥 This will trigger DLQ
    )

    print("✅ Message sent successfully!")
    print("Message ID:", response['MessageId'])

except Exception as e:
    print("❌ Error sending message:", e)