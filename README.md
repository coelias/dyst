# dyst
Dynamic histograms in the terminal

## Installation

```
pip install dyst
```

## Usage

```
cuf -f 3 file.tsv | dyst
```

![Alt text](/img/cast3.gif "screencast")

## Options

```
usage: dyst [-h] [-w] [-b BINS] [-c COLUMNS] [-p] [-n] [-m MIN] [-x MAX]
            [inputfile]

Text mode Histogram software

positional arguments:
  inputfile   Input file containing data

optional arguments:
  -h, --help  show this help message and exit
  -w          process words instead of numbers
  -b BINS     Bins shows in the histogram (numeric mode only) [10]
  -c COLUMNS  Histogram width in columns [80]
  -p          Show percentage for each bar
  -n          Don't show progress only final result
  -m MIN      Minimum value to show in the histogram
  -x MAX      Maximum value to show in the histogram
```

## Usage example

[![asciicast](https://asciinema.org/a/5LfDABPRYeGmpVBBFpbb9qpNN.png)](https://asciinema.org/a/5LfDABPRYeGmpVBBFpbb9qpNN)
