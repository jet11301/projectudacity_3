#! /bin/bash
HUNGTH1_CLUSTER_NAME=$1
HUNGTH1_REGION=$2
eksctl create cluster --name "$HUNGTH1_CLUSTER_NAME" --region="$HUNGTH1_REGION" --nodes-min=2 --nodes-max=3
aws eks update-kubeconfig --region "$HUNGTH1_REGION" --name "$HUNGTH1_CLUSTER_NAME"  