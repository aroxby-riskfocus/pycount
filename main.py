#!/usr/bin/env python
import sys


def bisect(arr, pred):
    matched = []
    unmatched = []
    for elem in arr:
        if pred(elem):
            matched.append(elem)
        else:
            unmatched.append(elem)
    return matched, unmatched


def range_length(a, b):
    start = int(a.strip())
    stop = int(b.strip())
    return stop - start + 1


def count(data):
    items = data.split(',')
    ranges, items = bisect(items, lambda e: '-' in e)
    total = len(items)
    for rnge in ranges:
        try:
            start, stop = rnge.split('-')
        except ValueError:
            msg = 'Ranges must have exactly two values, {} is not valid'.format(rnge)
            raise ValueError(msg)
        total += range_length(start, stop)
    return total


def main():
    data = sys.stdin.read().strip()
    total = count(data)
    print total


if __name__ == '__main__':
    main()
