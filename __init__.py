from mycroft import MycroftSkill, intent_file_handler


class MycroftPlayground(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('playground.mycroft.intent')
    def handle_playground_mycroft(self, message):
        self.speak_dialog('playground.mycroft')
        self.speak_dialog("yay hardcode!")

    def initialize(self):
        # Connecting Message Handler
        self.add_event("recognizer_loop:utterance", self.ensure_converse)
        self.add_event("mycroft.skill.handler.complete", self.handle_output)
        # Wait for user input
        self.make_active()

    def get_question(self, context):
        pass

    def handle_record(self, message):
        pass



def create_skill():
    return MycroftPlayground()