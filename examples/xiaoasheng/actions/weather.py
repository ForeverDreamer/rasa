from typing import Dict, Text, Any, List
from rasa_sdk import Tracker, Action
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher


class ActionWeatherForm(Action):
    def name(self) -> Text:
        """Unique identifier of the form"""
        return "action_weather_form"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
        after all required slots are filled"""
        address = tracker.get_slot('address')
        date_time = tracker.get_slot('date_time')
        print(f"action_weather_form->address:{address}")
        print(f"action_weather_form->date_time:{date_time}")
        dispatcher.utter_message("正在为你查询 {} {}的天气 ing".format(address, date_time))
        return [SlotSet("address", None), SlotSet("date_time", None)]
