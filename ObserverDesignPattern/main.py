from observable import IphoneObservable
from observer import EmailAlertObserver, MobileAlertObserver

iphone_observable = IphoneObservable()
observer1 = EmailAlertObserver("user@example.com", iphone_observable)
observer2 = MobileAlertObserver("123-456-7890", iphone_observable)
observer3 = EmailAlertObserver("user2@example.com", iphone_observable)

iphone_observable.add(observer1)
iphone_observable.add(observer2)
iphone_observable.add(observer3)

iphone_observable.setStockCount(10)  # This should trigger notifications to all observers