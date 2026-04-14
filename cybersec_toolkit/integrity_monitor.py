"""File hash tools for integrity monitoring."""

from dataclasses import dataclass
import hashlib
from pathlib import Path


SUPPORTED_ALGORITHMS = {"sha256", "sha1", "md5"}


@dataclass
class FileHashResult:
    """Stores hash details for a file."""

    file_path: str
    algorithm: str
    digest: str


def calculate_file_hash(file_path: str, algorithm: str = "sha256") -> FileHashResult:
    """Calculate a file hash using a selected algorithm."""
    algo = algorithm.lower()
    if algo not in SUPPORTED_ALGORITHMS:
        allowed = ", ".join(sorted(SUPPORTED_ALGORITHMS))
        raise ValueError(f"Unsupported algorithm '{algorithm}'. Choose one of: {allowed}")

    path = Path(file_path)
    if not path.exists() or not path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")

    hasher = hashlib.new(algo)
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(8192), b""):
            hasher.update(chunk)

    return FileHashResult(file_path=str(path), algorithm=algo, digest=hasher.hexdigest())


def verify_file_hash(file_path: str, expected_hash: str, algorithm: str = "sha256") -> bool:
    """Check whether the file hash matches the expected hash value."""
    result = calculate_file_hash(file_path=file_path, algorithm=algorithm)
    return result.digest.lower() == expected_hash.strip().lower()
