# ACID Transactions

Four properties that make a transaction reliable
- Atomicity = all operations either complete fully or not at all
- Consistency = transaction leaves the storage system in a consistent state by following rules and constraints
- Isolation = concurrent transactions do not interfere with each other
- Durability = changes are saved instantly and remain saved even if the system crashes

`Transaction = operations completed as single unit of work`

# Data Pipeline

ETL = Extract Transform Load
- Extract data from source (e.g. CRM, transactions, engagement, documentation)
- Transform data into suitable format (organise into structure)
- Load into database (INSERT INTO)

## Relational Data Processing

OLTP = Online Transaction Processing
- Transaction = any change to database
- Requires high degree of normalisation
- Heavy write, low read

OLAP = Online Analytic Processing
- Extract business intelligence from OLTP
- Adds layer of abstraction and aggregation
- Heavy read, low write

# Data Warehouses

Designed for data analysis
-  Database = OLTP
-  Data warehouse = OLAP
- Aggregate data from a variety of sources
- Only store data that answers business questions

`Data mart = subset of data warehouse for specific business unit`

## Inmon Architecture

Top-down approach
1. Create data warehouse
2. Distribute into data marts

## Kimball Architecture

Bottom-up approach
1. Create data marts separately
2. Combine into data warehouse

## Dimensional Modelling

- Fact tables = events
    - Data corresponding to specific business processes with numeric measurable data
- Dimension tables = people/items/objects
    - Data corresponding to instances of objects with textual dimension data
- Star schema = one or more fact tables joint with dimension tables
- Snowflake schema = star schema with dimension tables more normalised

# Data Lakes

Store unstructured data in original form
- Data is only processed when analysis is needed
- ELT (no need to transform data before loading because it is unstructured)
- ELTL (transform and load into database or data warehouse for analysis)

# Data Lakehouses

Combine best aspects of data warehouses and data lakes
- Data warehouse built on top of a data lake (can be decoupled)
- Some structure and control but still flexible and scalable