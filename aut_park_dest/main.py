from datetime import datetime

from aut_park_dest.car import Car
from aut_park_dest.car import Auto
from aut_park_dest.bus import Bus
from aut_park_dest.truck import Truck
from aut_park_dest.driver import Driver

car = Car(
        predicted_km_per_year=20000,
        number='ANB205',
        fuel_type='Petrol',
        fixed_cost=4000,
        technical_date= datetime(year=2024, month=5, day=15),
        driver_category='B',
        fuel_consumption_per_100_km= 8,
        insurance_date=datetime(year=2024, month=5, day=15),
)

bus = Bus(
        predicted_km_per_year=120000,
        number='DCB555',
        fuel_type='Diesel',
        fixed_cost=8000,
        technical_date= datetime(year=2025, month=1, day=8),
        driver_category='C',
        fuel_consumption_per_100_km= 20,
        insurance_date=datetime(year=2024, month=9, day=3),
)

truck = Truck(
        predicted_km_per_year=85000,
        number='ABC123',
        fuel_type='Diesel',
        fixed_cost=9000,
        technical_date= datetime(year=2024, month=4, day=1),
        driver_category='D',
        fuel_consumption_per_100_km= 25,
        insurance_date=datetime(year=2024, month=5, day=18),
        weight_capacity = 12000, trailer = True, trailer_weight_capacity = 5000,)

driver = Driver(
        salary_per_km = 1.5,
        driver_license = "D"

)


print("car insurance needed next month?", car.check_if_next_month_needs_insurance())
print("car tech needed next month?", car.check_if_next_month_needs_technical())

print("bus insurance need next month?",bus.check_if_next_month_needs_insurance())
print("bus technical needed?",bus.check_if_next_month_needs_technical())

print("need truck insurance next month?",truck.check_if_next_month_needs_insurance())
print("need truck technical check next month?",truck.check_if_next_month_needs_technical())

print("Car travel costs:", car.travel_costs(1000,1.5))
print("Bus travel costs:",bus.travel_costs(1000,1.6))
print("Truck travel costs",truck.travel_costs(1000,1.6))

print("Bus trips needed",bus.trips_needed(121))
print("Bus trips costs:",bus.trips_total_cost(1000,1.6))
print("Trucks and trailers needed to deliver cargo:",truck.count_numb_truck_and_trailer(30000))
print("Can driver drive truck with trailer?:",truck.can_driver_drive_truck_with_trailer(driver_license="D"))
