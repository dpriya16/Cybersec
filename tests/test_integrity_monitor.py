import hashlib

from cybersec_toolkit.integrity_monitor import calculate_file_hash, verify_file_hash


def test_calculate_file_hash_sha256(tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("hello-security", encoding="utf-8")

    result = calculate_file_hash(str(file_path), "sha256")
    expected = hashlib.sha256(b"hello-security").hexdigest()

    assert result.algorithm == "sha256"
    assert result.digest == expected


def test_verify_file_hash_success(tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("cyber", encoding="utf-8")
    expected = hashlib.sha1(b"cyber").hexdigest()

    assert verify_file_hash(str(file_path), expected, "sha1") is True


def test_verify_file_hash_fail(tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("cyber", encoding="utf-8")

    assert verify_file_hash(str(file_path), "0" * 40, "sha1") is False
