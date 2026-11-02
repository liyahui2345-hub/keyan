"""Synthetic scalar WLS baseline; not a paper-specific observer."""
import argparse
import json
import math
import platform
from pathlib import Path


def estimate(h, z, variances):
    if not h or not (len(h) == len(z) == len(variances)):
        raise ValueError("Nonempty, equal-length inputs required")
    if not all(math.isfinite(v) for values in (h, z, variances) for v in values):
        raise ValueError("Finite inputs required")
    if any(v <= 0 for v in variances):
        raise ValueError("Variances must be positive")
    denominator = sum(a * a / v for a, v in zip(h, variances))
    if denominator <= 0:
        raise ValueError("State is unobservable")
    return sum(a * b / v for a, b, v in zip(h, z, variances)) / denominator


def run():
    # z = h*x + e; all quantities are dimensionless synthetic values.
    h, z, variances = [1.0, 2.0], [1.02, 1.98], [0.01, 0.04]
    x = estimate(h, z, variances)
    return {"model": "scalar linear WLS", "truth": 1.0, "estimate": x,
            "absolute_error": abs(x - 1.0), "h": h, "z": z,
            "variances": variances, "randomness": "none",
            "python": platform.python_version()}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="results/minimal.json")
    args = parser.parse_args()
    result = run()
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
