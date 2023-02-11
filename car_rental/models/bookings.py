def bookings():
    bookings_table = '''
        CREATE TABLE IF NOT EXISTS bookings (
            id int NOT NULL AUTO_INCREMENT,
            vehicle_id int NOT NULL,
            customer_id int NOT NULL,
            reserve_date DATE NOT NULL,
            return_date DATE NOT NULL,
            pickup_date DATE NOT NULL,
            number_of_days int NOT NULL,
            created_by varchar(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            deleted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (id),
            FOREIGN KEY (vehicle_id) REFERENCES vehicles(id),
            FOREIGN KEY (customer_id) REFERENCES customers(id)
        )
    '''

    return bookings_table
