# openapi-cli-tool
OpenAPI (Swagger 3.x) CLI Tool.


# Installation

Run this command:

```bash
$ python setup.py install
```

Then `$ openapi-cli-tool` command is installed in your environment.

# Tools

- [ ] List
- [ ] Search
- [ ] Find
- [x] Scaffold

## List

```bash
$ openapi-cli-tool list [spec-path]
```

## Search

```bash
$ openapi-cli-tool list [keyword] [spec-path]
```

## Find

```bash
$ openapi-cli-tool find [-m method] [-p path] [spec-path]
```

## Scaffold

```bash
$ openapi-cli-tool scaffold
```

Interactively input information of your api endpoint.  
Then template OpenAPI Specification is generated on your prompt.
