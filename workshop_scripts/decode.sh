#!/bin/bash
OUTPUT__FILE="workshop_data/16.txt"
INPUT_FILE="encrypted_data/16.txt"

base64 --decode "$INPUT_FILE" > "$OUTPUT_FILE"

echo "decode complete"
