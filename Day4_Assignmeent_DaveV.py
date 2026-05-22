# Comic Book Inventory Manager
# What it does:
# # Create an initial inventory (list of dictionaries)
# # Add new comics dynamically
# # Update comic info (price, condition, quantity)
# # Remove comics
# # Return totals (count, value, publisher totals)

#initial inventory (list of dictionaries)
comic_inventory = [
    {"title": "Amazing Spider-Man #300", "publisher": "Marvel", "condition": "VF", "qty": 1, "price": 450},
    {"title": "Batman #420", "publisher": "DC", "condition": "NM", "qty": 1, "price": 2500},
    {"title": "Punisher #1", "publisher": "Marvel", "condition": "NM", "qty": 1, "price": 120},
    {"title": "Justice League #1234", "publisher": "DC", "condition": "F", "qty": 1, "price": 25},
    {"title": "AvP #1", "publisher": "Dark Horse", "condition": "P", "qty": 1, "price": 1.99},
]
print(comic_inventory)

#Add a new comic
def add_comic(title, publisher, condition, qty, price):
    new_comic = {
        "title": title,
        "publisher": publisher,
        "condition": condition,
        "qty": qty,
        "price": price
    }
    comic_inventory.append(new_comic)
    print(f"Added comic: {title}")

add_comic("Avengers Assemble #43", "Marvel", "M", 1, 6.99)
print(comic_inventory)

# update existing comic
def update_comic(title, field, new_value):
    for comic in comic_inventory:
        if comic["title"] == title:
            comic[field] = new_value
            print(f"Updated comic: {title} set {field} to {new_value}")
            return
        print("comic not found")

def update_comic(title, field, new_value):
    for comic in comic_inventory:
        if comic["title"] == title:
            comic[field] = new_value
            print(f"Updated comic: {title} set {field} to {new_value}")
            return
    print("Comic not found")


update_comic("Punisher #1", "condition", "M")
update_comic("Punisher #1", "price", 2500)
print(comic_inventory)

#Remove a comic book
def remove_comic(title):
    for comic in comic_inventory:
        if comic["title"] == title:
            comic_inventory.remove(comic)
            print(f"Removed comic: {title}")
            return
    print("comic not found")

#Totals
def total_comics():
    total = 0
    for comic in comic_inventory:
        total += comic["qty"]
    return total

def total_value():
    value = 0
    for comic in comic_inventory:
        value += comic["qty"] * comic["price"]
    return value

def count_by_publisher(publisher):
    count = 0
    for comic in comic_inventory:
        if comic["publisher"] == publisher:
            count += comic["qty"]
    return count

print("Total Comics:", total_comics())
print("Total Value: $", total_value())
print("Marvel Count:", count_by_publisher("Marvel"))
print("DC Count:", count_by_publisher("DC"))
print("Dark Horse Count:", count_by_publisher("Dark Horse"))
