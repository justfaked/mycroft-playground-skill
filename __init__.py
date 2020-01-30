from mycroft import MycroftSkill, intent_file_handler
import json
import os
class MycroftPlayground(MycroftSkill):

    def __init__(self):
        MycroftSkill.__init__(self)
        self.saving_user={}
        self.helper_save=0
    @intent_file_handler('playground.mycroft.intent')
    def handle_playground_mycroft(self, message):
        self.speak_dialog(self.magic)
        self.speak_dialog("Do you have a question?")


    def initialize(self):
        # Connecting Message Handler
        self.add_event("recognizer_loop:utterance", self.ensure_converse)
        self.add_event("mycroft.skill.handler.complete", self.skill_interaction_response)
        self.magic = "I am a little lady, you know?"
        self.ensure_converse()

    def skill_interaction_response(self,message):
        # question=self.get_question()
        # self.speak_dialog(question)
        self.speak_dialog(str(message.data) + 'loss of info')

    def get_question(self):
        return "Do you know you lost private information?"

    def handle_record(self, message):
        pass

    def ensure_converse(self, message = None):
        self.make_active()

    def converse(self, utterances, lang="en-us"):
        utterance = utterances[0]
        self.saving_user[self.helper_save]=utterance
        self.speak_dialorg(utterance)
        # self.speak_dialog(json.dumps(self.saving_user))
        # self.speak_dialog(os.path.abspath())
        # print(json.dumps(self.saving_user))
        self.ensure_converse()


def create_skill():
    return MycroftPlayground()