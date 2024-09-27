import io

import boto3

from modules.tools.logger.logger import logger as log


class S3Client:
    def __init__(self):
        self.s3 = boto3.client('s3')
        self.bucket = 'teams-generator'

    def upload_teams(self, resource_name, body):
        log.info("Upload teams to bucket")
        res = self.s3.upload_fileobj(
            io.BytesIO(body.encode("utf-8")), Bucket=self.bucket, Key=resource_name
        )
        return res
