def fetch_body(body):
    name = body.get("name", None)
    email = body.get("email", None)
    password = body.get("password", None)
    phone = body.get("phone", None)
    date_of_birth = body.get("date_of_birth", None)
    address = body.get("address", None)
    driving_license_number = body.get("driving_license_number", None)

    return dict(
        name=name,
        email=email,
        password=password,
        phone=phone,
        date_of_birth=date_of_birth,
        address=address,
        driving_license_number=driving_license_number
    )
