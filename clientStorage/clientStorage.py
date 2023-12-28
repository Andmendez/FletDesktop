
# strings
page.client_storage.set("key", "value")

# numbers, booleans
page.client_storage.set("number.setting", 12345)
page.client_storage.set("bool_setting", True)

# lists
page.client_storage.set("favorite_colors", ["read", "green", "blue"])


# Reading data:
# The value is automatically converted back to the original type
value = page.client_storage.get("key")

colors = page.client_storage.get("favorite_colors")
# colors = ["read", "green", "blue"]

# Check if a key exists:
page.client_storage.contains_key("key")

# Get all keys:
page.client_storage.get_keys("key-prefix.")

# Remove a value:
page.client_storage.remove("key")

# Clear the storage:
page.client_storage.clear()