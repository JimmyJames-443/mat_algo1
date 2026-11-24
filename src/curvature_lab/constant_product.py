from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True, slots=True)
class SwapQuote:
    amount_in: float
    fee_amount: float
    effective_amount_in: float
    amount_out: float
    execution_price: float
    price_impact: float


def _positive(name: str, value: float) -> None:
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be a positive finite number")


def invariant(reserve_x: float, reserve_y: float) -> float:
    """Return the constant-product invariant k = x * y."""
    _positive("reserve_x", reserve_x)
    _positive("reserve_y", reserve_y)
    return reserve_x * reserve_y


def marginal_price(reserve_x: float, reserve_y: float) -> float:
    """Return the marginal price in units of Y per unit of X."""
    _positive("reserve_x", reserve_x)
    _positive("reserve_y", reserve_y)
    return reserve_y / reserve_x


def quote_exact_input(
    reserve_in: float,
    reserve_out: float,
    amount_in: float,
    fee_rate: float = 0.0,
) -> SwapQuote:
    """Quote an exact-input constant-product swap.

    The fee-adjusted input determines output. The full input remains in the
    pool, matching the standard v2-style fee accounting model.
    """
    _positive("reserve_in", reserve_in)
    _positive("reserve_out", reserve_out)
    _positive("amount_in", amount_in)

    if not math.isfinite(fee_rate) or not 0 <= fee_rate < 1:
        raise ValueError("fee_rate must be finite and satisfy 0 <= fee_rate < 1")

    effective = amount_in * (1.0 - fee_rate)
    fee = amount_in - effective
    output = reserve_out * effective / (reserve_in + effective)
    if not 0 < output < reserve_out:
        raise ArithmeticError("computed output violates reserve bounds")

    execution_price = output / amount_in
    initial_price = reserve_out / reserve_in
    impact = 1.0 - execution_price / initial_price

    return SwapQuote(
        amount_in=amount_in,
        fee_amount=fee,
        effective_amount_in=effective,
        amount_out=output,
        execution_price=execution_price,
        price_impact=impact,
    )
