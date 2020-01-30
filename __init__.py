import json
import os
from mycroft import MycroftSkill, intent_file_handler


class MycroftPlayground(MycroftSkill):

    def __init__(self):
        MycroftSkill.__init__(self)
        self.saving_user = {}
        self.helper_save = 0

    @intent_file_handler('playground.mycroft.intent')
    def handle_playground_mycroft(self, message):
        self.speak_dialog("Do you have a question?")

    def initialize(self):
        # Connecting Message Handler
        self.add_event("recognizer_loop:utterance", self.ensure_converse)
        self.add_event("mycroft.skill.handler.complete", self.skill_interaction_response)
        self.user_input = ""
        self.survey = []
        self.filepath = None
        self.ensure_converse()

    def ask_and_save(self,message,number):
        question= self.get_question(number)
        answer = self.ask_yesno(question)
        self.survey.append((self.user_input, question, answer, str(message.data)))
    def skill_interaction_response(self, message):
        self.ask_and_serve(message,1)
        self.ask_and_save(message,2)
        # self.speak_dialog(str(self.survey))
        survey_copy = self.survey.copy()
        with open(os.path.join(self.root_dir, 'log_file_ours.json'), 'w') as f:
            json.dump(survey_copy, f, indent=4, sort_keys=True)

    def get_question(self, number):
        question = {1: "Do you know you lost private information?",
                    2: "In your opinion which information got lost?"}
        return question[number]

    def ensure_converse(self, message=None):
        self.make_active()

    def converse(self, utterances, lang="en-us"):
        self.user_input = utterances[0]
        self.ensure_converse()
        return False


def create_skill():
    return MycroftPlayground()
