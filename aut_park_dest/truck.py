import math
from aut_park_dest.auto import Auto
from aut_park_dest.driver import Driver


class Truck(Auto):
    def __init__(
        self, weight_capacity, trailer,trailer_weight_capacity,
        predicted_km_per_year,
        number,
        fuel_type,
        fixed_cost,
        technical_date,
        driver_category,
        fuel_consumption_per_100_km,
        insurance_date,
    ):
        super().__init__(
            predicted_km_per_year,
            number,
            fuel_type,
            fixed_cost,
            technical_date,
            driver_category,
            fuel_consumption_per_100_km,
            insurance_date,
        )
        self.weight_capacity = weight_capacity
        self.trailer = trailer
        self.trailer_weight_capacity = trailer_weight_capacity

# Paskaičiuoti kiek reisų reikia padaryti ir ar reikia prikabinti priekabą (tarkim reikia pervežti 30t, automobilio pervežamas svoris yra 12 tonų, priekabos pervežamas svoris 5 tonos. Tokiu atveju reikia vieną karta vežti be priekabos, o antra su priekaba. Bet jei reikia pervežti tarkime 36 tonos, priekabos kabinti neverta, nes vistiek reikia daryti tris reisus);

    def count_numb_truck_and_trailer(self,cargo:int):
        trucks = math.ceil((cargo / (self.weight_capacity + self.trailer_weight_capacity)))
        trailer = math.ceil((cargo - self.weight_capacity * trucks) / self.trailer_weight_capacity)
        return trucks, trailer


    def can_driver_drive_truck_with_trailer(self,driver_license):
        if driver_license == "DE":
            return "Gali"
        else:
            return "Negali"