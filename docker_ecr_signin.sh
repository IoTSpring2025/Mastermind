#!/bin/bash -e

account_id=$(aws sts get-caller-identity --query Account --output text)

aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin ${account_id}.dkr.ecr.us-east-2.amazonaws.com
