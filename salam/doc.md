### Tools

```bash
dotnet publish -r osx-x64 -c Release -p PublishAot=true

ls -lah bin/Release/net8.0/osx-x64/native/demo-01

bin/Release/net8.0/osx-x64/native/demo-01
```

### Windows

```bash
dotnet publish -r win-x64 -c Release -p PublishAot=true
```

error : Cross-OS native compilation is not supported.
