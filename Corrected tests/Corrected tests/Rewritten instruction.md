Analyze the Apache-style access log at /app/access.log and create /app/report.json.

The output file must be valid JSON with exactly these fields:

{

"total_requests": integer,

"unique_ips": integer,

"top_path": string

}

Success criteria

Create the file /app/report.json.

Set total_requests to the total number of log entries in /app/access.log.

Set unique_ips to the number of unique client IP addresses in the log.

Set top_path to the most frequently requested path in the log.
