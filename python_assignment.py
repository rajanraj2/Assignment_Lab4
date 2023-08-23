class Flight:
    def __init__(self, flight_id, origin, destination, price):
        self.flight_id = flight_id
        self.origin = origin
        self.destination = destination
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_by_city(self, city):
        result = []
        for flight in self.flights:
            if flight.origin == city or flight.destination == city:
                result.append(flight)
        return result

    def search_by_origin(self, origin):
        result = []
        for flight in self.flights:
            if flight.origin == origin:
                result.append(flight)
        return result

    def search_between_cities(self, origin, destination):
        result = []
        for flight in self.flights:
            if flight.origin == origin and flight.destination == destination:
                result.append(flight)
        return result

def main():
    flight_table = FlightTable()

    flight_data = [
        ("AI161E90", "BLR", "BOM", 5600),
        ("BR161F91", "BOM", "BBI", 6750),
        ("AI161F99", "BBI", "BLR", 8210),
        ("VS171E20", "JLR", "BBI", 5500),
        ("AS171G30", "HYD", "JLR", 4400),
        ("AI131F49", "HYD", "BOM", 3499)
    ]

    for data in flight_data:
        flight = Flight(data[0], data[1], data[2], data[3])
        flight_table.add_flight(flight)

    while True:
        print("\nSearch options:")
        print("1. Flights for a particular City")
        print("2. Flights From a city")
        print("3. Flights between two given cities")
        print("4. Exit")

        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            city = input("Enter the city: ")
            results = flight_table.search_by_city(city)
        elif choice == 2:
            origin = input("Enter the origin city: ")
            results = flight_table.search_by_origin(origin)
        elif choice == 3:
            origin = input("Enter the origin city: ")
            destination = input("Enter the destination city: ")
            results = flight_table.search_between_cities(origin, destination)
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice.")
            continue

        if results:
            print("Flight ID\tFrom\tTo\tPrice")
            for flight in results:
                print(f"{flight.flight_id}\t{flight.origin}\t{flight.destination}\t{flight.price}")
        else:
            print("No flights found.")

if __name__ == "__main__":
    main()
