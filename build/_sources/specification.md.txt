# Specifications

## Hardware

| Component         | Specification                                                   |
| ----------------- | --------------------------------------------------------------- |
| **Compute Nodes** |                                                                 |
| Processor         | 4 x AMD Epyc 64-core CPU in each node                           |
| Memory            | 256 GB DDR4 RAM in each node (1 TB total)                       |
| Storage           | 16 TB SSD for in each node, 175 TB for storage                  |
| Networking        | 10Gigabit Ethernet per compute node                             |
| OS                | Ubuntu Server LTS 22 with Kernel 5.4+ 0                         |
| **GPU Nodes**     |                                                                 |
| -                 | Currently unavailable, with plans to incorporate in the future. |

The front-end of our HPC cluster looks as-
![HPC-front](images/hpc-front.png)

.. autosummary::
:toctree: generated
