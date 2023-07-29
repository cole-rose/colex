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
    print("----------------\n\n\n")

    if name:
        print(
            f"Calculations for {name}:",
        )

    price_per_sq_ft = [x[1] / x[0] for x in houses_and_sq_ft]
    avg_price = np.average(price_per_sq_ft)
    median_price_per_sq_ft = round(np.median(price_per_sq_ft), 2)
    print(f"Median price per square foot: ${median_price_per_sq_ft}")
    print(f"Comps average: ${round(avg_price, 2)}.")
    listed_price_per_sq_ft = round(listed_price / listed_sq_ft, 2)
    print(f"Listed house price per square foot: ${listed_price_per_sq_ft}.")
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
        round(np.abs(percentage_below), 2),
        "%",
        below_or_above,
        "market value average.",
    )
    print(
        "This house is",
        round(np.abs(percentage_below_median), 2),
        "%",
        median_below_or_above,
        "median market value.",
    )
    amount_to_be_15_percent = avg_price - (avg_price * 0.15)

    print(
        f"The house would need to sell for ${round(amount_to_be_15_percent * listed_sq_ft, 2)}  to be 15 percent average below market value.",
    )

    amount_to_be_15_percent_below_median = round(
        (median_price_per_sq_ft - (median_price_per_sq_ft * 0.15)) * listed_sq_ft, 2
    )

    print(
        f"The house would need to sell for ${amount_to_be_15_percent_below_median} to be 15 percent average below median market value.",
    )


percentage_below_market_val(homes_and_sq_ft, 365000, 1350, name=None)


smith_homes_and_sq_ft = [
    (1344, 334500),
    (2000, 395000),
    (1117, 300000),
    (1260, 302000),
    (1343, 310000),
    (1590, 322000),
    (1200, 322000),
    (1600, 379000),
    (1431, 399000),
]


print("----------------\n\n\n")
percentage_below_market_val(smith_homes_and_sq_ft, 350000, 1838, "833 Smith St NW")


geraldine_homes_and_sq_ft = [
    (2870, 410000),
    (1727, 410500),
    (22000, 418000),
    (1200, 425000),
    (2141, 430000),
    (2272, 435000),
    (1809, 440000),
]

percentage_below_market_val(
    geraldine_homes_and_sq_ft, 395000, 2300, "85 Geraldine Dr SE, Smyrna, GA"
)


hilltop = [
    (1215, 425000),
    (1806, 425000),
    (1150, 435000),
    (1382, 440000),
    (1658, 450000),
    (1380, 476300),
]


percentage_below_market_val(hilltop, 449000, 1500, "2997 Hilltop Dr, Doraville")
