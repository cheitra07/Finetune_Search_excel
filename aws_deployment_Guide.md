Deployment on AWS (Lambda + Bedrock + S3 + API Gateway)

This guide explains how to deploy the Machine Parts RAG Repair Assistant using AWS Lambda, S3, API Gateway, and Bedrock.

1. Lambda Layer Setup (for dependencies)

AWS Lambda doesn’t support large libraries directly in your main function. You need to use Lambda Layers to include:

    langchain

    pandas

    faiss-cpu

    boto3

    openpyxl

🛠️ Steps:

On your local system or EC2 instance:

mkdir python
pip install langchain boto3 faiss-cpu pandas openpyxl -t python/
zip -r lambda-layer.zip python

2. Upload Excel File to S3

Call this before loading the Excel:

EXCEL_FILE_PATH = download_excel_from_s3()

Your repair data Excel file (machine_parts.xlsx) must be accessible to Lambda.
🛠️ Steps:

Upload machine_parts.xlsx to an S3 bucket (e.g. cheitra-machine-parts)

In lambda_handler.py, add this:

import boto3

def download_excel_from_s3():
    s3 = boto3.client('s3')
    bucket = "cheitra-machine-parts"
    key = "machine_parts.xlsx"
    download_path = "/tmp/machine_parts.xlsx"
    s3.download_file(bucket, key, download_path)
    return download_path

 3. API Gateway Setup

 Expose the Lambda via REST API.
🛠️ Steps:

    Go to AWS → API Gateway → Create new REST API

    Create resource /query

    Add GET method:

        Integration type: Lambda Function

        Enable CORS

    Deploy API to a stage (e.g., prod)

    Call like:

GET https://your-api-id.execute-api.region.amazonaws.com/prod/query?query=gear+oil+leak

4. IAM Role Permissions for Lambda
Ensure your Lambda’s execution role has permissions for:
📜 Minimum IAM Policy:

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream"
      ],
      "Resource": "*"
    }
  ]
}
You can scope it to your S3 bucket and Bedrock model ARN if you want to be strict.
**********************************************
5. Environment Variables (Optional)
Set your AWS region as an env var:

| Key          | Value       |
| ------------ | ----------- |
| `AWS_REGION` | `us-east-1` |


6. Test the End-to-End Flow

 Test Lambda with test query in console

✅ Test API Gateway: hit the endpoint in browser or Postman

✅ Output: Should return repair instructions based on your Excel file

Example Project Tree (Deployment Files Only)
deploy/
├── bedrock_config.py
├── lambda_handler.py
├── README.md
├── lambda-layer.zip (local)
├── lambda-policy.json
