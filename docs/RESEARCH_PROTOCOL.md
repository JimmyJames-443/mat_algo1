# Research Protocol

## Research question

Can an alternative two-asset AMM invariant improve the trade-off between trader execution cost and liquidity-provider adverse-selection exposure under a specified market model, without violating reserve, solvency, or manipulation-resistance constraints?

## Null hypothesis

Under the selected evaluation model, the proposed invariant does not improve the predeclared objective relative to established baselines once fees, liquidity-provider outcomes, and adversarial behaviour are included.

## Required baselines

- Constant product: xy = k.
- Constant sum: x + y = k, including boundary and depletion risks.
- A concentrated-liquidity design or faithful active-range model where relevant.

Do not compare against an inaccurately simplified implementation.

## Evaluation dimensions

1. Trader execution cost across trade sizes and pool imbalances.
2. Liquidity-provider mark-to-market outcomes under external price movement.
3. Adverse-selection costs under arbitrage or informed trading.
4. Reserve positivity and solvency conditions.
5. Sensitivity to fees and invariant parameters.
6. Numerical stability and implementation precision.
7. Manipulation resistance under explicit adversarial strategies.

## Experimental discipline

- Fix initial pool value and external reference price when comparing curves.
- State whether fees are retained or routed elsewhere.
- Use identical trade and price paths across candidate mechanisms.
- Separate deterministic curve properties from stochastic assumptions.
- Report distributions and worst-case outcomes, not only averages.
- Publish random seeds and configurations for stochastic experiments.
- Include counterexamples and failed hypotheses.

## Novelty standard

A new parameterization of a known curve is not automatically a contribution. A contribution must identify a limitation in existing mechanisms, derive a meaningful property or trade-off, and demonstrate the result analytically or experimentally.

## Safety

Use test assets and isolated environments. No real funds, private keys, or mainnet deployment are needed for this research.
