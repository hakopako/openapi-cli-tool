![openapi-cli-tool](https://raw.githubusercontent.com/hakopako/openapi-cli-tool/master/doc/logo.png)

[![Build Status](https://travis-ci.com/hakopako/openapi-cli-tool.svg?branch=master)](https://travis-ci.com/hakopako/openapi-cli-tool)

# openapi-cli-tool
OpenAPI (Swagger 3.x) CLI Tool.  

- Supports multi file extension (json|yaml|yml).
- List up defined APIs.
- Display a API specification which is resolved `$ref`.
- OAS interactive scaffold.  


# Installation

Execute Python installation command on your machine.  
Supports Python 2.7, 3.4 <=.

```bash
$ python setup.py install
```

Then `openapi-cli-tool` command is installed.

# Usage

```
$ openapi-cli-tool --help
Usage: openapi-cli-tool [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  bundle    Bundle multi-file into one.
  list      List up APIs in a specific file or directory.
  resolve   Display `$ref` resolved API specification.
  scaffold  Interactively create a simple OpenAPI Specification.
```

## Bundle

Bundle multi-file specifications into one, regardless of file extension (json|yaml|yml).

```
$ openapi-cli-tool bundle --help
Usage: openapi-cli-tool bundle [OPTIONS] FILE_PATH

  Bundle multi-file into one.

Options:
  -t, --title TEXT    [default: API]
  -v, --version TEXT  [default: v1.0]
  -l, --license TEXT  [default: Apache 2.0]
  -s, --server TEXT   [default: http://localhost]
  --help              Show this message and exit.
```

example:
```
$ openapi-cli-tool bundle FILE_PAH > ./specification.json
```

## List

List up APIs from specification file/directory regardless of file extension (json|yaml|yml).

```bash
$ openapi-cli-tool list [spec-path]

Method    Path       File
--------  ---------  ------------------------------------------
PUT       /avatar    ./tests/resources/spec/sample.yml
GET       /follwers  ./tests/resources/spec/folder1/sample2.yaml
POST      /follwers  ./tests/resources/spec/folder1/sample2.yaml
PUT       /follwers  ./tests/resources/spec/folder1/sample2.yaml
POST      /pets      ./tests/resources/spec/sample.yml
GET       /posts     ./tests/resources/spec/folder1/sample.json
POST      /posts     ./tests/resources/spec/folder1/sample.json
GET       /users     ./tests/resources/spec/folder1/sample.json
POST      /users     ./tests/resources/spec/folder1/sample.json
```


## Resolve

Display an API specification which is resolved multi-file API specification via $ref pointers.  

```bash
$ openapi-cli-tool resolve [method] [path] [spec-path]
```


## Scaffold

Interactively input information of your API.  
A simple OpenAPI Specification is generated on your prompt.

```bash
$ openapi-cli-tool scaffold

Please enter title [""]: sample
Please enter version [v1.0]:
Please enter license [Apache 2.0]:
Please enter server url [http://example.com]:
Please enter path [/]: /example
Please enter method for /example [get|post|put|delete|head|option|trace]: get
Please enter description for get /example [""]: sample get endpoint
Please enter response code for get /example [200]:
```
