from lantern import *

bed_lantern = Lantern(power_in_watts=5, producer_name="BOSH")
medical_lantern = Lantern(power_in_watts=100, luminosity_in_candles=5000, producer_name="Terra", producer_country="France", diodes_count=1000, has_warranty=True)
candle = Lantern(producer_name="Church", producer_country="Moldova", kind_of_lamp="fire", power_in_watts=10, luminosity_in_candles=1, diodes_count=0, has_warranty=True)
new_lamp = Lantern()


print(bed_lantern, candle, medical_lantern, new_lamp)
Lantern.calculate_the_cash()
print("\n")
