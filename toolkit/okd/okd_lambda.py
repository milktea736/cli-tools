import json
import os
from typing import Dict, List

import boto3
from dotenv import load_dotenv

load_dotenv()

# okd cluster name
CLUSTER_NAME = os.getenv('CLUSTER_NAME')
BUCKET_NAME = os.getenv('BUCKET_NAME')
KEY_NAME = os.getenv('KEY_NAME')


def lambda_handler(event, context):
    "triggerd when okd-state/state.json get updated"
    owh = OkdWorkerHelper()
    owh.check()
    return {
        'statusCode': 200,
    }


class OkdWorkerHelper:

    def __init__(self) -> None:
        self.s3 = boto3.client('s3')
        self.ec2 = boto3.client('ec2')
        self.user_working_state = self._read_state_file()

    def check(self):
        if any(self.user_working_state.values()):
            self.ec2.start_instances(InstanceIds=self._get_worker_instances())
            print('=== Starting wokers ===')
        else:
            self.ec2.stop_instances(InstanceIds=self._get_worker_instances())
            print('=== Stoping workers ===')

    def _read_state_file(self) -> Dict[str, bool]:
        """
        return: {'user_A': bool, 'user_B': bool, ...}
        """
        obj = self.s3.get_object(Bucket=BUCKET_NAME, Key=KEY_NAME)['Body'].read().decode()

        return json.loads(obj)

    def _get_worker_instances(self) -> List[str]:
        """get a list of instance id"""
        response = self.ec2.describe_instances(Filters=[{'Name': 'tag:Name', 'Values': [f'{CLUSTER_NAME}*worker*']}])

        return [_['Instances'][0]['InstanceId'] for _ in response['Reservations']]
