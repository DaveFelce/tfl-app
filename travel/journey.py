class Journey:

    @staticmethod
    def calculate_num_zones(first, second):
        zones = {
            'A': 1,
            'B': 2,
            'C': 3,
            'D': 4,
            'E': 5,
        }

        zones_travelled = zones[second] - zones[first]
        return abs(zones_travelled)


