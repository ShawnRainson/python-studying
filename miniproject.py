#Homework
class Notification:
    def __init__(self, recipient):
        self.recipient = recipient

    def send(self):
        return "Sending "

class EmailNotification(Notification):
    def __init__(self, recipient):
        super().__init__(recipient)

    def send(self):
        return super().send() + "Email"

    def __str__(self):
        return f"{self.recipient} got a new Email."
    
class SMSNotification(Notification):
    def __init__(self, recipient):
        super().__init__(recipient)

    def send(self):
        return super().send() + "SMS"

    def __str__(self):
        return f"{self.recipient} got a new SMS."

rec1 = EmailNotification("Mia")
rec2 = SMSNotification("Rachel")
print(rec1)
print(rec2)

notifications = [rec1, rec2]
for notification in notifications:
    print(notification.send())


        