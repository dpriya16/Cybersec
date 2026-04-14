"""Command line interface for the beginner cybersecurity toolkit."""

import argparse
import json
import sys

from cybersec_toolkit import (
    calculate_file_hash,
    evaluate_password_strength,
    scan_local_ports,
    verify_file_hash,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python main.py",
        description="Basic cybersecurity working project toolkit.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    pwd_parser = subparsers.add_parser(
        "password-audit", help="Evaluate password strength and get recommendations."
    )
    pwd_parser.add_argument("password", help="Password string to evaluate.")

    hash_parser = subparsers.add_parser(
        "hash-file", help="Calculate the hash of a file for integrity monitoring."
    )
    hash_parser.add_argument("file_path", help="Path to file to hash.")
    hash_parser.add_argument(
        "--algorithm",
        default="sha256",
        choices=["sha256", "sha1", "md5"],
        help="Hash algorithm to use.",
    )

    verify_parser = subparsers.add_parser(
        "verify-hash", help="Verify file hash against expected digest."
    )
    verify_parser.add_argument("file_path", help="Path to file to verify.")
    verify_parser.add_argument("expected_hash", help="Expected digest value.")
    verify_parser.add_argument(
        "--algorithm",
        default="sha256",
        choices=["sha256", "sha1", "md5"],
        help="Hash algorithm to use.",
    )

    scan_parser = subparsers.add_parser(
        "port-scan", help="Scan local host ports to find open TCP services."
    )
    scan_parser.add_argument("host", help="Target host (e.g. 127.0.0.1).")
    scan_parser.add_argument("start_port", type=int, help="Start port.")
    scan_parser.add_argument("end_port", type=int, help="End port.")
    scan_parser.add_argument(
        "--timeout",
        type=float,
        default=0.3,
        help="Per-port timeout in seconds.",
    )

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        if args.command == "password-audit":
            report = evaluate_password_strength(args.password)
            print(
                json.dumps(
                    {
                        "score": report.score,
                        "max_score": report.max_score,
                        "rating": report.rating,
                        "checks": report.checks,
                        "recommendations": report.recommendations,
                    },
                    indent=2,
                )
            )
            return 0

        if args.command == "hash-file":
            result = calculate_file_hash(args.file_path, args.algorithm)
            print(
                json.dumps(
                    {
                        "file_path": result.file_path,
                        "algorithm": result.algorithm,
                        "digest": result.digest,
                    },
                    indent=2,
                )
            )
            return 0

        if args.command == "verify-hash":
            is_valid = verify_file_hash(args.file_path, args.expected_hash, args.algorithm)
            print(json.dumps({"valid": is_valid}, indent=2))
            return 0 if is_valid else 1

        if args.command == "port-scan":
            result = scan_local_ports(
                host=args.host,
                start_port=args.start_port,
                end_port=args.end_port,
                timeout=args.timeout,
            )
            print(
                json.dumps(
                    {
                        "host": result.host,
                        "start_port": result.start_port,
                        "end_port": result.end_port,
                        "open_ports": result.open_ports,
                    },
                    indent=2,
                )
            )
            return 0
    except (FileNotFoundError, ValueError, OSError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
