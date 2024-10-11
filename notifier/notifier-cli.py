import argparse
from notifier.notifier import Notifier


def parse_args():
    parser = argparse.ArgumentParser(description="Notifier CLI for sending notifications to various platforms.")

    # Global arguments for Notifier configuration
    parser.add_argument("--slack-webhook", type=str, help="Slack webhook URL")
    parser.add_argument("--discord-webhook", type=str, help="Discord webhook URL")
    parser.add_argument("--teams-webhook", type=str, help="Teams webhook URL")
    parser.add_argument("--pushover-token", type=str, help="Pushover token")
    parser.add_argument("--pushover-user", type=str, help="Pushover user key")
    parser.add_argument("--operator-id", type=str, help="Optional operator ID")
    parser.add_argument("--notifier-name", type=str, help="Notifier name for display")

    # Subcommands for different notification types
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Success notification subcommand
    success_parser = subparsers.add_parser("notify-success", help="Send a success notification")
    success_parser.add_argument("--taskname", type=str, required=True, help="Task name for the notification")
    success_parser.add_argument("--taskid", type=str, required=True, help="Task ID for the notification")
    success_parser.add_argument("--group", type=str, default="", help="Group name for the notification")
    success_parser.add_argument("--url", type=str, default="", help="URL for more details")

    # General update notification subcommand
    update_parser = subparsers.add_parser("notify-update", help="Send a general update notification")
    update_parser.add_argument("--message", type=str, required=True, help="Message content for the update")

    return parser.parse_args()


def main():
    args = parse_args()

    # Initialize the Notifier with provided arguments
    notifier = Notifier(
        slack_webhook=args.slack_webhook,
        discord_webhook=args.discord_webhook,
        teams_webhook=args.teams_webhook,
        pushover_token=args.pushover_token,
        pushover_user=args.pushover_user,
        operator_id=args.operator_id,
        notifier_name=args.notifier_name,
    )

    # Handle subcommands
    if args.command == "notify-success":
        notifier.notify_success(taskname=args.taskname, taskid=args.taskid, group=args.group, url=args.url)
        print("Success notification sent.")
    elif args.command == "notify-update":
        notifier.notify_update(message=args.message)
        print("Update notification sent.")
    else:
        print("Unknown command. Use --help for more information.")


if __name__ == "__main__":
    main()
