"""
Group Challenge: The Concert Guest List Master Control
Scenario: Your group is managing the main gate security for a massive concert.
You will use Python lists, a tuple, loops, and conditional checks to keep the crowd safe,
clean up typos, and handle rowdy fans!
Part 1: Setting up the Master Data
Have your driver type out this starting code:
"""
vip_list = ["Beyonce", "Zendaya", "Pedro Zascal", "Tom Holland"]
event_details = ("May 21st", "Madison Square Garden")

print("Starting VIPs: ", vip_list)
print("Event Info: ", event_details)

#	Task 1: Late Arrivals (Append & Insert).
vip_list.append("Rihanna")
vip_list.insert(1, "Drake")

print("Starting VIPs: ", vip_list)
print("Event Info: ", event_details)

#	Task 2: The Typo & The Removal.
vip_list[3] = "Pedro Pascal"
vip_list.remove("Tom Holland")

print("Starting VIPs: ", vip_list)
print("Event Info: ", event_details)

# Task 3: Finding the Index. Security needs to know exactly where "Zendaya"
# is standing in line. Use .index() to find her position, save it to a variable,
# and print it out.
zendaya_spot = vip_list.index("Zendaya")
print("Zendaya is at position number: ", zendaya_spot)

# Task 4: Finding a Missing Person (The Exception). Security wants to look up "Kanye".
# Because he isn't on the list, using .index() will normally crash your program with an error.
# Use an if/else check: if "Kanye" is in the list, print his index.
# Else, print a custom message saying "Entry not found!".
search_name = "Kanye"
if search_name in vip_list:
    name_spot = vip_list.index(search_name)
    print(search_name + "found at position number " + name_spot)
else:
    print("SECURITY ALERT! " + search_name + " does not exist on this list")

# Task 5: Checking for Duplicates. Someone claims they are "Zendaya" to try and sneak in twice.
# Use .count() to see how many times "Zendaya" appears in your list. If the count is greater than 1,
# print a warning about a duplicate; otherwise, print that the entry is unique.

lookup_name = input("What name you like to look up? ")
if lookup_name in vip_list:
    print(lookup_name + " is already in line!")
else:
    print(lookup_name + " is not in line yet. proceed!")

# Task 6: Tuple Unpacking & The Entrance Loop.
#    Unpack your event_details tuple into two variables: concert_date and venue.
#    Write a for loop to iterate over your final vip_list and print a custom welcome message for each person!

concert_date, venue = event_details
print("concert_date = "+concert_date+" venue = "+venue)

print("---------- Gate Entrance Open ----------")
for guest in vip_list:
    print("Welcome to " + venue + ", "+guest)
