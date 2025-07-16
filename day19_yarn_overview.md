# 📘 Day 19 – YARN (Yet Another Resource Negotiator)

## 🔷 What is YARN?
YARN is the **resource management layer** in Hadoop responsible for allocating system resources and managing distributed job execution.

## 🔷 Key Components of YARN

| Component         | Role                                                                 |
|------------------|----------------------------------------------------------------------|
| ResourceManager   | Central authority for resource allocation across the cluster         |
| NodeManager       | Runs on every DataNode, monitors resources, and reports to RM        |
| ApplicationMaster | Manages lifecycle of a single application                            |
| Containers        | Execution environment for tasks (launched by NodeManager)            |

---

## 🔷 Real-world Analogy:
Imagine a university:
- **ResourceManager** = Dean of Academics (allocates classrooms)
- **NodeManagers** = Department Heads (track class usage per department)
- **ApplicationMaster** = Teacher (executes and monitors a class)
- **Containers** = Classrooms where teaching happens

---

## 🔷 YARN Job Lifecycle (Step-by-Step)

1. Client submits job
2. ResourceManager assigns NodeManager and launches ApplicationMaster
3. ApplicationMaster negotiates containers for tasks
4. NodeManager launches containers
5. ApplicationMaster monitors progress and reports to ResourceManager
6. On completion, containers are released
