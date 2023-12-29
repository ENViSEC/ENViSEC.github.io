# Getting Started Guide:

Before you begin, make sure you have the following:

- Access to an HPC cluster with Slurm installed.
- Basic knowledge of Linux command-line operations.

## Slurm scheduler:

Simple Linux Utility for Resource Management (SLURM) is commonly used for job scheduling and resource management on high-performance computing (HPC) clusters. Slurm operates on the concept of jobs, nodes, and partitions. Familiarize yourself with these key terms:

- **Job**: A computational task submitted to the cluster.
- **Node**: A computing resource that performs tasks as part of a job.
- **Partition**: A logical division of the cluster resources.

## Connecting to the HPC Cluster

Use SSH to connect to the HPC cluster:

```
ssh <username>@hpc-cluster.example.com
```

Replace `username` with your username and hpc-cluster.example.com with the actual address of your HPC cluster.

## Submitting a Job

To submit a job using the `sbatch` command followed by the script file, run the command as-

```
sbatch script.sh
```

where `script.sh` is the name of your shell script. The script should include the commands necessary for running your analysis or simulation.

The output will provide a unique job ID (e.g., 12345678). You can view more information about
your job using the `squeue` command::

## Example of slurm script:

```
#!/bin/bash
#SBATCH --job-name=my_mpi_job          # Job name
#SBATCH --partition=LocalQ             # Partition to submit to
#SBATCH --output=output.%j             # Output file name (%j expands to jobID)
#SBATCH --error=error.%j               # Error file name (%j expands to jobID)
#SBATCH --ntasks=4                     # Number of tasks (MPI processes)
#SBATCH --nodes=1                      # Number of nodes
#SBATCH --ntasks-per-node=4            # Number of tasks per node
#SBATCH --time=00:10:00                # Walltime (hh:mm:ss)

# Load available modules if you require any
module load <module-name>

# Run your program here
python3 test.py
```

This is a basic example, and you may need to customize it according to your specific needs, such as adjusting resource requirements, module loading, and paths.
You can specify the following parameters in your slurm script.

**--job-name=<name>**: Specifies a name for the job. This name will be used in identifying the job in the queue and in the output and error files.

**--output=<filename>**: Specifies the name of the file where the standard output of the job will be written. You can use `%j` in the filename, and SLURM will replace it with the job ID.

**--error=<filename>**: Specifies the name of the file where the standard error of the job will be written. Like `--output`, `%j` can be used in the filename.

**--partition=<partition_name>**: Specifies the name of the partition or queue to which the job should be submitted. Partitions are used to group nodes with similar characteristics.

**--ntasks=<number>**: Specifies the total number of tasks (or processes) to be run. This is often used in parallel computing with MPI.

**--nodes=<number>**: Specifies the number of nodes requested for the job. If not specified, SLURM may allocate the tasks across nodes as needed.

**--ntasks-per-node=<number>**: Specifies the number of tasks (or processes) to be run per node.

**--cpus-per-task=<number>**: Specifies the number of CPU cores to allocate per task. This can be used to control the number of threads per task.

**--time=<time>**: Specifies the maximum wall-clock time for the job to run. The format is `days-hours:minutes:seconds`.

**--mem=<memory>**: Specifies the total memory required for the job. The format is in megabytes (M), gigabytes (G), etc.

**--mail-type=<type>**: Specifies the type of email notifications to receive. Types include `BEGIN`, `END`, `FAIL`, and `ALL`.

**--mail-user=<email_address>**: Specifies the email address to which notifications will be sent.

**--dependency=<type:jobid>**: Specifies a job dependency, meaning the current job will not start until the specified job (identified by job ID) completes successfully.

## Basic slurm commands

You can check the status of all jobs with the following command:

```
squeue -u <username>
```

Replace `username` with your username. You can also view the status of your job using the `sacct` command::

```
sacct -j 12345678
```

Replace 12345678 with your job ID. Once your job is complete, you will receive an email notification. You can also check the output of your job in the `slurm-12345678.out` file. Replace 12345678 with your job ID.

You can interact with a running job using the `srun` command::

```
srun --jobid 12345678 --pty bash
```

Replace 12345678 with your job ID. This will open a new terminal session on the node where your job is running.
You can use this terminal session to run commands on the node. To exit the terminal session, type `exit`.
You can also use the `scancel` command to cancel a running job::

```
scancel 12345678
```

Replace 12345678 with your job ID. This will cancel your job and terminate all processes associated with it.
You can also use the `scontrol` command to view more information about your job::

```
scontrol show job 12345678
```

Replace 12345678 with your job ID. This will display detailed information about your job.
You can also use the `sinfo` command to view information about the nodes on the cluster::

```
sinfo
```

This will display information about the nodes on the cluster, including the number of nodes, the number of CPUs per node, and the number of GPUs per node.
You can also use the `smap` command to view information about the memory usage on the cluster::

```
smap
```

This will display information about the memory usage on the cluster, including the total memory, the memory used, and the memory available.
You can also use the `sview` command to view information about the cluster::

```
sview
```

This will display a graphical view of the cluster, including the nodes, the partitions, and the jobs running on the cluster.
You can also use the `scontrol` command to view information about the partitions on the cluster::

```
scontrol show partition
```

This will display information about the partitions on the cluster, including the number of nodes, the number of CPUs per node, and the number of GPUs per node.
You can also use the `scontrol` command to view information about the jobs running on the cluster::

```
scontrol show job
```

This will display information about the jobs running on the cluster, including the job ID, the job name, the job status, and the job owner.
You can also use the `scontrol` command to view information about the nodes on the cluster::

```
scontrol show node
```

This will display information about the nodes on the cluster, including the node name, the node status, and the node owner.
You can also use the `scontrol` command to view information about the users on the cluster::

```
scontrol show user
```

This will display information about the users on the cluster, including the user name, the user status, and the user owner.
You can also use the `scontrol` command to view information about the partitions on the cluster::

```
scontrol show partition
```

This will display information about the partitions on the cluster, including the partition name, the partition status, and the partition owner.
You can also use the `scontrol` command to view information about the jobs running on the cluster::

## For additional tutorials:

- To gain in-depth knowledge on utilizing an HPC cluster in conjunction with the SLURM scheduler, consider following the introductory carpentry training tutorials. This tutorial provides comprehensive guidance on effectively navigating and leveraging the capabilities of an HPC environment, particularly focusing on the SLURM job scheduler, Link: [Introduction to High-Performance Computing](https://carpentries-incubator.github.io/hpc-intro/).

  .. autosummary::
  :toctree: generated
