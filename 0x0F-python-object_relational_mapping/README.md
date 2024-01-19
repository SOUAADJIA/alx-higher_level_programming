# 0x0F. Python - Object-relational mapping

## Overview

This project focuses on Object-Relational Mapping (ORM) in Python, utilizing the MySQLdb module for direct SQL interaction and SQLAlchemy as an ORM tool. The aim is to seamlessly connect Python with MySQL databases, eliminating the need for extensive SQL queries. The project emphasizes the power of ORM by abstracting storage details, enabling developers to work primarily with Python code and allowing flexibility in changing storage without rewriting the entire project.

## Project Details

- **Project Title:** 0x0F. Python - Object-relational mapping
- **By:** Guillaume
- **Weight:** 1
- **Project Deadline:** Jan 20, 2024, 4:00 AM
- **Auto Review:** Will be launched at the deadline
- **Auto QA Review:**

## Prerequisites

Before starting, ensure that your MySQL server is version 8.0. Refer to [How to install MySQL 8.0 in Ubuntu 20.04](<MySQL Installation Guide Link>).

## Background Context

The project connects the realms of Databases and Python, bridging the gap through two main components:

1. **MySQLdb:** Utilized in the initial part to connect to a MySQL database and execute SQL queries.

2. **SQLAlchemy:** An Object-Relational Mapper (ORM) used in the second part, eliminating the need for direct SQL queries. The focus shifts from "How is this object stored?" to "What can I do with my objects?". This facilitates Python code usage without SQL queries, making the code storage-type independent.

## Code Examples

### Without ORM:

```python
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")  # SQL knowledge required to fetch states
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```
### With an ORM:

```python
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
``` 
Do you see the difference? Cool, right?

The biggest difficulty with ORM is: The syntax!

Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don’t read the entire documentation before starting, just jump on it if you don’t get something.
