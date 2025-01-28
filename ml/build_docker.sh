#!/bin/bash -xe

# make sure we build for amd64 so it can run on ec2 instance
docker build --platform linux/amd64 -t mastermind .
