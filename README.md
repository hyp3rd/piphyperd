# piphyperd

A simple python package to leverage pip programmatically.
**piphyperd** is a wrapper around **pip**; it can provide features like automation or dependencies control within your workflows.

## About this package

The reasons behind this package, in alternative to the standard `pip` (`import pip`) module, are in the attempt to expose a more stable interface, when programmatically installing or managing python packages, within pipelines or automation workflows.

Although it is a **Python** module, and it is available via `import pip`, by design, **pip** is not supposed to be a library; every detail is subject to changes for any reason, from the import name itself to its API. It might be better to call the pip’s internal APIs differently.

### Pitfalls

When leveraging `pip` programmatically, there are also other topics worth considering:

1. The pip code assumes that it is in sole control of the global state of the program;
2. pip’s code is not thread-safe. If you were to run pip in a thread;
3. pip assumes that once it has finished its work, the process terminates.

Furthermore, installing packages under the `sys.path` from a running Python process might result in unexpected or undesired behaviors.

Taking everything into account, still might be necessary, or usefull, handling pip packages within code and automations, as much as possible in controlled manner. The most reliable way to do so, is leveraging pip in a `subprocess`:

```python
# leverage subprocess.Popen to execute pip commands
subprocess.process = Popen(
    [sys.executable, "-m", "pip", command] + self.pip_options + self.packages + self.command_args, stdout=PIPE, stderr=PIPE)
```

For further information, continue reading from the source of this topic at the [the official pypa](https://pip.pypa.io/en/latest/user_guide/#using-pip-from-your-program) user guide.

## Install the package

Refer to the official [project page](https://pypi.org/project/piphyperd/) for further information about the package status and releases.

To install the latest version, run the following command in your terminal:

```bash
pip install --user piphyperd
```

## API overview

Once installed, you can import the package as follows `from piphyperd import PipHyperd`.
The module is wrapping pip commands in methods, exposed through the object `PipHyperd`. You can initialize it by optionally passing pip commands extra options:

```python
class PipHyperd:
    def __init__(self, *pip_options):
# ...
```

The API exposed conveniently wraps a set of pip commands that can help generating virtual environments, reports of the installed packages, outdated libraries. The `stdout` and `stderr` are returned by each method, allowing to store the output or to read it in a second instance.

### Object description

To follow, a brief walkthrough through the methods exposed by the `PipHyperd` object.

#### pip freeze

Output installed pip packages in requirements format:

```python
piphyperd.PipHyperd().freeze()
```

#### pip list

List installed pip packages.

```python
piphyperd.PipHyperd("--verbose").list() # the argument "--verbose" is of course optional
```

#### pip show {{ package }}

Show information about installed packages.

```python
piphyperd.PipHyperd("--verbose").show("ansible")
```

#### pip check

Verify installed packages have compatible dependencies.

```python
piphyperd.PipHyperd().check()
```

#### pip install {{ packages }}

Install pip packages.

```python
piphyperd.PipHyperd("-U").install("ansible", "cryptography") # -U is of course optional, set here as example
```

#### pip download {{ package }}

Download pip packages.

```python
piphyperd.PipHyperd("-U").download("ansible", "pip", "cryptography", destination="/your/path/here") # the destination argument is optional
```

#### pip uninstall {{ packages }}

Uninstall pip packages.

```python
piphyperd.PipHyperd().uninstall("ansible", "pip", "cryptography") # the destination argument is optional
```

## License

[GNU General Public License v3 (GPLv3)](https://gitlab.com/hyperd/piphyperd/blob/master/LICENSE)

## Author Information

[Francesco Cosentino](https://www.linkedin.com/in/francesco-cosentino/)

I'm a surfer, a crypto trader, and a DevSecOps Engineer with 15 years of experience designing highly-available distributed production environments and developing cloud-native apps in public and private clouds.
