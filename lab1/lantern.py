class Lantern:
    __count_of_bought_lamps = None

    def __init__(self, kind_of_lamp="digital", power_in_watts=12, diodes_count=100, producer_name="Siemens", producer_country="Germany",
                 has_warranty=False, luminosity_in_candles=100):
        self.__kind_of_lamp = kind_of_lamp
        self.__power_in_watts = power_in_watts
        self.__diodes_count = diodes_count
        self.__producer_name = producer_name
        self.__producer_country = producer_country
        self.__has_warranty = has_warranty
        self.__luminosity_in_candles = luminosity_in_candles

        if Lantern.__count_of_bought_lamps is None:
            Lantern.__count_of_bought_lamps = 1
        else:
            Lantern.__count_of_bought_lamps += 1

    def __del__(self):
        print("The lantern of company {} is no more in operation".format(self.__producer_name))

    def __str__(self):
        return "Lantern made by: {}, {}\nluminosity: {} cd\nwarranty: {}\nADDITIONAL PARAMETERS\nPower: {} W, Number of diodes: {}, Kind of lamp: {}\n\n"\
            .format(self.__producer_name, self.__producer_country, self.__luminosity_in_candles, self.__has_warranty, self.__power_in_watts,
                    self.__diodes_count, self.__kind_of_lamp)

    @staticmethod
    def calculate_the_cash():
        print("There are {} lanterns sold since the start of the program\nTotal received cash is {} EUR".format(Lantern.__count_of_bought_lamps, Lantern.__count_of_bought_lamps*20))

    @staticmethod
    def get_sold_lamps():
        return Lantern.__count_of_bought_lamps
    """
    GETTERS AND SETTERS GO HERE
    """
    @property
    def kind_of_lamp(self):
        return self.__kind_of_lamp

    @property
    def kind_of_lamp(self, val):
        self.__kind_of_lamp = val

    @property
    def power_in_watts(self):
        return self.__kind_of_lamp

    @property
    def power_in_watts(self, val):
        self.__kind_of_lamp = val

    @property
    def diodes_count(self):
        return self.__kind_of_lamp

    @property
    def diodes_count(self, val):
        self.__kind_of_lamp = val

    @property
    def producer_name(self):
        return self.__kind_of_lamp

    @property
    def producer_name(self, val):
        self.__kind_of_lamp = val

    @property
    def producer_country(self):
        return self.__kind_of_lamp

    @property
    def producer_country(self, val):
        self.__kind_of_lamp = val

    @property
    def has_warranty(self):
        return self.__kind_of_lamp

    @property
    def has_warranty(self, val):
        self.__kind_of_lamp = val

    @property
    def luminosity_in_candles(self):
        return self.__kind_of_lamp

    @property
    def luminosity_in_candles(self, val):
        self.__kind_of_lamp = val
