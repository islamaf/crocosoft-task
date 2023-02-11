from ..enums.vehicle_types import VehicleTypes


def vehicles():
    vehicles_table = f'''
        CREATE TABLE IF NOT EXISTS vehicles (
            id int NOT NULL AUTO_INCREMENT,
            model varchar(50) NOT NULL,
            year int NOT NULL,
            type ENUM('{VehicleTypes.SMALL.value}', '{VehicleTypes.FAMILY.value}', '{VehicleTypes.VAN.value}') NOT NULL,
            daily_price int NOT NULL,
            plate varchar(15) NOT NULL,
            mileage DECIMAL(6,2) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            deleted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (id),
            UNIQUE KEY (plate)
        )
    '''

    return vehicles_table
