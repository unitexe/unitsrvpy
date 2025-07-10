# unitsrvpy
Initialize virtual environment from lock file.
```bash
pdm sync
```

Build (i.e. codegen & generate whl).
```bash
pdm build
```

Install `unitsrvpy` to virtual environment.
```bash
pdm install
```

Run linting & formatting.
```bash
pdm run all
```

List endpoints of the `Wireguard` service.
```bash
grpcurl -plaintext 10.0.0.43:60000 list unit.network.v0.Wireguard
```

Get devices wg pubkey.
```bash
grpcurl -plaintext -import-path ./proto -proto wireguard.proto -d '{}' '10.0.0.43:60000' unit.network.v0.Wireguard/GetPublicKey
```
