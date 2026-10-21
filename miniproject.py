class Notification:
    def __init__(self, recipient):
        self.recipient = recipient

    def send(self):
        return f"Sending notification for {self.recipient}"

    def __str__(self):
        return f"Notification for {self.recipient}"

    def change_recipient(self, new_recipient):
        new_recipient = new_recipient.strip()
        if not new_recipient.strip():
            raise ValueError("Recipient cannot be empty")
        self.recipient = new_recipient

class EmailNotification(Notification):
    def send(self):
        return f"Sending Email to {self.recipient}"

    def __str__(self):
        return "Email " + super().__str__()
    
class SMSNotification(Notification):
    def send(self):
        return f"Sending SMS to {self.recipient}"

    def __str__(self):
        return "SMS " + super().__str__()

notes = [SMSNotification("Mia"), EmailNotification("Alex"), EmailNotification("Rachel")]
for note in notes:
    print(note.send())

recipient = EmailNotification("Mike")
recipient.change_recipient("Antony")
print(recipient)