from google.cloud import bigquery

def copy_schema_with_filter(source_project, source_dataset, target_project, target_dataset, tables_to_replicate):
    client = bigquery.Client()

    source_dataset_ref = client.dataset(source_dataset, project=source_project)
    tables = client.list_tables(source_dataset_ref)

    for table in tables:
        if table.table_id not in tables_to_replicate:
            continue

        source_table_ref = source_dataset_ref.table(table.table_id)
        source_table = client.get_table(source_table_ref)

        target_table_ref = bigquery.TableReference(
            bigquery.DatasetReference(target_project, target_dataset),
            table.table_id
        )

        target_table = bigquery.Table(target_table_ref, schema=source_table.schema)
        client.create_table(target_table)
        print(f"Copied schema for table {table.table_id} to {target_dataset}")

# Replace these variables with your project and dataset names
SOURCE_PROJECT = 'tfmv-371720'
SOURCE_DATASET = 'tpch'
TARGET_PROJECT = 'tfmv-371720'
TARGET_DATASET = 'tpch_copy'

# List of table names to replicate
TABLES_TO_REPLICATE = ['customer', 'lineitem', 'nation', 'orders', 'part', 'partsupp', 'region', 'supplier']

copy_schema_with_filter(SOURCE_PROJECT, SOURCE_DATASET, TARGET_PROJECT, TARGET_DATASET, TABLES_TO_REPLICATE)
