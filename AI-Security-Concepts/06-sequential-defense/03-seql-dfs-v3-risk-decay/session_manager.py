import time

class SessionManager:
    def __init__(self):
        self.sessions = {}

    def get_session(self, user_id):
        if user_id not in self.sessions:
            self.sessions[user_id] = {
                "messages": [],
                "intents": [],
                "risks": [],
                "timestamps": []   # 🔥 ADD THIS
            }
        return self.sessions[user_id]

    def update_session(self, user_id, message, intent, risk):
        session = self.get_session(user_id)

        session["messages"].append(message)
        session["intents"].append(intent)
        session["risks"].append(risk)
        session["timestamps"].append(time.time())  # 🔥 ADD THIS

        return session