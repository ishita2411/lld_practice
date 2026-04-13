from abc import ABC, abstractmethod

class NotificationAlertObserver(ABC):
    @abstractmethod
    def update(self):
        pass

class EmailAlertObserver(NotificationAlertObserver):
    def __init__(self, email, observable):
        self.email = email
        self.observable = observable
        # self.stockObservable.add(self)

    def update(self):
        print(f"Email Alert to {self.email}: iPhone is back in stock!")
    
class MobileAlertObserver(NotificationAlertObserver):
    def __init__(self, mobile_number, observable):
        self.mobile_number = mobile_number
        self.observable = observable
        # self.stockObservable.add(self).   this adds the obs to observable list here itself instead of doing it in main.

    def update(self):
        print(f"Mobile Alert to {self.mobile_number}: iPhone is back in stock!")
