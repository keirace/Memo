from enum import Enum
from typing import Optional

class VehicleType(Enum):
    MOTORCYCLE = "Motorcycle"
    CAR = "Car"
    BUS = "Bus"

class SpotSize(Enum):
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"

class Vehicle:
    def __init__(self, license_plate: str, vehicle_type: VehicleType):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type

class ParkingSpot:
    def __init__(self, spot_id: str, size: SpotSize):
        self.spot_id = spot_id
        self.size = size
        self.vehicle = None

    def isAvailable(self) -> bool:
        # your code here
        return not self.vehicle

    def canFitVehicle(self, vehicle: Vehicle) -> bool:
        # your code here
        size_map = {
            VehicleType.MOTORCYCLE : SpotSize.SMALL,
            VehicleType.CAR : SpotSize.MEDIUM,
            VehicleType.BUS : SpotSize.LARGE,
        }
        return size_map[vehicle.vehicle_type] == self.size

    def parkVehicle(self, vehicle: Vehicle) -> bool:
        if self.isAvailable():
            self.vehicle = vehicle
            return True
        return False

    def removeVehicle(self) -> Optional[Vehicle]:
        vehicle = self.vehicle
        self.vehicle = None
        return vehicle

class ParkingLevel:
    def __init__(self, level_id: str, num_spots: int):
        self.level_id = level_id
        self.spots = [None] * num_spots
        self._initializeSpots(num_spots)

    def _initializeSpots(self, num_spots: int):
        # spot_id and size
        cur = 0
        small_count, medium_count = int(0.2 * num_spots), int(0.5 * num_spots)
        for _ in range(small_count): # 20% are small
            self.spots[cur] = ParkingSpot(f"{SpotSize.SMALL.value}_{cur+1}", SpotSize.SMALL)
            cur += 1
        for _ in range(medium_count): # 50% are medium
            self.spots[cur] = ParkingSpot(f"{SpotSize.MEDIUM.value}_{cur+1}", SpotSize.MEDIUM)
            cur += 1
        for _ in range(num_spots-(small_count+medium_count)): # 30% are large
            self.spots[cur] = ParkingSpot(f"{SpotSize.LARGE.value}_{cur+1}", SpotSize.LARGE)
            cur += 1

    def findAvailableSpot(self, vehicle: Vehicle) -> Optional[ParkingSpot]:
        for spot in self.spots:
            if spot.isAvailable() and spot.canFitVehicle(vehicle):
                return spot
        return None

    def getAvailableSpotsCount(self, vehicle_type: VehicleType) -> int:
        vehicle = Vehicle("", vehicle_type)
        return sum(1 for spot in self.spots if spot.isAvailable() and spot.canFitVehicle(vehicle))


class ParkingLot:
    def __init__(self, num_levels: int, spots_per_level: int):
        self.levels = [ParkingLevel(i+1, spots_per_level) for i in range(num_levels)] # initialize levels
        self.occupied = {} # license_plate: spot_id
        self.spot_map = {} # spot_id: ParkingSpot

    def parkVehicle(self, vehicle: Vehicle) -> bool:
        if vehicle.license_plate in self.occupied:
            return False
        for level in self.levels:
            spot = level.findAvailableSpot(vehicle)
            if spot and spot.parkVehicle(vehicle):
                self.occupied[vehicle.license_plate] = spot.spot_id
                self.spot_map[spot.spot_id] = spot  # Update the spot map
                return True
        return False
                
    def removeVehicle(self, license_plate: str) -> bool:
        if license_plate not in self.occupied:
            return False
        spot_id = self.occupied[license_plate]
        spot = self.spot_map[spot_id]
        if spot and spot.vehicle and spot.vehicle.license_plate == license_plate:
            spot.removeVehicle()
            del self.occupied[license_plate]

    def getAvailableSpots(self, vehicle_type: VehicleType) -> int:
        return sum(level.getAvailableSpotsCount(vehicle_type) for level in self.levels) 

v_car  = Vehicle("C123", VehicleType.CAR)
v_bus  = Vehicle("B999", VehicleType.BUS)
v_moto = Vehicle("M001", VehicleType.MOTORCYCLE)
lot = ParkingLot(2, 10)
lot.parkVehicle(v_car)
lot.parkVehicle(v_bus)
print(lot.getAvailableSpots(VehicleType.MOTORCYCLE))
lot.parkVehicle(v_moto)
lot.removeVehicle("C123")
print(lot.getAvailableSpots(VehicleType.CAR))