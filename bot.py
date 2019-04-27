import text_config as tc


class Bot:
    def __init__(self, implements):
        self.user_sessions = {}
        self.send_message = implements["send_message"]

    def got_location(self, location, user_id):
        pass

    def got_text_message(self, msg, user_id):
        if msg == tc.phys:
            self.user_sessions.update(user_id={'state': "service choice"})
            # self.user_sessions[user_id].state = "service choice"
            self.send_message(user_id, tc.service_list)

    def got_command(self, cmd, user_id, text):
        if cmd == "start":
            self.user_sessions.update(user_id={'state' : "service type"})
            self.send_message(user_id, tc.greeting)
        if cmd == "help":
            self.send_message(user_id, tc.help)

