from collections import defaultdict
from langchain_core.messages import HumanMessage, AIMessage

#memoria en RAM por chat por sesion


class ChatMemory:
    def __init__(self, max_turns: int = 5):
        self.store = defaultdict(list)
        self.max_turns = max_turns

    def add_user(self, session_id: str, text: str):
        self.store[session_id].append(HumanMessage(content=text))
        self._trim(session_id)

    def add_ai(self, session_id: str, text: str):
        self.store[session_id].append(AIMessage(content=text))
        self._trim(session_id)

    def get(self, session_id: str):
        return self.store[session_id]

    def _trim(self, session_id: str):
        if len(self.store[session_id]) > self.max_turns * 2:
            self.store[session_id] = self.store[session_id][-self.max_turns * 2:]