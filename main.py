from js import document

restaurant_name = "Yumamochi"
location = "Maginhawa, Quezon City"
opening_hours = "10:00 AM – 9:00 PM"

document.getElementById("restaurant-name").innerText = restaurant_name
document.getElementById("welcome-text").innerText = f"🍡 Welcome to {restaurant_name}!"
document.getElementById("location").innerText = f"📍 Location: {location}"
document.getElementById("hours").innerText = f"⏰ Opening Hours: {opening_hours}"

mochi_items = [
    ("Matchi", "Matcha", "₱50"),
    ("Sakura Delight", "Cherry Blossom", "₱60"),
    ("Choco Mochi", "Chocolate", "₱55")
]

tbody = document.getElementById("mochi-body")

rows = ""
for name, flavor, price in mochi_items:
    rows += f"<tr><td>{name}</td><td>{flavor}</td><td>{price}</td></tr>"

tbody.innerHTML = rows


