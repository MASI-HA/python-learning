tickets = [
    {"passenger": "Ali", "from": "Tehran", "to": "Mashhad", "price": 15000},
    {"passenger": "reza", "from": "tabriz", "to": "tehran", "price": 275000},
    {"passenger": "masiha", "from": "esfehan", "to": "mazandaran", "price": 3845000},
]
total_revenue = 0

while True:
    for ticket in tickets:
        print(
            f"passenger :{ticket['passenger']}, {ticket['from']}, {ticket['to']}, {ticket['price']}"
        )

    passenger = input("enter your name :")
    from_city = input("enter your city from : ")
    to_city = input("enter your city to : ")
    price = int(input("enter your price :"))

    new_ticket = {
        "passenger": passenger,
        "from": from_city,
        "to": to_city,
        "price": price,
    }
    tickets.append(new_ticket)

    again = input("Do you want to sell another ticket? (yes/no): ")
    if again != "yes":
        break

print(f"total_revenue :{total_revenue}")
print(f"Total Tickets: {len(tickets)}")
