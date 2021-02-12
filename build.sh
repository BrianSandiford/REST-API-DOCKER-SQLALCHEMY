#!/bin/bash

echo "****************************"
echo "** Building Docker Image ***"
echo "****************************"

ansible-playbook -i hosts build.yml
