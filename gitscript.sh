#!/bin/bash
git add -A
git status
sleep 1
timestamp=$(date "+%Y-%m-%d %H:%M:%S")
git commit -m "Automated commit at $timestamp"
git push origin main
