import math

import pytest

from curvature_lab import invariant, marginal_price, quote_exact_input


def test_invariant():
    assert invariant(10.0, 40.0) == 400.0


def test_marginal_price():
    assert marginal_price(10.0, 40.0) == 4.0


def test_zero_fee_swap():
    quote = quote_exact_input(20.0, 100.0, 2.0)
    assert quote.amount_out == pytest.approx(100.0 * 2.0 / 22.0)
    assert quote.fee_amount == 0.0


def test_fee_reduces_output():
    no_fee = quote_exact_input(10.0, 40.0, 1.0)
    with_fee = quote_exact_input(10.0, 40.0, 1.0, 0.003)
    assert with_fee.amount_out < no_fee.amount_out
    assert with_fee.fee_amount == pytest.approx(0.003)


def test_output_stays_inside_reserve():
    quote = quote_exact_input(1.0, 5.0, 1_000_000.0)
    assert 0.0 < quote.amount_out < 5.0


def test_price_impact_positive():
    assert quote_exact_input(10.0, 40.0, 1.0).price_impact > 0.0


@pytest.mark.parametrize("x,y", [
    (0.0, 1.0), (-1.0, 2.0), (math.inf, 2.0), (math.nan, 2.0)
])
def test_invalid_reserves_rejected(x, y):
    with pytest.raises(ValueError):
        invariant(x, y)


@pytest.mark.parametrize("fee", [-0.1, 1.0, math.inf, math.nan])
def test_invalid_fee_rejected(fee):
    with pytest.raises(ValueError):
        quote_exact_input(10.0, 40.0, 1.0, fee)
