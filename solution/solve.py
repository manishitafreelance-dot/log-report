import json
import re
from collections import Counter
from pathlib import Path

log_path = Path("/app/access.log")
report_path = Path("/app/report.json")

path_counts = Counter()
ips = set()
total_requests = 0

for raw_line in log_path.read_text().splitlines():
    line = raw_line.strip()
    if not line:
        continue
    total_requests += 1
    ips.add(line.split()[0])
    match = re.search(r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ', line)
    if match:
        path_counts[match.group(1)] += 1

top_path = path_counts.most_common(1)[0][0] if path_counts else ""
report_path.write_text(
    json.dumps(
        {
            "total_requests": total_requests,
            "unique_ips": len(ips),
            "top_path": top_path,
        },
        indent=2,
        sort_keys=True,
    )
    + "\n"
)
