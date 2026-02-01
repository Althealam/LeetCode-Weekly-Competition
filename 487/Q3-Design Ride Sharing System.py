from collections import deque
class RideSharingSystem:

    def __init__(self):
        self.rider_ids = deque()
        self.driver_ids = deque()

    def addRider(self, riderId: int) -> None:
        self.rider_ids.append(riderId)

    def addDriver(self, driverId: int) -> None:
        self.driver_ids.append(driverId)

    def matchDriverWithRider(self):
        if len(self.rider_ids)>=1 and len(self.driver_ids)>=1:
            return [self.driver_ids.popleft(), self.rider_ids.popleft()]
        return [-1, -1]

    def cancelRider(self, riderId: int) -> None:
        if riderId in self.rider_ids:
            self.rider_ids.remove(riderId)


obj = RideSharingSystem()
obj.addRider(3)
obj.addDriver(2)
obj.addRider(1)
print(obj.rider_ids.pop())
m1 = obj.matchDriverWithRider()
print(m1)
