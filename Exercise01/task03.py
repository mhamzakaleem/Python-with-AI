class User:
    def __init__(self, name):
        self.name = name

class Message:
    def __init__(self, sender, text):
        self.sender = sender
        self.text = text

class ChatRoom:
    def __init__(self):
        self.users = []
        self.messages = []

    def join(self, user):
        self.users.append(user)
        print(user.name, "joined the chat")

    def leave(self, user):
        self.users.remove(user)
        print(user.name, "left the chat")

    def send_message(self, message):
        self.messages.append(message)
        print(message.sender.name + ":", message.text)

    def show_history(self):
        print("\nChat History:")
        for msg in self.messages:
            print(msg.sender.name + ":", msg.text)

user1 = User("Hamza")
user2 = User("Usman")
chat = ChatRoom()
chat.join(user1)
chat.join(user2)

msg1 = Message(user1, "Hello!")
chat.send_message(msg1)
msg2 = Message(user2, "Hi Hamza!")
chat.send_message(msg2)
chat.show_history()
chat.leave(user1)