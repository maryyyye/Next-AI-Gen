import csv
import sqlite3
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DATABASE = ROOT / "kit-td1" / "data" / "boutique.sqlite"
OUTPUT = ROOT / "reference-td1.csv"

CASES = [
    ("C01", "2026-03-01 00:00:00", "2026-06-01 00:00:00", None, False, None),
    ("C02", None, None, "2026-09-25", False, None),
    ("C03", "2026-01-01 00:00:00", "2026-07-01 00:00:00", None, False, ("a", "b", "c")),
    ("C04", "2026-01-01 00:00:00", "2026-10-01 00:00:00", None, False, None),
    ("C05", "2026-06-01 00:00:00", "2026-06-02 00:00:00", None, False, None),
    ("C06", "2025-01-01 00:00:00", "2026-01-01 00:00:00", None, False, None),
    ("C07", "2026-05-31 00:00:00", "2026-06-01 00:00:00", None, False, None),
    ("C08", None, None, "2026-09-24", False, None),
    ("C09", None, None, "2026-09-26", False, None),
    ("C10", None, None, None, True, None),
    ("C11", None, None, "2026-12-01", False, None),
    ("C12", None, None, None, False, ("a", "b", "c")),
    ("C13", "2026-04-01 00:00:00", "2026-05-01 00:00:00", None, False, ("a", "c")),
    ("C14", "2026-10-01 00:00:00", "2026-12-01 00:00:00", None, False, ("a", "b", "c")),
    ("C15", "2026-03-01 00:00:00", "2026-06-01 00:00:00", "2026-09-25", False, None),
    ("C16", None, None, "2026-09-25", False, ("a", "b", "c")),
    (
        "C17",
        "2026-01-01 00:00:00",
        "2026-07-01 00:00:00",
        "2026-09-25",
        False,
        ("a", "b", "c"),
    ),
    ("C18", "2026-05-01 00:00:00", "2026-06-01 00:00:00", None, True, None),
    ("C19", "2026-09-01 00:00:00", "2026-10-01 00:00:00", "2026-09-25", False, ("d",)),
    ("C20", "2026-06-01 00:00:00", "2026-09-01 00:00:00", None, False, None),
]


def build_query(start, end, reference_date, age_at_order, products):
    conditions = []
    if start:
        conditions.extend((f"o.date >= '{start}'", f"o.date < '{end}'"))
    if reference_date or age_at_order:
        day = "o.date" if age_at_order else f"'{reference_date}'"
        conditions.append(
            "CAST(strftime('%Y', {day}) AS INTEGER) "
            "- CAST(substr(c.birth_date, 1, 4) AS INTEGER) "
            "- (strftime('%m-%d', {day}) < substr(c.birth_date, 6, 5)) = 25".format(
                day=day
            )
        )
    if products:
        quoted = ", ".join(f"'{product}'" for product in products)
        conditions.append(f"o.product_id IN ({quoted})")

    query = (
        "SELECT COALESCE(SUM(o.quantity_product * p.price), 0) AS revenue_cents\n"
        "FROM orders AS o\n"
        "JOIN product AS p ON p.product_id = o.product_id\n"
        "JOIN customers AS c ON c.customer_id = o.customer_id"
    )
    if conditions:
        query += "\nWHERE " + "\n  AND ".join(conditions)
    return query + ";"


def completed_age(day_text, birth_text):
    day = date.fromisoformat(day_text[:10])
    birth = date.fromisoformat(birth_text)
    return day.year - birth.year - ((day.month, day.day) < (birth.month, birth.day))


def main():
    connection = sqlite3.connect(DATABASE.resolve().as_uri() + "?mode=ro", uri=True)
    try:
        order_lines = connection.execute(
            "SELECT o.date, c.birth_date, o.product_id, o.quantity_product, p.price "
            "FROM orders AS o "
            "JOIN customers AS c ON c.customer_id = o.customer_id "
            "JOIN product AS p ON p.product_id = o.product_id"
        ).fetchall()

        rows = []
        for case_id, start, end, reference_date, age_at_order, products in CASES:
            query = build_query(start, end, reference_date, age_at_order, products)
            cursor = connection.execute(query)
            result = cursor.fetchone()
            if (
                len(cursor.description) != 1
                or cursor.description[0][0] != "revenue_cents"
            ):
                raise ValueError(
                    f"{case_id}: query must return one revenue_cents column"
                )

            python_total = 0
            for order_date, birth_date, product_id, quantity, price in order_lines:
                if start and not start <= order_date < end:
                    continue
                if reference_date or age_at_order:
                    age_day = order_date if age_at_order else reference_date
                    if completed_age(age_day, birth_date) != 25:
                        continue
                if products and product_id not in products:
                    continue
                python_total += quantity * price

            if result[0] != python_total:
                raise ValueError(
                    f"{case_id}: SQL={result[0]}, "
                    f"independent Python check={python_total}"
                )
            rows.append((case_id, query, result[0]))
            print(f"{case_id}: {result[0]} cents; SQL/Python match")
    finally:
        connection.close()

    with OUTPUT.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(("case_id", "sql", "revenue_cents"))
        writer.writerows(rows)
    print(f"Wrote {len(rows)} verified references to {OUTPUT.name}.")


if __name__ == "__main__":
    main()
