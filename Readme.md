# Cron Expression Parser

## Overview

This is a command line application that parses a cron string and expands each field to show the times at which it will run. The application handles the standard cron format with five time fields (minute, hour, day of month, month, and day of week) plus a command.

## Features

- Parses and expands cron expressions.
- Supports special characters such as `*`, `,`, `-`, and `/`.
- Provides clear and formatted output.

## Prerequisites

Make sure Python 3 is installed on your machine.

### Checking Python Version

#### Linux and macOS

Open a terminal and run:

```bash
python3 --version
```

### Running the Program
unzip the zip provided
Then do the following command format
```bash
cd deliveroo_cron_parser
python3 __main__.py "0 15 10 * * /usr/bin/find"
```

### Running the test cases
Do the following command 
```bash
python3 -m unittest discover tests
```