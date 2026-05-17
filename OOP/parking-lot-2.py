from abc import ABCMeta
from enum import Enum
from datetime import datetime
import time


class VehicleType(Enum):
    CAR = 1
    TRUCK = 2
    ELECTRIC = 3
    VAN = 4
    MOTORCYCLE = 5


class Vehicle(metaclass=ABCMeta):
    def __init__(
        self,
        license_number: str,
        vehicle_type: VehicleType,
        assigned_ticket: ParkingTicket = None,
    ):
        self.__license_number = license_number
        self.__vehicle_type = vehicle_type
        self.__assigned_ticket = None

    @property
    def license_number(self):
        return self.__license_number

    @property
    def vehicle_type(self):
        return self.__vehicle_type

    @property
    def assigned_ticket(self):
        return self.__assigned_ticket

    @assigned_ticket.setter
    def assigned_ticket(self, ticket: ParkingTicket):
        self.__assigned_ticket = ParkingTicket


class Car(Vehicle):
    def __init__(self, license_number: str):
        super().__init__(license_number, VehicleType.CAR)


class Truck(Vehicle):
    def __init__(self, license_number: str):
        super().__init__(license_number, VehicleType.TRUCK)


class ElectricVehicle(Vehicle):
    def __init__(self, license_number: str):
        super().__init__(license_number, VehicleType.ELECTRIC)


class Van(Vehicle):
    def __init__(self, license_number: str):
        super().__init__(license_number, VehicleType.VAN)


class Motorcycle(Vehicle):
    def __init__(self, license_number: str):
        super().__init__(license_number, VehicleType.MOTORCYCLE)


class ParkingSpotType(Enum):
    HANDICAPPED = 1
    COMPACT = 2
    LARGE = 3
    MOTORCYCLE = 4
    ELECTRIC = 5


class ParkingSpot(metaclass=ABCMeta):
    def __init__(
        self, lot_number: str, spot_type: ParkingSpotType, curr_vehicle: Vehicle = None
    ):
        self.__lot_number = lot_number
        self.__curr_vehicle = curr_vehicle
        self.__spot_type = spot_type

    @property
    def license_number(self):
        return self.__lot_number

    @property
    def curr_vehicle(self):
        if self.__curr_vehicle == None:
            print("This parking spot is not currently occupied")
        else:
            print(f"This parking spot is currently occupied by {self.__curr_vehicle}")
        return self.__curr_vehicle

    _ALLOWED_SPOTS = {
        VehicleType.TRUCK: {ParkingSpotType.LARGE},
        VehicleType.VAN: {ParkingSpotType.LARGE},
        VehicleType.MOTORCYCLE: {ParkingSpotType.MOTORCYCLE},
        VehicleType.CAR: {ParkingSpotType.COMPACT},
        VehicleType.ELECTRIC: {ParkingSpotType.ELECTRIC},
    }

    def fits(self, new_vehicle: Vehicle) -> bool:
        if new_vehicle.has_handicap_registration():
            return self.__spot_type == ParkingSpotType.HANDICAPPED
        return self.__spot_type in self._ALLOWED_SPOTS.get(
            new_vehicle.vehicle_type, set()
        )


class Handicapped(ParkingSpot):
    def __init__(self, lot_number: str):
        super().__init__(lot_number, ParkingSpotType.HANDICAPPED)


class Compact(ParkingSpot):
    def __init__(self, lot_number: str):
        super().__init__(lot_number, ParkingSpotType.COMPACT)


class Large(ParkingSpot):
    def __init__(self, lot_number: str):
        super().__init__(lot_number, ParkingSpotType.LARGE)


class Motorcycle(ParkingSpot):
    def __init__(self, lot_number: str):
        super().__init__(lot_number, ParkingSpotType.MOTORCYCLE)


class ElectricSpot(ParkingSpot):
    def __init__(self, lot_number: str):
        super().__init__(lot_number, ParkingSpotType.ELECTRIC)


PAYMENT_TIMEOUT = 120
PAYMENT_POLLING_INTERVAL = 2


class ParkingLot:
    __floors: dict[int, list[ParkingSpot]]
    __entrance_panels: dict
    __exit_panels: dict

    # this should be triggered only at one of the entrance_panels
    def collect_parking_ticket(self, vehicle: Vehicle) -> ParkingTicket:
        new_ticket = ParkingTicket()
        vehicle.assigned_ticket = new_ticket
        return new_ticket

    # this should be triggered from one of the exit_panels, a ParkingAttendant or at the CustomerPortal
    def pay_parking_ticket(self, vehicle: Vehicle) -> int:
        curr_ticket = vehicle.assigned_ticket
        if curr_ticket.status == ParkingTicketStatus.PAID:
            return
        cost = curr_ticket.calculate_cost()

        ## integrates with some paynow...
        show_payment_info(cost)
        retrieve_payment(cost)  # cash or credit
        ## wait for payment
        payment_deadline = datetime.now + PAYMENT_TIMEOUT
        while datetime.now() < payment_deadline:
            if curr_ticket.status == ParkingTicketStatus.PAID:
                # vehicle exits
                return
            time.sleep(PAYMENT_POLLING_INTERVAL)

    def is_full(self, new_vehicle: Vehicle):
        for floor, parking_spots in self.__floors:
            for parking_spot in parking_spots:
                if parking_spot.curr_vehicle == None and parking_spot.fits(new_vehicle):
                    return False
        return True


class ParkingTicketStatus(Enum):
    ACTIVE, PAID, LOST = 1, 2, 3


class ParkingTicket:
    def __init__(self, time_issued: datetime = None):
        if time_issued:
            self.__time_issued = time_issued
        else:
            self.__time_issued = datetime.now()
        self.__status = ParkingTicketStatus.ACTIVE

    def calculate_cost(self, time_paid: datetime = None):
        if not time_paid:
            time_paid = datetime.now()

        duration = time_paid - self.__time_issued
        return duration.total_seconds() / 3600

    @property
    def status(self):
        return self.__status
