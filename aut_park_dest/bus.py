from aut_park_dest.auto import Auto


class Bus(Auto):
    def __init__(
        self,
        predicted_km_per_year,
        number,
        fuel_type,
        fixed_cost,
        technical_date,
        driver_category,
        fuel_consumption_per_100_km,
        insurance_date,
        seats: int = 30,
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
        self.seats = seats

    # Metodas, kiek reikia autobusų norint pervežti N keleivių;
    def trips_needed(self, passengers: int):
        return passengers // self.seats + (1 if passengers % self.seats != 0 else 0)

    # Paskaičiuotų kokia būtų bendra samata pervežus N keleivių ir nuvažiavus X kilometrų.
    def trips_total_cost(self, distance, fuel_price=1.5):
        keliones_kaina = ((self.fixed_cost / self.predicted_km_per_year) * distance) + (distance / 100 * self.fuel_consumption_per_100_km * fuel_price)
        rez = keliones_kaina * self.trips_needed(121)
        return rez


        # return (((self.fixed_cost / self.predicted_km_per_year) * distance) + (distance / 100 * self.fuel_consumption_per_100_km * fuel_price)) * self.trips_needed(5)

    #         (self.trips_needed(121) * self.fuel_consumption_per_100_km * fuel_price / 100
    #             + self.fixed_cost / self.predicted_km_per_year * distance)
    #
    #
    #
    #
    # ((self.fixed_cost / self.predicted_km_per_year) * distance) + (distance / 100 * self.fuel_consumption_per_100_km * fuel_price)

# return (
#     ((distance * self.trips_needed(passengers)) * fuel_price) / 100
# ) * self.fuel_consumption_per_100_km
