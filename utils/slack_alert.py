import requests

def send_slack_alert(summary_text, webhook_url):
    payload = {
        "text": f"🚨 *AI Alert Summary:*\n```{summary_text}```"
    }
    response = requests.post(webhook_url, json=payload)

    if response.status_code == 200:
        print("✅ Slack alert sent successfully.")
    else:
        print(f"❌ Slack alert failed: {response.status_code} - {response.text}")

