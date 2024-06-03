# BigQuery Schema Copier

This Python script copies the schema of tables from a specified BigQuery dataset to another specified BigQuery dataset without copying the data.

## Prerequisites

- Python 3.7 or higher
- Google Cloud SDK installed and configured
- Google Cloud BigQuery API enabled for your project
- Service account with appropriate permissions to access BigQuery datasets

## Installation

### Clone the repository

```bash
git clone https://github.com/TFMV/BQCopySchema.git
cd BQCopySchema
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Configuration

Be sure to edit the source/target projects and datasets in the script.

## Usage

Before running the script, make sure you have set up authentication for your Google Cloud project. You can do this by setting the GOOGLE_APPLICATION_CREDENTIALS environment variable to the path of your service account key file:

```bash
python main.py
```

## Example Output

(BQCopySchema) ☁  BQCopySchema [feature/v1] ⚡  python main.py

- Copied schema for table customer to tpch_copy
- Copied schema for table lineitem to tpch_copy
- Copied schema for table nation to tpch_copy
- Copied schema for table orders to tpch_copy
- Copied schema for table part to tpch_copy
- Copied schema for table partsupp to tpch_copy
- Copied schema for table region to tpch_copy
- Copied schema for table supplier to tpch_copy
