import json
from pathlib import Path


def test_report_exists():
    """The agent must create `/app/report.json`."""
    assert Path("/app/report.json").exists(), "no report.json found"


def test_report_is_valid_json():
    """The report file must contain valid JSON."""
    json.loads(Path("/app/report.json").read_text())


def test_report_total_requests():
    """The report must count all non-empty log lines."""
    data = json.loads(Path("/app/report.json").read_text())
    assert data["total_requests"] == 6


def test_report_unique_ips():
    """The report must count distinct client IP addresses."""
    data = json.loads(Path("/app/report.json").read_text())
    assert data["unique_ips"] == 3


def test_report_top_path():
    """The report must identify the most frequently requested path."""
    data = json.loads(Path("/app/report.json").read_text())
    assert data["top_path"] == "/index.html"
