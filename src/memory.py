"""
=========================================================
Conversation Memory
Research Paper Expert Chatbot
=========================================================
"""

from collections import deque


class ConversationMemory:

    def __init__(self, max_history=5):

        self.history = deque(maxlen=max_history)

    def add(self, question, answer):

        self.history.append({

            "question": question,

            "answer": answer

        })

    def get_context(self):

        if len(self.history) == 0:

            return ""

        context = ""

        for item in self.history:

            context += f"""
User: {item['question']}

Assistant: {item['answer']}

"""

        return context

    def clear(self):

        self.history.clear()

    def get_history(self):

        return list(self.history)


memory = ConversationMemory()