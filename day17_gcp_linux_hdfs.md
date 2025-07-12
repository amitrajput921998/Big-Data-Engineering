# 🌐 Day 17 – GCP Hadoop Cluster, Linux & HDFS Command Practice

## ✅ GCP Cluster Creation
- Created VMs using Compute Engine
- SSH access setup & Hadoop installation
- Configured cluster nodes (NameNode, DataNode)
- Configured security rules (firewall ports: 50070, 9000)

## ✅ Exploring the Cluster
- Verified Hadoop processes and UI dashboards
- Navigated between cluster machines using SSH
- Checked log files and configuration files

## ✅ GCP Best Practices (Quick Notes)
- Always restrict firewall access
- Use startup scripts for automation
- Monitor disk usage and region zones
- Use metadata tags to organize resources

---

## ✅ Linux Commands Practice
- File navigation: `ls`, `cd`, `pwd`, `cat`, `more`
- File manipulation: `cp`, `mv`, `rm`, `touch`, `nano`, `chmod`
- System info: `top`, `ps`, `df -h`, `free -m`
- Directory ops: `mkdir`, `rmdir`, `tree`
- User & permissions: `chmod`, `chown`, `su`, `sudo`

---

## ✅ HDFS Commands Practiced
- File operations:
  - `hdfs fs -ls /`
  - `hdfs fs -mkdir /data`
  - `hdfs fs -put localfile.txt /data`
  - `hdfs fs -cat /data/localfile.txt`
  - `hdfs fs -rm /data/localfile.txt`
- Permissions and block checking:
  - `hdfs fs -chmod 755 /data`
  - `hdfs fsck /data -files -blocks -locations`


