class Vehicle:
    def fare(self):
        pass

class Bus(Vehicle):
    def fare(self):
        """ Params:
                num_zones(int): number of zones travelled
            
            Returns:
                price(int): the fare
        """

        return 3

class Tube(Vehicle):
    def fare(self, num_zones):
        """ Params:
                num_zones(int): number of zones travelled
            
            Returns:
                price(int): the fare
        """

        return {
            1: 4,
            2: 5,
            3: 6,
            4: 7,
        } [num_zones]
