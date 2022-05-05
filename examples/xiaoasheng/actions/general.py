from rasa_sdk import Action
from rasa_sdk.events import UserUtteranceReverted, Restarted


# class ActionDefaultFallback(Action):
#     """Executes the fallback action and goes back to the previous state
#     of the dialogue"""
#     def name(self):
#         return 'action_default_fallback'
#
#     def run(self, dispatcher, tracker, domain):
#         text = tracker.latest_message.get('text')
#         print(f"action_default_fallback->text:{text}")
#         dispatcher.utter_template('utter_default', tracker, silent_fail=True)
#         return [UserUtteranceReverted()]


class ActionClearMemory(Action):
    """清除机器人当前会话的记忆"""
    def name(self):
        return 'action_clear_memory'

    def run(self, dispatcher, tracker, domain):
        print("清除机器人当前会话的记忆")
        dispatcher.utter_message(text="记忆清除")
        return [Restarted()]
