# Command Line Interface

python-re3data.

**Usage**:

```console
$ re3data [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-V, --version`: Show python-re3data version and exit.
* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `repository`

## `re3data repository`

**Usage**:

```console
$ re3data repository [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `get`: Get the metadata of a specific repository.
* `list`: List the metadata of all repositories in...

### `re3data repository get`

Get the metadata of a specific repository.

**Usage**:

```console
$ re3data repository get [OPTIONS] REPOSITORY_ID
```

**Arguments**:

* `REPOSITORY_ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `re3data repository list`

List the metadata of all repositories in the re3data API.

**Usage**:

```console
$ re3data repository list [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.
