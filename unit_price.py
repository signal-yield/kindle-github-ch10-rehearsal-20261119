import csv
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path


def main():
    computed = 0
    unavailable = 0
    print("id,unit_price_man_yen_per_m2")
    source = Path(__file__).with_name("mansions.csv")
    with source.open(encoding="utf-8", newline="") as csv_file:
        for row in csv.DictReader(csv_file):
            area = row["area_m2"].strip()
            if area:
                unit_price = Decimal(row["price_man_yen"]) / Decimal(area)
                display = str(unit_price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
                computed += 1
            else:
                display = "算出不可（面積空欄）"
                unavailable += 1
            print(f'{row["id"]},{display}')
    print(f"computed={computed} unavailable={unavailable}")


if __name__ == "__main__":
    main()
