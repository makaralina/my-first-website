def validate_user(user_data):
    errors = {}
    if not user_data['name']:
        errors['name'] = "Name is required"
    if not user_data['email']:
        errors['email'] = "Email is required"
    if not user_data['password']:
        errors['password'] = "Password is required"
    return errors
