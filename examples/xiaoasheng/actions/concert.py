from rasa_sdk import Action
from rasa_sdk.events import SlotSet


class ActionSearchConcerts(Action):
    def name(self):
        return "action_search_concerts"

    def run(self, dispatcher, tracker, domain):
        concerts = [
            {"artist": "喷火战机", "reviews": 4.5},
            {"artist": "凯蒂·派瑞", "reviews": 5.0},
        ]
        description = ", ".join([c["artist"] for c in concerts])
        dispatcher.utter_message(text=f"{description}")
        return [SlotSet("concerts", concerts)]


class ActionSearchVenues(Action):
    def name(self):
        return "action_search_venues"

    def run(self, dispatcher, tracker, domain):
        venues = [
            {"name": "罗马大斗兽场", "reviews": 4.5},
            {"name": "岩石地窖", "reviews": 5.0},
        ]
        dispatcher.utter_message(text="这是我找到的一些场地")
        description = ", ".join([c["name"] for c in venues])
        dispatcher.utter_message(text=f"{description}")
        return [SlotSet("venues", venues)]


class ActionShowConcertReviews(Action):
    def name(self):
        return "action_show_concert_reviews"

    def run(self, dispatcher, tracker, domain):
        concerts = tracker.get_slot("concerts")
        dispatcher.utter_message(text=f"音乐会评价比较: {concerts}")
        return []


class ActionShowVenueReviews(Action):
    def name(self):
        return "action_show_venue_reviews"

    def run(self, dispatcher, tracker, domain):
        venues = tracker.get_slot("venues")
        dispatcher.utter_message(text=f"场地评价比较: {venues}")
        return []


# class ActionSetMusicPreference(Action):
#     def name(self):
#         return "action_set_music_preference"
#
#     def run(self, dispatcher, tracker, domain):
#         """Sets the slot 'likes_music' to true/false dependent on whether the user
#         likes music"""
#         intent = tracker.latest_message["intent"].get("name")
#
#         if intent == "affirm":
#             return [SlotSet("likes_music", True)]
#         elif intent == "deny":
#             return [SlotSet("likes_music", False)]
#         return []
