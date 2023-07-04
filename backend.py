from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Cars(Base):
    __tablename__ = "Cars"
    car_id = Column("Car-Id", Integer, primary_key=True)
    car_name = Column("Car-Name", String)
    car_type = Column("Car-Type", String)
    car_color = Column("Car-Color", CHAR)
    car_price = Column("Car-Price", Integer)

    def __init__(self, car_id, car_name, car_type, car_color, car_price):
        self.car_id = car_id
        self.car_name = car_name
        self.car_type = car_type
        self.car_color = car_color
        self.car_price = car_price

    def __repr__(self):
        return f"(car_id={self.car_id}, car_name='{self.car_name}', car_type='{self.car_type}', car_color='{self.car_color}', car_price={self.car_price})"


engine = create_engine("sqlite:///Carsdb.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

car1 = Cars(1, 'Aurora', 'Sedan', 'r', 25000)
car2 = Cars(2, 'Phoenix', 'SUV', 'b', 35000)
car3 = Cars(3, 'Titan', 'Pickup Truck', 'p', 40000)
car4 = Cars(4, 'Eclipse', 'Coupe', 'w', 30000)
car5 = Cars(5, 'Viper', 'Sports Car', 'o', 50000)

session.add_all([car1, car2, car3, car4, car5])
session.commit()



