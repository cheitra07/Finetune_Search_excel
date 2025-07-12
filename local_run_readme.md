Step-by-Step Setup in Cursor IDE
In Cursor:

    Open a new folder: machine-parts-repair-assistant

    Create this folder structure:

    machine-parts-repair-assistant/
├── data/
│   └── machine_parts.xlsx
├── app/
│   ├── ui_streamlit.py
│   └── backend_rag.py
├── deploy/
│   ├── lambda_handler.py
│   └── bedrock_config.py
├── requirements.txt
└── .env

2. Install Dependencies

Open the integrated terminal in Cursor IDE and run:
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

pip install -r requirements.txt

3. Set Up AWS Bedrock Access

Create a .env file at the root:
AWS_ACCESS_KEY_ID=YOUR_KEY
AWS_SECRET_ACCESS_KEY=YOUR_SECRET
AWS_REGION=us-east-1

4. Run Streamlit UI Locally

Use this terminal command:
streamlit run app/ui_streamlit.py

Then open your browser:
👉 http://localhost:8501

Type "gear pump leakage" and test the GenAI response.

5. Test Bedrock Integration
In backend_rag.py, ensure this line has your correct model:
llm = Bedrock(model_id="anthropic.claude-v2")  # Use supported Bedrock model

Confirm output appears below the input box.

6.Optional: Simulate Lambda in Cursor
To test lambda_handler.py locally, you can simulate:
event = {"queryStringParameters": {"query": "gear pump"}}
response = lambda_handler(event, None)
print(response['body'])
