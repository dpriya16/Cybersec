import socket

from cybersec_toolkit.port_scanner import scan_local_ports


def test_scan_local_ports_detects_open_port():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 0))
    server.listen(1)
    open_port = server.getsockname()[1]

    try:
        result = scan_local_ports("127.0.0.1", open_port, open_port, timeout=0.1)
        assert open_port in result.open_ports
    finally:
        server.close()

