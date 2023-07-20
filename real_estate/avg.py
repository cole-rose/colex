import numpy as np

homes_and_sq_ft = [
    (1468, 335000),
    (1920, 351043),
    (2472, 355000),
    (1251, 360000),
    (1384, 385000),
    (2179, 392000),
]


def percentage_below_market_val(
    houses_and_sq_ft, listed_price, listed_sq_ft, name=None
):
    if name:
        print(
            f"Calculations for {name}:",
        )
    price_per_sq_ft = [x[1] / x[0] for x in houses_and_sq_ft]
    avg_price = np.average(price_per_sq_ft)
    median_price_per_sq_ft = np.median(price_per_sq_ft)
    print("Median price per square foot:", median_price_per_sq_ft)
    print(f"Comps average: {avg_price}.")
    listed_price_per_sq_ft = listed_price / listed_sq_ft
    print(f"Listed house price per square foot: {listed_price_per_sq_ft}.")
    percentage_below = ((avg_price - listed_price_per_sq_ft) / avg_price) * 100
    percentage_below_median = (
        (median_price_per_sq_ft - listed_price_per_sq_ft) / median_price_per_sq_ft * 100
    )

    below_or_above = "above"
    if percentage_below > 0:
        below_or_above = "below"

    median_below_or_above = "above"
    if percentage_below_median > 0:
        median_below_or_above = "below"

    print(
        "This house is",
        np.abs(percentage_below),
        "%",
        below_or_above,
        "market value average.",
    )
    print(
        "This house is",
        np.abs(percentage_below_median),
        "%",
        median_below_or_above,
        "median market value.",
    )
    amount_to_be_15_percent = avg_price - (avg_price * 0.15)
    print(
        "The house would need to sell for",
        amount_to_be_15_percent * listed_sq_ft,
        "to be 15 percent below market value.",
    )


percentage_below_market_val(homes_and_sq_ft, 365000, 1350, name=None)


smith_homes_and_sq_ft = [(1344, 334500), (1509, 425000), (2000, 395000)]


print("----------------\n\n\n")
percentage_below_market_val(smith_homes_and_sq_ft, 350000, 1838, "833 Smith St NW")
