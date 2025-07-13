# 📘 Day 18 – MapReduce & Distributed Processing Introduction

## 🔷 What is MapReduce?
MapReduce is a programming model used to process large data sets with a distributed algorithm on a cluster.

- **Map Function**: Takes input and emits intermediate key-value pairs
- **Reduce Function**: Aggregates intermediate data and produces output

## 🔷 Why Use MapReduce?
- Handles large volumes of data by distributing processing
- Scalable across clusters
- Fault tolerant
- Part of core Hadoop processing engine

---

## 🔷 MapReduce Workflow
1. **Input Split** – Data is divided into splits
2. **Map Phase** – Each split is processed into key-value pairs
3. **Shuffle & Sort** – Grouped by key across nodes
4. **Reduce Phase** – Aggregates results
5. **Final Output** – Stored back in HDFS

---

## 🔷 Cluster Interaction
- Mappers run in parallel across nodes
- Data movement handled automatically via HDFS
- Resource management by YARN or JobTracker (older)
