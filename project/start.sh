  
  GNU nano 7.2                               start.sh
#!/bin/bash
cd /home/ubuntu

# activate env
source myenv/bin/activate

# start API
nohup python3 app.py > api.log 2>&1 &

# start worker
nohup python3 worker.py > worker.log 2>&1 &

# start frontend
nohup sudo python3 -m http.server 80 > web.log 2>&1 &
