#!/usr/bin/env python3
"""
Transform stage - Processes and transforms data
"""
import json
import logging
import sys
from pathlib import Path

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def transform_data():
    """Transform extracted data"""
    logger.info("Starting data transformation")
    
    # Read extracted data
    input_path = Path("data/extracted_data.json")
    if not input_path.exists():
        raise FileNotFoundError(f"Extracted data not found at {input_path}")
    
    with open(input_path, 'r') as f:
        data = json.load(f)
    
    logger.info(f"Transforming {len(data)} records")
    
    # Apply transformations
    transformed_data = []
    for record in data:
        # Add a new field
        record["status"] = "active" if record["value"] > 20 else "inactive"
        
        # Format name to uppercase
        record["name"] = record["name"].upper()
        
        # Add a processed timestamp
        from datetime import datetime
        record["processed_at"] = datetime.now().isoformat()
        
        transformed_data.append(record)
    
    # Write transformed data
    output_path = Path("data/transformed_data.json")
    with open(output_path, 'w') as f:
        json.dump(transformed_data, f, indent=2)
    
    logger.info(f"Transformed data written to {output_path}")
    return output_path

if __name__ == "__main__":
    try:
        result = transform_data()
        print(f"TRANSFORM_SUCCESS: {result}")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Transformation failed: {str(e)}")
        sys.exit(1)