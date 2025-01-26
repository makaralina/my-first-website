def validate_user(user_data):
    errors = {}
    if not user_data['email']:
        errors['email'] = "Email is required"
    if not user_data['password']:
        errors['password'] = "Password is required"
    if user_data['password'] != user_data['passwordConfirmation']:
        errors['passwordConfirmation'] = "⚠️Passwords do not match"
    return errors
