# Zenquotes

Utilizando o curl

```bash
curl -s https://zenquotes.io/api/quotes | jq -r '.[].q | gsub("\""; "")' > frases.txt
```