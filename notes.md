# Request

Example Bash request (curl)




```bash
POST /api/i/competitions.LeaderboardService/GetLeaderboard HTTP/2
Host: www.kaggle.com
Cookie: ka_sessionid=87a3af8b8f821ce1f5bfe923d3f559c0; CSRF-TOKEN=CfDJ8J1i-7MzxEhBg3BSP9qFZm_B8iC7tnSgpXHO2xnK0jGsR46DGbzIU9LG55mK8IbpP5Em8qigGxVJwj445-Oi3UCfHt1DmdIx-xdhg9Cn2g; GCLB=CPe_0Mu93pm6fBAD; build-hash=cd4030193262b4bebbd652dcdaf5b3a312bbc532; _ga=GA1.1.1769480738.1762707698; XSRF-TOKEN=CfDJ8J1i-7MzxEhBg3BSP9qFZm9VE-BEZKlJJ_N77voga2uLiItwsc6NhQTIqvjT_QA_aAiy_o-dL2BbR8NQlmypLn314NOqLnr9-ldnT9vBnBpagw; CLIENT-TOKEN=eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJpc3MiOiJrYWdnbGUiLCJhdWQiOiJjbGllbnQiLCJzdWIiOiIiLCJuYnQiOiIyMDI1LTExLTA5VDE3OjAzOjMyLjQyNzM2MTFaIiwiaWF0IjoiMjAyNS0xMS0wOVQxNzowMzozMi40MjczNjExWiIsImp0aSI6IjBhMWQyMDA1LTcxZDEtNDdjOC05NWY5LTEyYzFjMWEwYzE0NSIsImV4cCI6IjIwMjUtMTItMDlUMTc6MDM6MzIuNDI3MzYxMVoiLCJhbm9uIjp0cnVlLCJmZiI6WyJCZW5jaG1hcmtPcGVuR3JhcGgiLCJLZXJuZWxzT3BlbkluQ29sYWJMb2NhbFVybCIsIk1ldGFzdG9yZUNoZWNrQWdncmVnYXRlRmlsZUhhc2hlcyIsIlVzZXJMaWNlbnNlQWdyZWVtZW50U3RhbGVuZXNzVHJhY2tpbmciLCJTdHNEb3dubG9hZCIsIktlcm5lbHNQYXlUb1NjYWxlIiwiQmVuY2htYXJrT3V0cHV0SW1wcm92ZW1lbnRzIiwiVGFza1NoYXJlVmlhUm9sZXMiLCJGZWF0dXJlZE1vZGVsc1NoZWxmIiwiRGF0YXNldFBvbGFyc0RhdGFMb2FkZXIiLCJCZW5jaG1hcmtTb2NpYWxTaGFyaW5nIiwiS2VybmVsc1NldHRpbmdzVGFiIiwiUmVxdWlyZVBlcnNvbmFWZXJpZmljYXRpb25Gb3JUcHUiLCJLZXJuZWxzRmlyZWJhc2VMb25nUG9sbGluZyIsIkZyb250ZW5kRXJyb3JSZXBvcnRpbmciLCJBbGxvd0ZvcnVtQXR0YWNobWVudHMiLCJUZXJtc09mU2VydmljZUJhbm5lciIsIkRhdGFzZXRVcGxvYWRlckR1cGxpY2F0ZURldGVjdGlvbiJdLCJmZmQiOnsiTW9kZWxJZHNBbGxvd0luZmVyZW5jZSI6IiIsIk1vZGVsSW5mZXJlbmNlUGFyYW1ldGVycyI6InsgXCJtYXhfdG9rZW5zXCI6IDEyOCwgXCJ0ZW1wZXJhdHVyZVwiOiAwLjQsIFwidG9wX2tcIjogNSB9IiwiU3BvdGxpZ2h0Q29tbXVuaXR5Q29tcGV0aXRpb24iOiIxMDU4NzQsMTAxMDM5LDExMzE1NSwxMDM0MzIsMTEzNjY0IiwiRmVhdHVyZWRCZW5jaG1hcmtzIjoiMTM3LDE2LDg2LDEzNCIsIkdldHRpbmdTdGFydGVkQ29tcGV0aXRpb25zIjoiMzEzNiw1NDA3LDg2NTE4LDM0Mzc3IiwiR2FtZUFyZW5hUmVhc29uaW5nVGV4dFNwZWVkIjoiMiIsIlN0c01pbkZpbGVzIjoiMTc1MDAwIiwiU3RzTWluR2IiOiIxIiwiR2FtZUFyZW5hUmVhc29uaW5nU3RlcER1cmF0aW9uIjoiMjAwMCIsIlBlcnNvbmFsQmVuY2htYXJrc1ByaW9yaXR5VGFza0lkcyI6IjEwNiwyMjksMTA1LDIyNywxMTAsMjI4LDExNiwyMzAsMTczLDIzMiwxNzUsMjM5LDI2NCwyNDksMjQ3IiwiQ2xpZW50UnBjUmF0ZUxpbWl0UXBzIjoiNDAiLCJDbGllbnRScGNSYXRlTGltaXRRcG0iOiI1MDAiLCJBZGRGZWF0dXJlRmxhZ3NUb1BhZ2VMb2FkVGFnIjoiZGlzYWJsZWQiLCJLZXJuZWxFZGl0b3JBdXRvc2F2ZVRocm90dGxlTXMiOiIzMDAwMCIsIktlcm5lbHNMNEdwdUNvbXBzIjoiODYwMjMsODQ3OTUsODg5MjUsOTE0OTYiLCJFbmFibGVDZG5DYWNoZSI6IiIsIkh0dHBHZXRFbmFibGVkUnBjcyI6IiIsIkZlYXR1cmVkQ29tbXVuaXR5Q29tcGV0aXRpb25zIjoiNjAwOTUsNTQwMDAsNTcxNjMsODA4NzQsODE3ODYsODE3MDQsODI2MTEsODUyMTAiLCJFbWVyZ2VuY3lBbGVydEJhbm5lciI6IiIsIkNvbXBldGl0aW9uTWV0cmljVGltZW91dE1pbnV0ZXMiOiIzMCIsIkdhbWVBcmVuYUZlYXR1cmVkTGVhZGVyYm9hcmRCZW5jaG1hcmtWZXJzaW9ucyI6IjcyIiwiQ2RuQ2FjaGVEaXNhYmxlZFJwY3MiOiIiLCJEYXRhc2V0c1NlbmRQZW5kaW5nU3VnZ2VzdGlvbnNSZW1pbmRlcnNCYXRjaFNpemUiOiIxMDAiLCJHYW1lQXJlbmFCZW5jaG1hcmtWZXJzaW9ucyI6IjcyLDE2MSwxMjkiLCJLZXJuZWxzUGF5VG9TY2FsZVByb1BsdXNHcHVIb3VycyI6IjMwIiwiS2VybmVsc1BheVRvU2NhbGVQcm9HcHVIb3VycyI6IjE1IiwiRW1lcmdlbmN5QWxlcnRCYW5uZXJGb3JVc2VyUHJvZmlsZSI6IiIsIktlcm5lbHNIMTAwQ29tcHMiOiIifSwicGlkIjoia2FnZ2xlLTE2MTYwNyIsInN2YyI6IndlYi1mZSIsInNkYWsiOiJBSXphU3lBNGVOcVVkUlJza0pzQ1pXVnotcUw2NTVYYTVKRU1yZUUiLCJibGQiOiJjZDQwMzAxOTMyNjJiNGJlYmJkNjUyZGNkYWY1YjNhMzEyYmJjNTMyIn0.; _ga_T7QHS60L4Q=GS2.1.s1762707697$o1$g1$t1762707850$j17$l0$h0
Content-Length: 67
Sec-Ch-Ua-Platform: "Windows"
X-Xsrf-Token: CfDJ8J1i-7MzxEhBg3BSP9qFZm9VE-BEZKlJJ_N77voga2uLiItwsc6NhQTIqvjT_QA_aAiy_o-dL2BbR8NQlmypLn314NOqLnr9-ldnT9vBnBpagw
Accept-Language: en-US,en;q=0.9
Sec-Ch-Ua: "Chromium";v="139", "Not;A=Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
X-Kaggle-Build-Version: cd4030193262b4bebbd652dcdaf5b3a312bbc532
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36
Accept: application/json
Content-Type: application/json
Origin: https://www.kaggle.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://www.kaggle.com/competitions/titanic/leaderboard
Accept-Encoding: gzip, deflate, br
Priority: u=1, i

{"competitionId":3136,"leaderboardMode":"LEADERBOARD_MODE_DEFAULT"}
```

Response (JSON)

```json
HTTP/2 200 OK
Content-Type: application/json
Date: Sun, 09 Nov 2025 17:04:45 GMT
Vary: Accept-Encoding
X-Frame-Options: SAMEORIGIN
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
Content-Security-Policy: object-src 'none'; script-src 'nonce-9vRUm6niBEFD70R56fhwMw==' 'report-sample' 'unsafe-inline' 'unsafe-eval' 'strict-dynamic' https: http:; base-uri 'none'; report-uri https://csp.withgoogle.com/csp/kaggle/20201130; frame-src 'self' https://www.kaggleusercontent.com https://www.youtube.com/embed/ https://youtu.be https://polygraph-cool.github.io https://www.google.com/recaptcha/ https://www.docdroid.com https://www.docdroid.net https://kaggle-static.storage.googleapis.com https://kkb-production.jupyter-proxy.kaggle.net https://kkb-production.firebaseapp.com https://kaggle-metastore.firebaseapp.com https://apis.google.com https://content-sheets.googleapis.com/ https://accounts.google.com/ https://storage.googleapis.com https://docs.google.com https://drive.google.com https://calendar.google.com/ https://google.qualtrics.com/ https://player.kick.com/ https://player.twitch.tv/ https://kaggle.com http://localhost:* https://localhost:* localhost:* ;
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
Via: 1.1 google
Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000

{"publicLeaderboard":[{"teamId":12689008,"submissionId":46787804,"rank":1,"displayScore":"1.00000"},{"teamId":14366783,"submissionId":46788751,"rank":2,"displayScore":"1.00000"},{"teamId":14118222,"submissionId":46788774,"rank":3,"displayScore":"1.00000"},{"teamId":12801551,"submissionId":46791313,"rank":4,"displayScore":"1.00000"},{"teamId":14356364,"submissionId":46796913,"rank":5,"displayScore":"1.00000"},{"teamId":6497188,"submissionId":46799334,"rank":6,"displayScore":"1.00000"},{"teamId":12408744,"submissionId":46812059,"rank":7,"displayScore":"1.00000"},{"teamId":14374425,"submissionId":46818933,"rank":8,"displayScore":"1.00000"},{"teamId":14352923,"submissionId":46830974,"rank":9,"displayScore":"1.00000"},{"teamId":14379279,"submissionId":46840229,"rank":10,"displayScore":"1.00000"},{"teamId":13529434,"submissionId":46880931,"rank":11,"displayScore":"1.00000"},{"teamId":14403377,"submissionId":46920238,"rank":12,"displayScore":"1.00000"},{"teamId":14037607,"submissionId":46924831,"rank":13,"displayScore":"1.00000"},{"teamId":14406787,"submissionId":46930870,"rank":14,"displayScore":"1.00000"},{"teamId":14410527,"submissionId":46944690,"rank":15,