import moto
import boto3
from moto import mock_ecr
import json
from test_ecr_helpers import (
    _create_image_manifest,
)

@mock_ecr
def test_put_image():
    client = boto3.client(
        'ecr',
        aws_access_key_id='ACCESS_KEY',
        aws_secret_access_key='SECRET_KEY',
        aws_session_token='SESSION_TOKEN',
        region_name="us-east-1"
    )
    _ = client.create_repository(repositoryName="test_repository")

    response = client.put_image(
        registryId='string',
        repositoryName='test_repository',    #mandatory
        imageManifest=json.dumps(_create_image_manifest()),     #mandatory
        imageTag='latest',
    )
    response["image"]["imageId"]["imageTag"].should.equal("latest")
    response["image"]["imageId"]["imageDigest"].should.contain("sha")
    response["image"]["repositoryName"].should.equal("test_repository")
    response["image"]["registryId"].should.equal('ACCOUNT_ID')
