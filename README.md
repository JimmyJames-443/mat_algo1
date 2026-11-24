# Curvature Lab

A reproducible mathematical research environment for the design and evaluation of automated market makers (AMMs).

> Research status: foundational implementation. This repository does not claim a novel invariant or production readiness.

## Research question

Can an alternative AMM invariant improve the trade-off between trader execution cost and liquidity-provider adverse-selection exposure under a clearly specified market and adversary model?

A lower-slippage curve alone is not necessarily better: it may transfer risk to liquidity providers. Every proposed mechanism must be evaluated on both sides of the market.

## Current implementation

The initial baseline is the constant-product market maker:

$$xy=k$$

It includes invariant calculation, marginal price calculation, exact-input swap quotes, fee-aware output calculation, execution-price and price-impact metrics, input validation, and unit tests.

This is a mathematical reference implementation, not a live exchange. It does not connect to wallets, external price feeds, or deployed token contracts.

## Repository structure

    docs/
      MATHEMATICAL_FOUNDATIONS.md
      RESEARCH_PROTOCOL.md
      ROADMAP.md
    src/curvature_lab/
      __init__.py
      constant_product.py
    tests/
      test_constant_product.py
    .gitignore
    LICENSE
    Makefile
    pyproject.toml

## Quick start

Requires Python 3.11 or newer.

    python -m venv .venv

Windows PowerShell:

    .venv\Scripts\Activate.ps1
    python -m pip install -e ".[dev]"
    pytest

Linux/macOS:

    source .venv/bin/activate
    python -m pip install -e ".[dev]"
    pytest

Example:

    from curvature_lab import marginal_price, quote_exact_input

    print(marginal_price(10.0, 40.0))
    quote = quote_exact_input(10.0, 40.0, 1.0, fee_rate=0.003)
    print(quote.amount_out)
    print(quote.execution_price)

## Mathematical conventions

- Prices are expressed as units of token Y per token X.
- A fee rate of 0.003 means 0.3%.
- Python binary floating-point is used for exploratory analysis only. It is not suitable for consensus-critical token accounting.
- An eventual Solidity implementation must define fixed-point precision, rounding, overflow behaviour, and differential tests.

Read docs/MATHEMATICAL_FOUNDATIONS.md before extending the model.

## Research standards

Every candidate invariant must have a formal definition and valid domain; derivations for marginal price and swap output; reserve and solvency analysis; boundary and numerical-stability analysis; an explicit market and adversary model; and reproducible comparisons against established baselines.

See docs/RESEARCH_PROTOCOL.md.

## Scope and disclaimer

This is an experimental research codebase. It is not audited, is not production-ready, and must not be used to manage real funds. The initial constant-product model is an established baseline, not a novelty claim.

## License

MIT.
