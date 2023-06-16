def wrong_user_display(user_meta_data={"name": "John", "age": 30}):
    name = user_meta_data.pop("name")
    age = user_meta_data.pop("age")

    return f"{name} is {age} old"

def user_display(user_meta_data=None):
    user_meta_data = user_meta_data or {"name": "John", "age": 30}
    name = user_meta_data.pop("name")
    age = user_meta_data.pop("age")

    return f"{name} is {age} old"

print(wrong_user_display())
# Error will happen down
print(user_display())
print(user_display())
print(user_display())