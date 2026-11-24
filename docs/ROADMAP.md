# Roadmap

## Milestone 0 — Mathematical baseline
- [x] Define reserve-state notation and units.
- [x] Derive constant-product marginal price.
- [x] Derive exact-input swap equation.
- [x] Implement fee-aware reference quote.
- [x] Add unit tests for core properties.

## Milestone 1 — Baseline analysis
- [ ] Add constant-sum and weighted constant-mean reference models.
- [ ] Derive and test marginal prices for each model.
- [ ] Add trade-size and reserve-imbalance sweeps.
- [ ] Separate fee cost from curve-induced price impact.
- [ ] Produce reproducible plots and benchmark tables.

## Milestone 2 — Liquidity-provider economics
- [ ] Define an external price process.
- [ ] Model arbitrage back to the external price.
- [ ] Measure impermanent loss and adverse-selection costs.
- [ ] Compare outcomes at equal initial liquidity and market conditions.

## Milestone 3 — Candidate mechanism
- [ ] State a precise limitation in existing designs.
- [ ] Formulate candidate invariant and parameter domain.
- [ ] Derive marginal price and swap output.
- [ ] Establish reserve and solvency properties.
- [ ] Search for counterexamples before implementation.

## Milestone 4 — EVM implementation
- [ ] Specify fixed-point representation and rounding.
- [ ] Implement a minimal experimental Solidity pool.
- [ ] Differential-test Solidity outputs against the mathematical model.
- [ ] Fuzz boundary cases and invariant properties.
- [ ] Measure gas costs.

## Milestone 5 — Research release
- [ ] Document assumptions and limitations.
- [ ] Publish reproducible experiments.
- [ ] Compare against established AMMs.
- [ ] Write a technical report including negative results.
