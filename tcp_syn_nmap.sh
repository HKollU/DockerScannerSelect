#!/bin/bash
nmap -v -sS $1>TCPSYNScan.txt && cat TCPSYNScan.txt
