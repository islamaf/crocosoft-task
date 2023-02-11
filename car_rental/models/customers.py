def customers():
    customers_table = '''
        CREATE TABLE IF NOT EXISTS customers (
            id int NOT NULL AUTO_INCREMENT,
            name varchar(50) NOT NULL,
            email varchar(50) NOT NULL,
            password varchar(255) NOT NULL,
            phone varchar(25) NOT NULL,
            date_of_birth DATE,
            address varchar(255),
            driving_license_number varchar(50) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            deleted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (id),
            UNIQUE KEY (email, phone)
        )
    '''

    return customers_table
