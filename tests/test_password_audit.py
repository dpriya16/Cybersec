from cybersec_toolkit.password_audit import evaluate_password_strength


def test_password_audit_strong_password():
    report = evaluate_password_strength("StrongerPass!2026")
    assert report.score == 5
    assert report.rating == "very strong"
    assert report.recommendations == []


def test_password_audit_weak_password():
    report = evaluate_password_strength("short")
    assert report.score == 1
    assert report.rating == "weak"
    assert "Use at least 12 characters." in report.recommendations
