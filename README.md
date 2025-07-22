# Discord Role Messenger Bot

This is a simple Discord bot that can send a message to all members with a specific role in a server.

## Setup

1.  **Create a Discord bot application:**
    *   Go to the [Discord Developer Portal](https://discord.com/developers/applications).
    *   Click on "New Application".
    *   Give your application a name and click "Create".
    *   Go to the "Bot" tab and click "Add Bot".
    *   Click "Yes, do it!".

2.  **Get your bot token:**
    *   In the "Bot" tab, you will find your bot's token. Click "Copy" to copy the token.
    *   **Important:** Do not share this token with anyone.

3.  **Invite the bot to your server:**
    *   Go to the "OAuth2" tab.
    *   In the "Scopes" section, select "bot".
    *   In the "Bot Permissions" section, select "Send Messages".
    *   Copy the URL that is generated and paste it into your browser.
    *   Select the server you want to add the bot to and click "Authorize".

4.  **Install the required libraries:**
    ```
    pip install discord.py
    ```

5.  **Run the bot:**
    *   Open the `discord_bot.py` file and replace `"YOUR_BOT_TOKEN"` with your actual bot token.
    *   Run the bot from your terminal:
        ```
        python discord_bot.py
        ```

## Usage

To send a message to a role, use the following command in your server:

```
!message_role @<role_name> <message>
```

For example:

```
!message_role @everyone Hello everyone!
```
