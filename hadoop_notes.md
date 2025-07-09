# 📘 Day 14 – Hadoop Architecture, Ecosystem & HDFS Explained

## 🔷 What is Hadoop?
Hadoop is an open-source framework that allows distributed processing of large data sets across clusters of computers using simple programming models.

---

## 🔷 Core Properties of Hadoop
- **Scalability** – Add more nodes as data grows
- **Fault Tolerance** – Data replicated across nodes
- **Distributed Processing** – Tasks are executed in parallel
- **Cost-Effective** – Commodity hardware
- **Open-Source** – Maintained by Apache

---

## 🔷 Hadoop Ecosystem Overview

| Tool         | Category             | Purpose                                   |
|--------------|----------------------|-------------------------------------------|
| HDFS         | Storage              | Distributed file system                   |
| HBase        | Storage (NoSQL)      | Column-oriented database                  |
| MapReduce    | Processing           | Batch data processing                     |
| Hive         | Processing           | SQL-like querying on HDFS                 |
| Pig          | Processing           | Data flow language for analysis           |
| Spark        | Processing (Fast)    | In-memory computation engine              |
| Sqoop        | Data Integration     | RDBMS to HDFS import/export               |
| Flume        | Data Integration     | Streaming data ingestion into HDFS        |
| Oozie        | Workflow Management  | Schedule and manage Hadoop jobs           |
| ZooKeeper    | Coordination         | Synchronization service for Hadoop jobs   |
| Mahout       | Machine Learning     | Scalable ML libraries over Hadoop         |

---

## 🔷 HDFS (Hadoop Distributed File System)

### Terminology:
- **File System Block** – Default size 128 MB, data split into blocks
- **Cluster Node** – A machine in the Hadoop cluster
- **NameNode** – Master node, stores metadata
- **DataNode** – Stores actual data blocks
- **Replication** – Default replication factor is 3
- **Rack Awareness** – Ensures replicas are placed across racks

### Types of File Systems:
- Local File System
- Distributed File System (HDFS)
- S3-Compatible File Systems (cloud)

---

## 🔷 Hadoop Processes and Daemons

| Daemon      | Function                    |
|-------------|-----------------------------|
| NameNode    | Metadata storage             |
| DataNode    | Data block storage           |
| ResourceManager | Manages cluster resources |
| NodeManager | Executes tasks on nodes      |

---

## 🧱 Hadoop Architecture Flow

1. Input data is split into **blocks**.
2. **NameNode** manages metadata.
3. **DataNodes** store blocks.
4. **MapReduce** processes data in a distributed way.
5. Results are stored back in HDFS.

---


