Perfect! Let’s give your README a professional, visually appealing GitHub look with badges, code highlighting, and clean sectioning. Here’s the enhanced version:


---

Distributed-Task-System-Using-AWS
   
📌 Overview

A distributed task processing system built using AWS services.
It demonstrates how modern scalable systems handle asynchronous workloads using queues and auto scaling.

Users can send tasks via a web dashboard, which are placed into an SQS queue. Worker instances running on EC2 process these tasks dynamically based on system load.


🏗️ Architecture

Frontend (HTML/JS) → Flask API → Amazon SQS → EC2 Workers → Auto Scaling


⚙️ Features

🌐 Web-based dashboard to send tasks
📬 Amazon SQS for decoupled messaging
⚙️ Background worker processing system
📈 Auto Scaling based on queue load
🔁 Retry mechanism with failure handling (DLQ)
📊 Real-time queue monitoring
🚀 Fully deployed on AWS EC2  


🧠 How It Works

1. User clicks Send Task from UI
2. Request hits Flask API (/send)
3. Task is pushed to SQS queue
4. Worker instances poll the queue continuously
5. Tasks are processed asynchronously
6. Messages are deleted after success
7. CloudWatch monitors queue size
8. Auto Scaling adjusts EC2 instances dynamically

🛠️ Tech Stack

AWS: EC2, SQS, Auto Scaling, CloudWatch
Python: Flask, Boto3
Frontend: HTML, CSS, JavaScript  


📂 Project Structure

app.py        → API server
worker.py     → Background worker
index.html    → Frontend UI
send.py       → Load testing script
start.sh      → Startup script


🏆 Key Learnings

Distributed system design
Queue-based architecture
Auto scaling in cloud
Asynchronous processing
Debugging real-world systems


👨‍💻 Author

Bharath Vishnu B

