from mycroft import MycroftSkill, intent_file_handler


class MycroftPlayground(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

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
        self.speak_dialog(message.data['utterances'] + 'loss of info')

    def get_question(self):
        return "Do you know you lost private information?"

    def handle_record(self, message):
        pass

    def ensure_converse(self, message = None):
        self.make_active()




def create_skill():
    return MycroftPlayground()