#!/bin/bash
nmap -v -A $1>AggressiveScan.txt && cat AggressiveScan.txt
