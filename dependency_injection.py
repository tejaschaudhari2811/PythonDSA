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

import unittest

from unittest.mock import Mock

class TestUserService(unittest.TestCase):
    def test_notify_user(self):
        mock_service = Mock(spec=NotificationService)
        mock_email_service = Mock(spec=EmailService)

        user_service = UserService(mock_email_service)

        user_service.notify_user("Test Message")

        mock_email_service.send.assert_called_once_with("Test Message")

unittest.main()