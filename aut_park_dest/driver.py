import datetime
'''Vairuotojas, kuris turi atributus: 
Atostogų laikas 
Turima teisių kategorija (D sukvežimiai be priekabos, E su priekaba) 
Darbo užmokestis vienam kilometrui; 

 
Prie sukvežimių: 
pridėkime metodą, kuris vertintų vairuotoją ir pagal turimą kategoriją įvertintų ar gali vairuoti mašina su priekaba. 
Visiems automobiliams turi būti patikrinimas ar vairuotojas gali dirbti (ne atostogauja) '''

class Driver:
    def __init__(self, driver_license:str, salary_per_km):
        self.salary_per_km = salary_per_km
        self.driver_license = driver_license
        
        