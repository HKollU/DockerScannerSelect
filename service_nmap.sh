#!/bin/bash
nmap -v -sV -version-intensity 5 $1>ServiceScan.txt && cat ServiceScan.txt
