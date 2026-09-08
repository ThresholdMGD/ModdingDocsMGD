#!/bin/bash

echo "MGD Documentation Build (Unix/Linux/macOS)"
echo "Using local Python virtual environment (mkenv)"
echo

PYTHON="mkenv/bin/python"
PIP="mkenv/bin/pip"

if [ -x "$PYTHON" ]; then
    "$PYTHON" build.py
    exit_code=$?
else
    echo "⚠ ERROR: Python venv not found at mkenv/bin/python"
    echo "Run: python3 -m venv mkenv && source mkenv/bin/activate"
    exit 1
fi

if [ $exit_code -ne 0 ]; then
    echo
    echo "Build failed with exit code $exit_code"
    exit $exit_code
fi

echo
echo "Build completed"
