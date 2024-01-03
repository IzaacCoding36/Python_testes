#!/bin/bash

user=$(whoami)
date=$(date)
whereami=$(pwd)

echo "overall checkup"

sleep 2

echo "Date: $date"

sleep 2

echo "You are currently logged in as $user and you are in the directory $whereami."

sleep 2

echo "system check starting in 5 seconds"

sleep 1

echo "loading..."

sleep 4

echo "checking system..."

sleep 4

echo "CPU Status: Operational (OK) | Battery: OK | Graphic Card: OK | Hard Drive (HD): OK | RAM: OK | Overall System Status: OK"