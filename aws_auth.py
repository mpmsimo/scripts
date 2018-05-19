# msimo
# 5/17/17
# aws_auth

import boto3 as aws
from botocore.exceptions import ClientError

# Profile authentication - from config file
def profile_auth(pname, service):
    """Authenticate from a profile defined in credentials."""
    session = aws.Session(profile_name=pname)
    client = session.client(service)
    return client

if __name__ == "__main__":
    s3 = profile_auth('default', 's3')
    print(s3)
