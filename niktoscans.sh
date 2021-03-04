#!/bin/bash
nikto -Display 1234V -h $1 >niktoScan.txt && cat niktoScan.txt
