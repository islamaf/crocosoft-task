def invoices():
    invoices_table = '''
        CREATE TABLE IF NOT EXISTS invoices (
            id int NOT NULL AUTO_INCREMENT,
            vehicle_id int NOT NULL,
            customer_id int NOT NULL,
            days int NOT NULL,
            price int NOT NULL,
            date_recieved TIMESTAMP NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            deleted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (id),
            FOREIGN KEY (vehicle_id) REFERENCES vehicles(id),
            FOREIGN KEY (customer_id) REFERENCES customers(id),
            FOREIGN KEY (days) REFERENCES bookings(number_of_days)
        )
    '''

    return invoices_table