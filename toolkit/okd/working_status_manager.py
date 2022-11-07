import json
from typing import Dict

import boto3

USERS = ['Ivan', 'Jacky', 'Amber', 'Square']
# okd cluster name
CLUSTER_NAME = 'csc'
BUCKET_NAME = 'lab-micro-cluster'
KEY_NAME = 'okd-state/state.json'


class WorkingStatusManger:

    def __init__(self) -> None:
        self.s3 = boto3.client('s3')

    def force_shutdown(self):
        working_status = {user: False for user in USERS}
        self.s3.put_object(Bucket=BUCKET_NAME, Key=KEY_NAME, Body=json.dumps(working_status).encode('utf-8'))

    def _read_state_file(self) -> Dict[str, bool]:
        """
        return: {'user_A': bool, 'user_B': bool, ...}
        """
        obj = self.s3.get_object(Bucket=BUCKET_NAME, Key=KEY_NAME)['Body'].read().decode()
        return json.loads(obj)

    def udpate(self, user: str, is_working: bool):
        working_status = self._read_state_file()
        working_status[user] = is_working

        self.s3.put_object(Bucket=BUCKET_NAME, Key=KEY_NAME, Body=json.dumps(working_status).encode('utf-8'))

    def show_working_status(self):
        print(json.dumps(self._read_state_file(), indent=4))
