import os
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY"),
)

def summarize_errors(errors):
    joined = "\n".join(errors)

    prompt = f"""
You are a log analysis assistant for MQ systems. Analyze the following logs, identify affected partners, detect patterns like timeouts or unreachable hosts, and summarize the root cause clearly in ONE line.

Be specific:
- Mention the partner(s)
- Mention reason (timeout, communication error, etc.)
- Optionally, suggest fix

Logs:
{joined}

Summary:
"""

    response = client.chat.completions.create(
        model="deepseek/deepseek-r1-0528-qwen3-8b:free",
        messages=[
            {"role": "user", "content": prompt}
        ],
        extra_headers={
            "HTTP-Referer": "https://github.com/pavankrosuri",
            "X-Title": "AI Alert Analyzer"
        }
    )

    return response.choices[0].message.content.strip()
if __name__ == "__main__":
    sample = [
        "AMQ9206: Error sending data to host 'MQHOST1 (10.11.12.13)'.",
        "EXPLANATION: Communication failure with MQHOST1.",
        "AMQ9510: Messages cannot be retrieved from a queue.",
        "EXPLANATION: Attempt to get messages from queue 'INPUT.QUEUE' on queue manager 'MQ.QM1' failed with reason code 2053.",
        "Transfer failed: MQ timeout - PartnerA",
        "Transfer failed: MQ timeout - PartnerB"
    ]

    result = summarize_errors(sample)
    print("🚨 AI-Generated Summary:")
    print(result)

