from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

class EmailService(NotificationService):
    def send(self, message: str):
        print(f"Sending email: {message}")

class SMSService(NotificationService):
    def send(self, message: str):
        print(f"Sending SMS: {message}")

class UserService:
    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service
    
    def notify_user(self, message: str):
        self.notification_service.send(message)

email_service = SMSService()
user1 = UserService(email_service)
user1.notify_user("Tejas is Here. Run!!1")