![openapi-cli-tool](https://raw.githubusercontent.com/hakopako/openapi-cli-tool/master/doc/logo.png)


[![Build Status](https://travis-ci.com/hakopako/openapi-cli-tool.svg?branch=master)](https://travis-ci.com/hakopako/openapi-cli-tool)
 <img src="https://img.shields.io/badge/version-v0.2.1-green.svg">
 <img src="https://img.shields.io/badge/license-MIT-lightgray.svg">  
<img src="https://img.shields.io/badge/python-2.7,3.4<=-blue.svg"> <img src="https://img.shields.io/badge/swagger-3.x-yellow.svg">

# openapi-cli-tool
OpenAPI (Swagger 3.x) CLI Tool.  

- Supports multiple file extensions (json|yaml|yml).
- Can list up defined API paths.
- Display an API specification which is resolved (`$ref`).
- Bundle multi-file into one (output to json|yaml|html).
- OAS interactive scaffolding.  

# Requirements

Python 2.7, 3.4 <=.

# Installation

With pip:

```bash
$ pip install openapi-cli-tool
```
Manually:  
Clone the repository and execute the Python installation command on your machine.  

```bash
$ pip -r requirements.txt install
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
  bundle    Bundle multiple files into one.
  list      List up API paths in a file or directory.
  resolve   Display `$ref` resolved API specification.
  scaffold  Interactively create a simple OpenAPI Specification.
```

## Bundle

Bundle multi-file specifications into one, regardless of file extension (json|yaml|yml).

```
$ openapi-cli-tool bundle --help
Usage: openapi-cli-tool bundle [OPTIONS] FILE_PATHS

  Bundle multiple files into one.

Options:
  -f, --file TEXT  Load common objects such as info and servers from a
                   specific file. Default is a file which is the top of list
                   command result.
  -t, --type TEXT  Export data type. {json|yaml|html}  [default: json]
  --help           Show this message and exit.
```

example:
```
$ openapi-cli-tool bundle -t html file1.json file2.yaml` > ./specification.html
```

In the html file, an unpkg version of [swagger-ui](https://github.com/swagger-api/swagger-ui) is embedded. Rendered screenshot below:  


![bundle-html-img](https://raw.githubusercontent.com/hakopako/openapi-cli-tool/master/doc/bundle-html.png)


## List

List up API paths from a file/directory regardless of the file extension (json|yaml|yml).

```bash
$ openapi-cli-tool list `find ./spec`

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

Display an API specification which is resolved from  a multi-file API specification via $ref pointers.  

```
Usage: openapi-cli-tool resolve [OPTIONS] METHOD PATH FILE_PATHS

  Display `$ref` resolved API specification.

Options:
  -t, --type TEXT  Export data type. {json|yaml}  [default: json]
  --help           Show this message and exit.
```

example:
```bash
$ openapi-cli-tool resolve post /cats `find ./tests/resources/spec`
```


## Scaffold

Interactively input information of your API.  
A simple OpenAPI Specification is generated from your prompt.

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
