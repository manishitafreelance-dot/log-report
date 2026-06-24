#!/bin/bash
set -euo pipefail

mkdir -p /logs/verifier
if pytest /tests/test_outputs.py -rA; then
  echo 1 > /logs/verifier/reward.txt
  cat > /logs/verifier/ctrf.json <<'JSON'
{"results":[{"status":"passed"}]}
JSON
else
  echo 0 > /logs/verifier/reward.txt
  cat > /logs/verifier/ctrf.json <<'JSON'
{"results":[{"status":"failed"}]}
JSON
  exit 1
fi
