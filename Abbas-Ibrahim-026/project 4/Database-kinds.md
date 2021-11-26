# <y> **The different use cases for different kinds of databases.**

## *What Is Database?**<y>

 Database is an organized collection of structured information, or data, typically stored electronically in a computer system. The data can then be easily accessed, managed, modified, updated, controlled, and organized.

## *What is Database Management System (DBMS)?*

 A database management system (DBMS) is a software package designed to define, manipulate, retrieve and manage data in a database

## **What are the types of databases?**

some of the popular types of database are listed below ;

- Relational databases
  - Microsoft SQL Server, Oracle Database, MySQL, PostgreSQL and IBM Db2

- NoSQL databases
  - Apache Cassandra, MongoDB, CouchDB, and CouchBase

- Cloud databases
  - Microsoft Azure SQL Database, Amazon Relational Database Service, Oracle Autonomous Database.
- Columnar databases
  - Google BigQuery, Cassandra, HBase, MariaDB, Azure SQL Data Warehouse
- Document databases
  - MongoDB, Amazon DocumentDB, Apache CouchDB

With such a rich platter to pick from, the key to finding the perfect match is to have a clear understanding of the use cases and go for the one that best answers the call.

Below is  a selection of  different database use cases and my choice of database in each context.

<style>
h2{
    color:green;
}
</style>

<style>
y{
    color:green;
}
</style>

<style>
t{
    color:red;
}
</style>

### <t>Use Case 1<t>

**A generic IoT platform required support for data from wide range of devices, some of which could not be envisaged while developing the platform.**

*Database used: MongoDB*

The above use case necessitated a data storage mechanism that could handle data from different types of devices. This led to the choice of JSON-based document database, MongoDB. Indexing support of MongoDB makes it easy to pull data using single index or multiple index such as device id with location id. Records for a particular device in different locations are easily accessed. Common parameters like temperature from different types of devices and their records are retrieved fast through these indexes.

### <t>Use Case 2<t>

**Managing infrastructure, IoT sensor collection, and log monitoring and alerting.**

*Database used: InfluxDB, Kdb+, and Prometheus*

 InfluxDB, Kdb+, and Prometheusare designed for dealing with linear data over time, can handle high ingestion rates, have built-in features specifically for dealing with time-based data, a schema optimized for time-series arrays, and batch delete features

### <t>Use Case 3<t>

 **A gift coupon application that handles offers and payment-related information**

 *Database used: MariaDB*

 MariaDB was chose because, a relational database, for its capability to scale horizontally while keeping the ACID property. The last was particularly important because transactional data was being handled. Eventual consistency as offered by other databases was not suitable.

### <t>Use Case 4<t>

 **The application allows users to search for menu items and restaurants in a country.**

*Database used: Elasticsearch and PostgreSQL*

Elasticsearch was used as a secondary database with PostgreSQL as a primary database. There were more than 20 million menu items in the database. Given the enormous volume, a text search on PostgreSQL/MySQL would have been time-consuming and bad in terms of user experience. Waiting too long for search results to show up can annoy and put off users. So a full-text, distributed NoSQL database was used to make the searches faster. Storing the records in Elasticsearch, we could obtain search results in seconds.

### <t>Use Case 5<t>

**Embedded systems, URL shorteners, configuration data, application variables and flags for web applications, state information, and data represented by a dictionary or hash.**

*Database used: MongoDB, Redis, DynamoDB, Cosmos DB*

Key value stores provide fast, low-complexity access to data, are flexible, and can scale quickly and cheaply.

### <t>Use Case 6<t>

  **A solution for storing error logs and traces of applications that are as huge as 100k users.**

*Database used: Azure Table Storage*

Though errors and traces could have different schema, they can be stored in a single Table storage and partitioned by week or month for quick retrieval for debugging purposes. Though Azure Table storage appears very similar to a relational table, the prime advantage of using a table storage when compared to a regular relational table is its ability to support flexible schema, along with its inherent support for storing huge amounts of data as distributed partitions. Adding new columns to Table storage does not require any kind of alter scripts and can be handled by simply altering the type of the object being saved. This makes it an apt solution for storing data such as application logs, chat transcripts, and so on.

### <t>Use Case 7<t>

 **An eCommerce platform with the difference that it had to support regional inventories.**

*Database used: Google Cloud Datastore*

First off, we decided to go with a document store model to align with the data structure. Since the entire environment was in the Google Cloud platform, we weighed the benefits of having a MongoDB in Cloud Platform versus using a DBaaS solution within the platform like Google Cloud Datastore or Cloud Bigtable. Finally, we picked Google Cloud Datastore as it provided SQL-like queries as well as ACID transactions, which were very important for the platform. Since it is a part of Google Cloud platform, we had a friction-free integration with other products we used. The query engine of the data store is also powerful, which allows users to search for data across multiple properties.
