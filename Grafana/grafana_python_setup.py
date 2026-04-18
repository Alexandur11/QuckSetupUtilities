import json
import time
import os
import requests
from dotenv import load_dotenv

load_dotenv()

class GrafanaLogger:
    def __init__(self, service_name, env):
        self.service_name = service_name
        self.env = env
        self.headers = {"Content-Type": "application/json"}

    def send_log(self, log_message):
        payload = {
            "streams": [
                {
                    "stream": {"service_name": self.service_name, "env": self.env},
                    "values": [
                        [str(int(time.time() * 1e9)), log_message],
                    ],
                }
            ]
        }

        requests.post(
            url=os.environ.get("GRAFANA_URL"),
            auth=(
                os.environ.get("GRAFANA_USER_ID"),
                os.environ.get("GRAFANA_LOG_API_KEY"),
            ),
            headers=self.headers,
            data=json.dumps(payload),
        )
