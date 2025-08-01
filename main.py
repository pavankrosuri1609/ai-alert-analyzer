import json
from analyzer.parse_logs import load_logs, extract_errors
from analyzer.summarize import summarize_errors
from utils.slack_alert import send_slack_alert


def save_summary(summary_text, output_path="output/summary.json"):
    result = {
        "incident_summary": summary_text,
        "generated_by": "AI Alert Analyzer",
        "version": "v1.0"
    }
    with open(output_path, "w") as f:
        json.dump(result, f, indent=2)
    print(f"\n✅ Summary saved to {output_path}")

if __name__ == "__main__":
    logs = load_logs("logs/sample_mq_logs.json")
    errors = extract_errors(logs)

    if not errors:
        print("✅ No error logs found.")
    else:
        print("🧠 Extracted Errors:")
        for e in errors:
            print("-", e)

        summary = summarize_errors(errors)
        print("\n🚨 AI-Generated Summary:")
        print(summary)
        save_summary(summary)
        slack_webhook = #Slack Webhook URL
        send_slack_alert(summary, slack_webhook)
