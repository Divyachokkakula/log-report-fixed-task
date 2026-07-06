tests/test_outputs.py

Python

import json

from pathlib import Path

REPORT = Path("/app/report.json")

def load_report():

with REPORT.open() as f:

return json.load(f)

def test_success_criterion_1_report_exists():

"""Success criterion 1: Create /app/report.json."""

assert REPORT.exists(), "report.json was not created"

def test_success_criterion_2_total_requests():

"""Success criterion 2: Count the total number of requests."""

report = load_report()

assert report["total_requests"] == 6

def test_success_criterion_3_unique_ips():

"""Success criterion 3: Count the number of unique client IP addresses."""

report = load_report()

assert report["unique_ips"] == 3

def test_success_criterion_4_top_path():

"""Success criterion 4: Determine the most frequently requested path."""

report = load_report()

assert report["top_path"] == "/index.html"
