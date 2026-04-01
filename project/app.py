from flask import Flask, request, jsonify
from flask_cors import CORS
import boto3

app = Flask(__name__)
CORS(app)

# AWS SQS setup
sqs = boto3.client('sqs', region_name='ap-south-1')

queue_url = "https://sqs.ap-south-1.amazonaws.com/551336603795/task-queue"


@app.route('/')
def home():
    return "🚀 SQS Task API is running!"


@app.route('/send', methods=['POST'])
def send_task():
    try:
        data = request.json
        message = data.get('message', '')

        if not message:
            return jsonify({"error": "Message is required"}), 400

        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=message
        )

        return jsonify({
            "status": "success",
            "message_id": response['MessageId'],
            "sent_message": message
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# 🔥 NEW: QUEUE SIZE ENDPOINT
@app.route('/queue')
def queue_size():
    response = sqs.get_queue_attributes(
        QueueUrl=queue_url,
        AttributeNames=['ApproximateNumberOfMessages']
    )

    count = int(response['Attributes']['ApproximateNumberOfMessages'])

    return jsonify({"queue_size": count})


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)