# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

def get_json_key(dict, key):
    try:
        key_split = key.split(".", 1)
        key_split_len = len(key_split)
        if key_split_len == 2:
            return get_json_key(dict[key_split[0]], key_split[1])
        elif key_split_len == 1:
            return dict[key_split[0]]
    except:
        return None
    return None

class ActionChatID(Action):

    def name(self) -> Text:
        return "action_chatid"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        chat_id = get_json_key(tracker.latest_message, "metadata.message.chat.id")
        reply_to_message_id = get_json_key(tracker.latest_message, "metadata.message.message_id")
        json_message = {"text": chat_id, "reply_to_message_id": reply_to_message_id}
        dispatcher.utter_message(json_message=json_message)

        return []
