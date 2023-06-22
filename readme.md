Install Requriemetns:

```bash
pip install -r requirements.txt
```

Run Python APP:

```bash
python app.py
```

Login API:
```bash
{{url}}/login
```
- It returns you token, which should have to be added in headers while calling the get request to books api


Books API

Add Header before sending request:

Autorization Bearer <token>

```bash
{{url}}/books
```
