# 📘 Day 16 – Hadoop High Availability & HDFS Write Path

## 🔷 Secondary NameNode
- NOT a backup for NameNode
- Periodically pulls fsimage and edits files
- Merges them to create updated fsimage
- Helps in reducing NameNode restart time

## 🔷 Standby NameNode
- Passive node that stays in sync with active NameNode
- Part of Hadoop High Availability (HA) configuration
- Uses shared storage (e.g., NFS) and fencing to avoid split-brain
- Takes over automatically on failure of active NameNode

## 🔷 Hadoop High Availability (HA) Architecture
- Active/Standby NameNode pair
- JournalNode quorum for shared edit logs
- Zookeeper for failover coordination
- Ensures 0 downtime in critical environments

## 🔷 HDFS Write Request Flow (Simplified)
1. Client contacts NameNode to get block locations
2. NameNode responds with available DataNodes
3. Client writes data → pipeline formed across DataNodes
4. Acknowledgments returned from each DataNode
5. NameNode updates block metadata

> Each block replicated (default: 3 times) across different racks
