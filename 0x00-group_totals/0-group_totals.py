#!/usr/bin/python3


def group_totals(strArr):
    totals = {}
    
    for x in strArr:
        key, value = x.split(":")
        value = int(value)
        if key in totals:
            totals[key] += value
        else:
            totals[key] = value
        sorted_totals = sorted([k + ":" + str(v) for k, v in totals.items() if v != 0])
    return ", ".join(sorted_totals)
