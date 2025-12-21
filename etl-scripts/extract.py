#!/usr/bin/env python3
"""
Extract stage - Reads data from a source
"""
import json
import logging
import sys
from pathlib import Path

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def extract_data():
    """Extract sample data"""
    logger.info("Starting data extraction")
    
    # Simulate extracted data
    data = [
        {"id": 1, "name": "John Doe", "email": "john@example.com", "value": 45.7},
        {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "value": 89.2},
        {"id": 3, "name": "Bob Johnson", "email": "bob@example.com", "value": 12.4}
    ]
    
    logger.info(f"Extracted {len(data)} records")
    
    # Write to intermediate file
    output_path = Path("data/extracted_data.json")
    output_path.parent.mkdir(exist_ok=True)
    
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)
    
    logger.info(f"Data written to {output_path}")
    return output_path

ujval=============
if __name__ == "__main__":
    try:
        result = extract_data()
        print(f"EXTRACT_SUCCESS: {result}")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Extraction failed: {str(e)}")
        sys.exit(1)
