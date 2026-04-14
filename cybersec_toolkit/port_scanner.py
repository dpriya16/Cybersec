"""Simple TCP local port scanner for beginner labs."""

from dataclasses import dataclass
import socket


@dataclass
class PortScanResult:
    """Stores local port scanning results."""

    host: str
    start_port: int
    end_port: int
    open_ports: list[int]


def scan_local_ports(host: str, start_port: int, end_port: int, timeout: float = 0.3) -> PortScanResult:
    """
    Scan a host for open TCP ports in a range.

    This is intentionally basic and should only be used on systems
    you own or have explicit permission to test.
    """
    if start_port < 1 or end_port > 65535 or start_port > end_port:
        raise ValueError("Port range must be between 1 and 65535, and start <= end.")

    open_ports: list[int] = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        try:
            if sock.connect_ex((host, port)) == 0:
                open_ports.append(port)
        finally:
            sock.close()

    return PortScanResult(
        host=host,
        start_port=start_port,
        end_port=end_port,
        open_ports=open_ports,
    )
