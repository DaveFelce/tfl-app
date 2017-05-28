from people.user import User
from travel.card import Card
from travel.journey import Journey
from transport.vehicle import Bus, Tube

def main():
    user = User('Mike')
    card = Card(-1)
    zones_travelled = Journey.calculate_num_zones('A', 'E')
    bus = Bus()
    fare = bus.fare()
    tube = Tube()
    fare += tube.fare(zones_travelled)
    can_pay = card.can_pay(fare)

    print("Fare is {}".format(fare))
    print("{} can pay? {}".format(user.name, can_pay))

if __name__ == '__main__':
    main()
