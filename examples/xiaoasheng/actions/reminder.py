# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for an assistant that schedules reminders and
# reacts to external events.

from typing import Any, Text, Dict, List
import datetime

from rasa_sdk import Action, Tracker
from rasa_sdk.events import ReminderScheduled, ReminderCancelled, SlotSet
from rasa_sdk.executor import CollectingDispatcher


class ActionSetReminder(Action):
    """Schedules a reminder, supplied with the last message's entities."""

    def name(self) -> Text:
        return "action_set_reminder"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        intent_name = tracker.get_slot("intent_name")
        dispatcher.utter_message(f"我10秒钟之后提醒您<{intent_name}>.")

        date = datetime.datetime.now() + datetime.timedelta(seconds=10)
        entities = tracker.latest_message.get("entities")

        reminder = ReminderScheduled(
            intent_name=intent_name,
            trigger_date_time=date,
            entities=entities,
            # name="my_reminder",
            kill_on_user_message=False,
        )

        return [reminder]


class ForgetReminders(Action):
    """Cancels all reminders."""

    def name(self) -> Text:
        return "action_forget_reminders"

    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        intent_name = tracker.get_slot("intent_name")
        dispatcher.utter_message(f"好的取消提醒<{intent_name}>.")

        # Cancel all reminders
        return [ReminderCancelled(intent_name=intent_name)]


class ActionReactToCallReminder(Action):
    """Reminds the user to call someone."""

    def name(self) -> Text:
        return "action_react_to_call_reminder"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("person")
        dispatcher.utter_message(f"记得给<{name}>打电话哦!")

        return [SlotSet("intent_name", None), SlotSet("person", None)]


class ActionReactToWaterDry(Action):
    """Informs the user that a plant needs water."""

    def name(self) -> Text:
        return "action_react_to_water_dry"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        plant = next(tracker.get_latest_entity_values("plant"), "<plant_name>")
        dispatcher.utter_message(f"你的<{plant}>口渴了!")

        return [SlotSet("intent_name", None), SlotSet("plant", None)]


class ActionTellID(Action):
    """Informs the user about the conversation ID."""

    def name(self) -> Text:
        return "action_tell_id"

    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        conversation_id = tracker.sender_id

        dispatcher.utter_message(f"The ID of this conversation is '{conversation_id}'.")
        dispatcher.utter_message(
            f"Trigger an intent with: \n"
            f'curl -H "Content-Type: application/json" '
            f'-X POST -d \'{{"name": "EXTERNAL_dry_plant", '
            f'"entities": {{"plant": "Orchid"}}}}\' '
            f'"http://localhost:5005/conversations/{conversation_id}'
            f'/trigger_intent?output_channel=latest"'
        )

        return []