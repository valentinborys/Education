
def test_password_validation():
    password = "11qqQQ##;"
    spec_sym = "!@#$%"
    is_valid = None
    is_upper = None
    is_length = None
    is_num = None
    is_spec = None
    errors = []

    if len(password) >= 8:
        is_length = True
    else:
        errors.append("Password must contain at least 8 characters")

    for x in password:
        if x.isupper():
            is_upper = True
            break

    if not is_upper:
        errors.append("Password must contain at least one uppercase letter")

    for b in password:
        if b.isdigit():
            is_num = True
            break

    if not is_num:
        errors.append("Password must contain at least one digit")

    for i in password:
        if i in spec_sym:
            is_spec = True
            break

    if not is_spec:
        errors.append("Password must contain at least one special character")

    if errors:
        is_valid = False
    else:
        is_valid = True

    print("Password is valid:", is_valid)

    for error in errors:
        print("Validation error:", error)

