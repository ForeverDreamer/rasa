from typing import Dict, Text, Any, List
from rasa_sdk import Tracker, Action
from rasa_sdk.events import UserUtteranceReverted, Restarted
from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.forms import FormAction
from requests import (
    ConnectionError,
    HTTPError,
    TooManyRedirects,
    Timeout
)

#
# # action weather_form
# class WeatherForm(FormAction):
#     def name(self) -> Text:
#         """Unique identifier of the form"""
#         return "weather_form"
#
#     @staticmethod
#     def required_slots(tracker: Tracker) -> List[Text]:
#         """A list of required slots that the form has to fill"""
#         return ["date_time", "address"]
#
#     def submit(
#             self,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any],
#     ) -> List[Dict]:
#         """Define what the form has to do
#         after all required slots are filled"""
#
#         address = tracker.get_slot('address')
#         date_time = tracker.get_slot('date-time')
#         print(f"action_default_fallback->address:{address}")
#         print(f"action_default_fallback->date_time:{date_time}")
#         dispatcher.utter_message("正在为你查询 {} {}的天气 ing".format(address, date_time))
#         return [Restarted()]


# action_default_fallback
class ActionDefaultFallback(Action):
    """Executes the fallback action and goes back to the previous state
    of the dialogue"""
    def name(self):
        return 'action_default_fallback'

    def run(self, dispatcher, tracker, domain):
        text = tracker.latest_message.get('text')
        print(f"action_default_fallback->text:{text}")
        dispatcher.utter_template('utter_default', tracker, silent_fail=True)
        return [UserUtteranceReverted()]
