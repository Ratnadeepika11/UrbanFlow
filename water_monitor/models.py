from django.db import models

class WaterSector(models.Model):
    sector_name = models.CharField(max_length=100)
    inflow_liters = models.FloatField(default=0.0)      # Water sent to sector
    consumption_liters = models.FloatField(default=0.0) # Water billed/used
    threshold = models.FloatField(default=5000.0)
    
    # New Sensors
    pressure_bar = models.FloatField(default=3.5)       # Standard 3-5 bar
    ph_level = models.FloatField(default=7.0)           # Neutral 7.0
    
    def __str__(self):
        return self.sector_name