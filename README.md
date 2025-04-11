## What is this?
jdtls, LSP for Java, is following gradle and maven as default, but not following ant.

But when you develop ant project with neovim, that is so hard.

Antenna is a CLI tool for generating .project and .classpath for jdtls from build.xml, ant configuration file, ant configuration file.

## Installation
```bash
pip install antenna
```

## Usage
Run the below command on the ant project root.

```bash
antenna <build.xml path>
```
You can get `.project` and `.classpath` in the current directory.

## Contribution
You need to run ci.sh.
```bash
./ci.sh # mypy and ruff
```
Any contribution is wellcome.
