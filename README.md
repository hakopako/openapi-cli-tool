# openapi-cli-tool
OpenAPI (Swagger 3.x) CLI Tool.


# Installation

Run this command:

```bash
$ python setup.py install
```

Then `openapi-cli-tool` command is installed in your environment.

# Commands

## List

```bash
$ openapi-cli-tool list [spec-path]

Method    Path       File
--------  ---------  ------------------------------------------
PUT       /avatar    ./tests/resources/spec/sample.yml
GET       /follwers  ./tests/resources/spec/folder1/sample2.yml
POST      /follwers  ./tests/resources/spec/folder1/sample2.yml
PUT       /follwers  ./tests/resources/spec/folder1/sample2.yml
POST      /pets      ./tests/resources/spec/sample.yml
GET       /posts     ./tests/resources/spec/folder1/sample.json
POST      /posts     ./tests/resources/spec/folder1/sample.json
GET       /users     ./tests/resources/spec/folder1/sample.json
POST      /users     ./tests/resources/spec/folder1/sample.json
```

## Find

```bash
$ openapi-cli-tool find [-m method] [-p path] [spec-path]
```

## Scaffold

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

Interactively input information of your api endpoint.  
Then template OpenAPI Specification is generated on your prompt.
