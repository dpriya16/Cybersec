"""Password strength checks for beginner cybersecurity practice."""

from dataclasses import dataclass
import re


@dataclass
class PasswordStrengthReport:
    """Summary result for a password strength evaluation."""

    score: int
    max_score: int
    rating: str
    checks: dict[str, bool]
    recommendations: list[str]


def evaluate_password_strength(password: str) -> PasswordStrengthReport:
    """
    Evaluate a password against basic security checks.

    Scoring (max 5):
      - Length at least 12 chars
      - Contains lowercase letters
      - Contains uppercase letters
      - Contains digits
      - Contains symbols
    """
    checks = {
        "length_12_plus": len(password) >= 12,
        "has_lowercase": bool(re.search(r"[a-z]", password)),
        "has_uppercase": bool(re.search(r"[A-Z]", password)),
        "has_digit": bool(re.search(r"\d", password)),
        "has_symbol": bool(re.search(r"[^A-Za-z0-9]", password)),
    }
    score = sum(checks.values())

    if score <= 2:
        rating = "weak"
    elif score == 3:
        rating = "medium"
    elif score == 4:
        rating = "strong"
    else:
        rating = "very strong"

    recommendations: list[str] = []
    if not checks["length_12_plus"]:
        recommendations.append("Use at least 12 characters.")
    if not checks["has_lowercase"]:
        recommendations.append("Add at least one lowercase letter.")
    if not checks["has_uppercase"]:
        recommendations.append("Add at least one uppercase letter.")
    if not checks["has_digit"]:
        recommendations.append("Add at least one number.")
    if not checks["has_symbol"]:
        recommendations.append("Add at least one symbol, e.g. !@#$%.")

    return PasswordStrengthReport(
        score=score,
        max_score=len(checks),
        rating=rating,
        checks=checks,
        recommendations=recommendations,
    )
