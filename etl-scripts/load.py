#!/usr/bin/env python3
"""
Load stage - Loads data to destination
"""
import json
import logging
import sys
from pathlib import Path
from datetime import datetime   # 🔹 FIXED

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def load_data():
    """Load transformed data to destination"""
    logger.info("Starting data loading")
    
    # Read transformed data
    input_path = Path("data/transformed_data.json")
    if not input_path.exists():
        raise FileNotFoundError(f"Transformed data not found at {input_path}")
    
    with open(input_path, 'r') as f:
        data = json.load(f)
    
    logger.info(f"Loading {len(data)} records")
    
    # Simulate loading to a database or other destination
    output_path = Path("output/final_data.json")
    output_path.parent.mkdir(exist_ok=True)
    
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)
    
    # Generate a summary report
    summary = {
        "total_records": len(data),
        "active_records": sum(1 for record in data if record.get("status") == "active"),
        "inactive_records": sum(1 for record in data if record.get("status") == "inactive"),
        "completion_time": datetime.now().isoformat()
    }
    
    summary_path = Path("output/load_summary.json")
    with open(summary_path, 'w') as f:
        json.dump(summary, f, indent=2)
    
    logger.info(f"Data loaded successfully to {output_path}")
    logger.info(f"Summary report generated at {summary_path}")
    # prin("cjlsdnjvn");
    return output_path, summary_path

if __name__ == "__main__":
    try:
        result, summary = load_data()
        print(f"LOAD_SUCCESS: {result}")
        print(f"SUMMARY: {summary}")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Loading failed: {str(e)}")
        sys.exit(1)
