import requests
import json


url = "https://www.kaggle.com/api/i/competitions.LeaderboardService/GetLeaderboard"

headers = {
    "Host": "www.kaggle.com",
    "Cookie": "ka_sessionid=87a3af8b8f821ce1f5bfe923d3f559c0; CSRF-TOKEN=CfDJ8J1i-7MzxEhBg3BSP9qFZm_B8iC7tnSgpXHO2xnK0jGsR46DGbzIU9LG55mK8IbpP5Em8qigGxVJwj445-Oi3UCfHt1DmdIx-xdhg9Cn2g; GCLB=CPe_0Mu93pm6fBAD; build-hash=cd4030193262b4bebbd652dcdaf5b3a312bbc532; _ga=GA1.1.1769480738.1762707698; XSRF-TOKEN=CfDJ8J1i-7MzxEhBg3BSP9qFZm9VE-BEZKlJJ_N77voga2uLiItwsc6NhQTIqvjT_QA_aAiy_o-dL2BbR8NQlmypLn314NOqLnr9-ldnT9vBnBpagw; CLIENT-TOKEN=eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJpc3MiOiJrYWdnbGUiLCJhdWQiOiJjbGllbnQiLCJzdWIiOiIiLCJuYnQiOiIyMDI1LTExLTA5VDE3OjAzOjMyLjQyNzM2MTFaIiwiaWF0IjoiMjAyNS0xMS0wOVQxNzowMzozMi40MjczNjExWiIsImp0aSI6IjBhMWQyMDA1LTcxZDEtNDdjOC05NWY5LTEyYzFjMWEwYzE0NSIsImV4cCI6IjIwMjUtMTItMDlUMTc6MDM6MzIuNDI3MzYxMVoiLCJhbm9uIjp0cnVlLCJmZiI6WyJCZW5jaG1hcmtPcGVuR3JhcGgiLCJLZXJuZWxzT3BlbkluQ29sYWJMb2NhbFVybCIsIk1ldGFzdG9yZUNoZWNrQWdncmVnYXRlRmlsZUhhc2hlcyIsIlVzZXJMaWNlbnNlQWdyZWVtZW50U3RhbGVuZXNzVHJhY2tpbmciLCJTdHNEb3dubG9hZCIsIktlcm5lbHNQYXlUb1NjYWxlIiwiQmVuY2htYXJrT3V0cHV0SW1wcm92ZW1lbnRzIiwiVGFza1NoYXJlVmlhUm9sZXMiLCJGZWF0dXJlZE1vZGVsc1NoZWxmIiwiRGF0YXNldFBvbGFyc0RhdGFMb2FkZXIiLCJCZW5jaG1hcmtTb2NpYWxTaGFyaW5nIiwiS2VybmVsc1NldHRpbmdzVGFiIiwiUmVxdWlyZVBlcnNvbmFWZXJpZmljYXRpb25Gb3JUcHUiLCJLZXJuZWxzRmlyZWJhc2VMb25nUG9sbGluZyIsIkZyb250ZW5kRXJyb3JSZXBvcnRpbmciLCJBbGxvd0ZvcnVtQXR0YWNobWVudHMiLCJUZXJtc09mU2VydmljZUJhbm5lciIsIkRhdGFzZXRVcGxvYWRlckR1cGxpY2F0ZURldGVjdGlvbiJdLCJmZmQiOnsiTW9kZWxJZHNBbGxvd0luZmVyZW5jZSI6IiIsIk1vZGVsSW5mZXJlbmNlUGFyYW1ldGVycyI6InsgXCJtYXhfdG9rZW5zXCI6IDEyOCwgXCJ0ZW1wZXJhdHVyZVwiOiAwLjQsIFwidG9wX2tcIjogNSB9IiwiU3BvdGxpZ2h0Q29tbXVuaXR5Q29tcGV0aXRpb24iOiIxMDU4NzQsMTAxMDM5LDExMzE1NSwxMDM0MzIsMTEzNjY0IiwiRmVhdHVyZWRCZW5jaG1hcmtzIjoiMTM3LDE2LDg2LDEzNCIsIkdldHRpbmdTdGFydGVkQ29tcGV0aXRpb25zIjoiMzEzNiw1NDA3LDg2NTE4LDM0Mzc3IiwiR2FtZUFyZW5hUmVhc29uaW5nVGV4dFNwZWVkIjoiMiIsIlN0c01pbkZpbGVzIjoiMTc1MDAwIiwiU3RzTWluR2IiOiIxIiwiR2FtZUFyZW5hUmVhc29uaW5nU3RlcER1cmF0aW9uIjoiMjAwMCIsIlBlcnNvbmFsQmVuY2htYXJrc1ByaW9yaXR5VGFza0lkcyI6IjEwNiwyMjksMTA1LDIyNywxMTAsMjI4LDExNiwyMzAsMTczLDIzMiwxNzUsMjM5LDI2NCwyNDksMjQ3IiwiQ2xpZW50UnBjUmF0ZUxpbWl0UXBzIjoiNDAiLCJDbGllbnRScGNSYXRlTGltaXRRcG0iOiI1MDAiLCJBZGRGZWF0dXJlRmxhZ3NUb1BhZ2VMb2FkVGFnIjoiZGlzYWJsZWQiLCJLZXJuZWxFZGl0b3JBdXRvc2F2ZVRocm90dGxlTXMiOiIzMDAwMCIsIktlcm5lbHNMNEdwdUNvbXBzIjoiODYwMjMsODQ3OTUsODg5MjUsOTE0OTYiLCJFbmFibGVDZG5DYWNoZSI6IiIsIkh0dHBHZXRFbmFibGVkUnBjcyI6IiIsIkZlYXR1cmVkQ29tbXVuaXR5Q29tcGV0aXRpb25zIjoiNjAwOTUsNTQwMDAsNTcxNjMsODA4NzQsODE3ODYsODE3MDQsODI2MTEsODUyMTAiLCJFbWVyZ2VuY3lBbGVydEJhbm5lciI6IiIsIkNvbXBldGl0aW9uTWV0cmljVGltZW91dE1pbnV0ZXMiOiIzMCIsIkdhbWVBcmVuYUZlYXR1cmVkTGVhZGVyYm9hcmRCZW5jaG1hcmtWZXJzaW9ucyI6IjcyIiwiQ2RuQ2FjaGVEaXNhYmxlZFJwY3MiOiIiLCJEYXRhc2V0c1NlbmRQZW5kaW5nU3VnZ2VzdGlvbnNSZW1pbmRlcnNCYXRjaFNpemUiOiIxMDAiLCJHYW1lQXJlbmFCZW5jaG1hcmtWZXJzaW9ucyI6IjcyLDE2MSwxMjkiLCJLZXJuZWxzUGF5VG9TY2FsZVByb1BsdXNHcHVIb3VycyI6IjMwIiwiS2VybmVsc1BheVRvU2NhbGVQcm9HcHVIb3VycyI6IjE1IiwiRW1lcmdlbmN5QWxlcnRCYW5uZXJGb3JVc2VyUHJvZmlsZSI6IiIsIktlcm5lbHNIMTAwQ29tcHMiOiIifSwicGlkIjoia2FnZ2xlLTE2MTYwNyIsInN2YyI6IndlYi1mZSIsInNkYWsiOiJBSXphU3lBNGVOcVVkUlJza0pzQ1pXVnotcUw2NTVYYTVKRU1yZUUiLCJibGQiOiJjZDQwMzAxOTMyNjJiNGJlYmJkNjUyZGNkYWY1YjNhMzEyYmJjNTMyIn0.; _ga_T7QHS60L4Q=GS2.1.s1762707697$o1$g1$t1762707850$j17$l0$h0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "X-Xsrf-Token": "CfDJ8J1i-7MzxEhBg3BSP9qFZm9VE-BEZKlJJ_N77voga2uLiItwsc6NhQTIqvjT_QA_aAiy_o-dL2BbR8NQlmypLn314NOqLnr9-ldnT9vBnBpagw",
    "Accept": "application/json",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Referer": "https://www.kaggle.com/competitions/titanic/leaderboard",
    "X-Kaggle-Build-Version": "cd4030193262b4bebbd652dcdaf5b3a312bbc532",
}

competitions = [
    {"slug": "titanic", "competitionId": 3136},
    {"slug": "titanic", "competitionId": 3136},
    {"slug": "titanic", "competitionId": 3136},
    {"slug": "titanic", "competitionId": 3136},
    {"slug": "titanic", "competitionId": 3136},
    {"slug": "titanic", "competitionId": 3136},
    {"slug": "titanic", "competitionId": 3136},
]

for comp in competitions:
    payload = {
        "competitionId": comp["competitionId"],
        "leaderboardMode": "LEADERBOARD_MODE_DEFAULT",
    }
    try:
        res = requests.post(url, headers=headers, json=payload, timeout=20)
        res.raise_for_status()
        data = res.json()
        print(f"\n✅ {comp['slug']} ({comp['competitionId']})")
        print(json.dumps(data, indent=2))
    except requests.exceptions.RequestException as e:
        print(f"\n❌ {comp['slug']} ({comp['competitionId']}): {e}")
