class Bot:
    def __init__(self, implements):
        self.user_sessions = []
        self.send_message = implements.send_message

    def got_location(self, location):
        pass

    def got_text_message(self, msg):



    def got_command(self, cmd, user_id, text):
        if cmd == "start":
            self.user_sessions.append({'id': id})
            self.send_message(user_id, "Hello!")

