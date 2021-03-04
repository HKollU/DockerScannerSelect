#!/bin/bash
nmap -v -sA $1 >>TCPACKScan.txt && cat TCPACKScan.txt
