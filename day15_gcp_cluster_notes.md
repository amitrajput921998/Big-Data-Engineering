# 🌐 Day 15 – Google Cloud Setup & DataNode Failure Handling

## ✅ GCP Setup Steps
- Created Google Cloud account
- Enabled Compute Engine API
- Launched VM instances as part of cluster setup
- Installed basic tools (SSH, Hadoop configs)

## ✅ Cluster Overview
- Nodes created within a region/zone
- Custom firewall rule setup
- SSH access & node monitoring enabled

## ✅ DataNode Failure: Temporary vs Permanent

| Failure Type      | Behavior                                           |
|-------------------|----------------------------------------------------|
| Temporary Failure | Node goes offline briefly (e.g., reboot/network)   |
| Permanent Failure | Hardware loss, disk corruption, or manual removal  |

### How HDFS Handles Failures:
- **Heartbeat mechanism** from DataNodes to NameNode
- If no heartbeat for X mins → marked dead
- Blocks replicated to healthy nodes automatically
- Admin can decommission nodes or re-add them

---
