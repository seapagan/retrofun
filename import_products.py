"""Simple script to import products from a CSV file.""" ""
import csv

from db import Model, Session, engine
from models import Country, Manufacturer, Product


def main():
    """Main entry point for the script."""
    Model.metadata.drop_all(engine)  # warning: this deletes all data!
    Model.metadata.create_all(engine)

    with Session() as session:
        with session.begin():
            with open("products.csv") as f:
                reader = csv.DictReader(f)
                all_manufacturers = {}
                all_countries = {}

                for row in reader:
                    row["year"] = int(row["year"])

                    manufacturer = row.pop("manufacturer")
                    countries = row.pop("country").split("/")

                    p = Product(**row)

                    if manufacturer not in all_manufacturers:
                        m = Manufacturer(name=manufacturer)
                        session.add(m)
                        all_manufacturers[manufacturer] = m
                    all_manufacturers[manufacturer].products.append(p)

                    for country in countries:
                        if country not in all_countries:
                            c = Country(name=country)
                            session.add(c)
                            all_countries[country] = c
                        all_countries[country].products.append(p)


if __name__ == "__main__":
    main()
