# 🚗 AWS Bedrock Car Service Assistant Agent

This project demonstrates how to build a simple **Generative AI Agent** using **Amazon Bedrock** and **AWS Lambda**.  
The agent can:
- 🧠 Answer general car service questions using Claude Foundation Model
- 🔧 Fetch real car service data using a Lambda action

## 🧰 Tech Stack
- Amazon Bedrock (Claude 3 / Titan)
- AWS Lambda
- OpenAPI Schema for Actions
- Python 3.12

## 🪜 Setup Guide
1️⃣ Create Lambda Function  
2️⃣ Create Bedrock Agent  
3️⃣ Test the Agent  
4️⃣ Deploy and Use

## 📝 Architecture
User → Bedrock Agent → Claude Model + Lambda Action → Response

## 💼 Tip
This project is perfect to demonstrate:
- ✅ AWS Bedrock Agent setup
- ✅ Lambda integration with OpenAPI schema
- ✅ Realistic use case (car service)
- ✅ API deployment and testing

## 📝 Folder Structure
aws-bedrock-car-service-agent/
│
├── lambda/
│   ├── car_service_info/
│   │   ├── lambda_function.py
│   │   └── requirements.txt
│
├── agent/
│   ├── openapi_action_schema.json
│   ├── agent_instructions.md
│
├── docs/
│   ├── architecture-diagram.png
│   └── setup-guide.md
│
├── .gitignore
├── README.md
└── LICENSE


## 📜 License
MIT License
