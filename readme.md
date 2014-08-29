# Secrets

A way to keep your secrets while in public. See [example.py](example.py).

### Generating keys
```bash
openssl genrsa -out key 2048
openssl rsa -in key -pubout -out key.pub
```

### Creating secrets
```bash
./encrypt MY_SECRET
```

### Dependencies
```bash
pip install PyCrypto
```