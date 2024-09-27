import json

import boto3

from modules.tools.logger.logger import logger as log


class S3Client:
    def __init__(self):
        self.s3 = boto3.client('s3')
        self.bucket = 'teams-generator'

    def get_teams(self, resource_name):
        log.info("Get teams from bucket")
        response = self.s3.get_object(Bucket=self.bucket, Key=resource_name)
        content = response['Body']
        content_json = json.loads(content.read())
        return (content_json.get('teams', {}), content_json.get('errors', {}))
