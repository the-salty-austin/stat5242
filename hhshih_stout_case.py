import pandas as pd


def calculate_price(face_amount,
                    interest_rate,
                    payment_periods_per_year,
                    maturity_years,
                    market_discount_rate):
    """
    Calculates the price of a bond.

    Args:
        face_amount: The face amount of the bond.
        interest_rate: The annual interest rate of the bond.
        payment_periods_per_year: The number of payment periods per year.
        maturity_years: The maturity of the bond in years.
        market_discount_rate: The market discount rate.

    Returns:
        The price of the bond.
    """
    schedule = pd.DataFrame(
        columns=['period',
                'beginning_bal',
                'interest_pmt',
                'principal_pmt',
                'ending_bal',
                'tenor',
                'discount_factor',
                'pv_payment'
                ]
    )

    schedule['period'] = [i for i in range(1, 1+payment_periods_per_year * maturity_years)]
    schedule['beginning_bal'] = face_amount
    schedule['interest_pmt'] = schedule['beginning_bal'] * interest_rate / payment_periods_per_year
    schedule['principal_pmt'] = [0] * (payment_periods_per_year * maturity_years - 1) + [face_amount]
    schedule['ending_bal'] = face_amount
    schedule['tenor'] = schedule['period'] / payment_periods_per_year
    schedule['discount_factor'] = 1 / (1 + market_discount_rate)**schedule['tenor']
    schedule['pv_payment'] = (schedule['interest_pmt'] + schedule['principal_pmt']) * schedule['discount_factor']

    return 100 * schedule['pv_payment'].sum() / face_amount



for y in [2,3,4]:
    for r in range(7, 14):
        val = calculate_price(face_amount=24000,
                interest_rate=0.10,
                payment_periods_per_year=4,
                maturity_years=y,
                market_discount_rate=r/100
            )
        
        print(f"{y}Y Maturity, Mkt {r:2}%: ${val:.4f}")