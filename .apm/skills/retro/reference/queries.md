# Run discovery queries

Use `session_store_sql` (DuckDB). Always time-bound and use LIMIT. Replace `<skill>` and `<days>`.

Find invocations:
```sql
SELECT session_id, turn_index, timestamp, substr(user_message, 1, 500) AS prompt
FROM turns
WHERE timestamp > now() - INTERVAL '<days> days'
  AND user_message ILIKE '%/<skill>%'
ORDER BY timestamp DESC LIMIT 50
```

Follow-up turns for one run (after narrowing by session_id):
```sql
SELECT turn_index, substr(user_message, 1, 300) AS user, substr(assistant_response, 1, 800) AS reply
FROM turns
WHERE session_id = '<id>' AND turn_index >= <start> ORDER BY turn_index LIMIT 20
```

Files changed and tool outcomes:
```sql
SELECT file_path, tool_name, turn_index FROM session_files WHERE session_id = '<id>' LIMIT 100
```
```sql
SELECT tool_name, success, error_code FROM tool_executions
WHERE session_id = '<id>' AND started_at > now() - INTERVAL '<days> days' LIMIT 200
```

Filter by repository through `sessions.repository` when scoping. Local-only stores need SQLite syntax (`LIKE`, `date('now', ...)`).
