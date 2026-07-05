# Phishing Detector API

## Base URL

```
http://127.0.0.1:5000
```

---

## GET /

Checks whether the server is running.

Response

```
Phishing Detector API is running!
```

---

## POST /analyze

Analyzes a URL.

### Request

```json
{
    "url":"https://google.com"
}
```

### Success Response

```json
{
    "url":"https://google.com",
    "basic_info":{},
    "checks":{},
    "ssl":{},
    "virustotal":{},
    "result":{}
}
```

### Error Response

```json
{
    "error":"No URL provided."
}
```