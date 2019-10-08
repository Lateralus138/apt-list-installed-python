# apt-list-installed-python

Retrieve a simple list of application packages installed with the apt package management system&#46;

## About apt-list-installed

apt-list-installed is a cli utility that lists apt package names&#46;

- Can be used as a normal &#46;py script&#46;
- You can strip the bash script and use it, with a bit of modification of course&#46;
- Use as an executable&#46; One has been compiled; though, you can do so yourself with with nuitka&#46;
- I provided a bash script. The executable might work better with other programs&#46;

## Usage: apt-list-installed [-h,--help]

### If compiled

- apt-get-installed [-h,--help]

### If Python script (&#46;py)

- python3 apt-get-installed&#46;py [-h,--help]

### If bash script

```bash
./apt-list-installed.sh
```

or

```bash
apt-list-installed
```

while in a &#36;PATH directory

(&#46;sh extension can be removed)

### @params

- -h, --help        This help message

## Current Release

[Current Executable](https://github.com/Lateralus138/apt-list-installed-python/releases/tag/1.10.7.19 "Release Page")

[Current Python Script](src/apt-list-installed-python.py "Python Script")

[Bash Script](src/apt-list-installed.sh "Bash Script")

## Motivation

I wanted a faster way to retrieve simple package names for APT&#46;

## Installation

Copy executable to a directory in &#36;PATH and make sure it is set to exectuable &#40;x&#41;&#46;

Example given&#58;

```bash
sudo cp apt-list-installed /usr/bin/apt-list-installed
sudo chmod +x /usr/bin/apt-list-installed
```

## Test

Tested on&#58;

```bash
flux @ ❨ /home/flux/.git/apt-list-installed-python ❩ > uname -a | awk '{print $4" "$12" "$1" "$3}'
#74-Ubuntu x86_64 Linux 4.15.0-65-generic

```

## Contributors

Ian Pride @ faithnomoread@yahoo.com - [Lateralus138][FluxApex] @ New Pride Services

## License

This license file: [LICENSE](LICENSE "GPLV3 License File")

```LICENSE
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    License provided in gpl.txt

```
