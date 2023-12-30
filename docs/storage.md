# Storage

The file and storage solution of our High-Performance Computing (HPC) system
is designed to meet the demanding requirements of parallel computing,
large-scale data processing, and high-throughput workloads.
Our robust file and storage infrastructure plays a pivotal role in
supporting the seamless execution of complex computational tasks.

## Beegfs Parallel File System

Our HPC cluster utilizes Beegfs, a high-performance parallel distributed file system, to provide scalable and efficient storage solutions. Beegfs is well-suited for handling large files and concurrent access by multiple compute nodes, making it an ideal choice for the parallel nature of HPC workloads.
Beegfs is designed for high-performance, large-scale workloads,
and is particularly well-suited for applications involving large,
sequential I/O operations.

## Storage Capacity

We offer a substantial storage capacity of 200TB to accommodate the vast amounts of data generated and processed by computational tasks. This enables researchers and scientists to store and analyze extensive datasets without constraints.

| Component         | Specification                 |
| ----------------- | ----------------------------- |
| File System       | Beegfs Parallel File System   |
| Storage Capacity  | ~200TB usable storage         |
| Storage Bandwidth | ~20 GB/s read, ~15 GB/s write |

## User Home Directory

Each user has their own dedicated home directory which can be up to 70 GB in size.
This includes:

- A personal working space with access to files and directories owned by the user.
- Software installed by the user.
- Job submission and job management facilities.

## Project Directory

The project directory is a shared space designed for collaborative projects involving multiple users. It facilitates data sharing, code collaboration, and joint research efforts.

**Capacity**: The project directory quota is determined based on the collective needs of project members. It is often larger than individual user home directory quotas. Each project is eligible to obtain storage space of up to 5 TB.

**Purpose**: It is intended for storing project-specific data, large datasets, code repositories, and any files relevant to the collaborative research project.

**Access Control**: Access to the project directory is granted to all approved project members, allowing collaborative work.

**Backup**: The HPC unit has implemented RAID-5 to safeguard data against potential damage caused by the failure of a single disk. Otherwise, routine backups are intended to protect their project data and ensure its recoverability from the respective project teams.
