# Mathematical Foundations

## 1. State space

A two-asset pool is represented by reserves (x, y) in the positive real plane. The constant-product reference invariant is:

$$k=xy$$

A trade moves the reserve state along a level set of this function, subject to fees and the protocol's accounting rules.

## 2. Marginal price

Differentiating xy = k gives:

$$y\,dx+x\,dy=0$$

Therefore:

$$-\frac{dy}{dx}=\frac{y}{x}$$

The marginal price of X in units of Y is y/x. This is an infinitesimal price, not the average execution price of a finite trade.

## 3. Exact-input swap without fees

For input Δx > 0, post-trade reserves satisfy:

$$(x+\Delta x)(y-\Delta y)=xy$$

Solving:

$$\Delta y=\frac{y\Delta x}{x+\Delta x}$$

For positive finite inputs and positive reserves, output is strictly between zero and the output reserve.

## 4. Exact-input swap with an input fee

Let f in [0,1) be the fee fraction and γ = 1 - f. The pricing-effective input is γΔx:

$$\Delta y=\frac{y\gamma\Delta x}{x+\gamma\Delta x}$$

The full input is assumed to remain in the pool, while only the fee-adjusted input determines output. Fee routing changes post-trade invariant behaviour and must be stated explicitly.

## 5. Execution price and price impact

$$p_{exec}=\frac{\Delta y}{\Delta x}$$

Given initial marginal price p0 = y/x, this implementation defines quote-level price impact as:

$$I=1-\frac{p_{exec}}{p_0}$$

This includes the fee. Experiments should separate fee cost from curve-induced price impact where possible.

## 6. Curvature

The constant-product level curve is:

$$y(x)=\frac{k}{x}$$

Its derivatives are:

$$y'(x)=-\frac{k}{x^2}, \qquad y''(x)=\frac{2k}{x^3}$$

Curvature influences how marginal price changes as the reserve state moves. A claim that a curve is better must specify the objective and constraints: lower trader slippage may transfer risk to liquidity providers or increase adverse-selection costs.

## 7. Numerical caveats

The Python reference uses binary floating-point for exploratory analysis. It is not appropriate for consensus-critical token accounting. A Solidity implementation must use integer fixed-point arithmetic, define rounding direction, prevent overflow, and test boundary conditions.
