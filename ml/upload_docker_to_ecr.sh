#!/bin/bash -e

docker tag mastermind:latest 982534359879.dkr.ecr.us-east-2.amazonaws.com/mastermind:latest

docker push 982534359879.dkr.ecr.us-east-2.amazonaws.com/mastermind:latest
