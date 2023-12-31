import os
from slack_sdk import WebClient


class WebClient:
    SLACK_BOT_TOKEN = os.environ["ADA_SLACK_BOT_TOKEN"]
    client = WebClient(token=SLACK_BOT_TOKEN)

    def get_username_from_message(self, message):
        user_id = message["user"]
        user = self.client.users_info(user=user_id)
        user_name = user["user"]["profile"]["display_name_normalized"]
        return user_name
