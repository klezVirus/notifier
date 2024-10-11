# Notifier Project

The `Notifier` project is a simple Python tool designed to send notifications to various platforms, such as Slack, Discord, Microsoft Teams, and Pushover. This utility helps integrate notification alerts into your workflow by providing a unified interface to send messages or updates to multiple platforms simultaneously.

## Features
- **Send notifications to multiple platforms**: Slack, Discord, Microsoft Teams, and Pushover.
- **Unified messaging**: Supports sending success notifications or general log entries.
- **Customizable**: Configure which platforms to send to, customize the message format, and include additional metadata like operator IDs.

## Installation
To install the required dependencies, use the following command:

```bash
pip install requests discordwebhook
```

## Usage
### Code Example

Below is a basic example of how to use the `Notifier` class:

```python
from notifier import Notifier

# Create an instance of Notifier with desired webhook URLs
notifier = Notifier(
    slack_webhook="https://hooks.slack.com/services/SLACK/WEBHOOK/URL",
    discord_webhook="https://discord.com/api/webhooks/DISCORD/WEBHOOK/URL",
    teams_webhook="https://outlook.office.com/webhook/TEAMS/WEBHOOK/URL",
    pushover_token="YOUR_PUSHOVER_TOKEN",
    pushover_user="YOUR_PUSHOVER_USER",
    notifier_name="MyNotifier",
    operator_id="1234"
)

# Send a success notification
notifier.notify_success(taskname="Task1", taskid="001", group="Operations", url="https://tasktracker.example.com/001")

# Send a general update message
notifier.notify_update(message="Daily Status: All systems operational.")
```

### CLI Usage
A command-line interface (CLI) is also available to send notifications directly from the terminal.

```bash
python notifier_cli.py <command> [options]
```

#### Available Commands
1. **Send Success Notification**:

   ```bash
   python notifier_cli.py notify-success --taskname "BackupJob" --taskid "1234" --group "BackupGroup" --url "https://tracker.example.com/1234"
   ```

2. **Send General Update**:

   ```bash
   python notifier_cli.py notify-update --message "Server health check: All services running."
   ```

## Configuration
The notifier can be configured with the following arguments:

- **slack_webhook**: The webhook URL for Slack.
- **discord_webhook**: The webhook URL for Discord.
- **teams_webhook**: The webhook URL for Microsoft Teams.
- **pushover_token**: The Pushover API token.
- **pushover_user**: The Pushover user key.
- **operator_id**: An optional operator ID to include in the notifications.
- **notifier_name**: The name of the notifier to be displayed in the messages.

## Requirements
- `requests`
- `discordwebhook`

## License
This project is licensed under the MIT License.
