# `sbatch` Cheat Sheet

## Basic `sbatch` structure

\#\!/bin/bash  
\#SBATCH \--job-name=my\_workflow  
\#SBATCH \--output=logs/my\_workflow\_%j.out  
\#SBATCH \--error=logs/my\_workflow\_%j.err  
\#SBATCH \--partition=cpu  
\#SBATCH \--cpus-per-task=4  
\#SBATCH \--mem=16G  
\#SBATCH \--time=02:00:00

set \-euo pipefail  
cd /path/to/project  
module purge  
module load python3/3.12.9  
source venv/bin/activate  
python scripts/run\_workflow.py  
sbatch \--begin=02:00 scripts/orchestration/daily\_cycle.sbatch

---

## Beginner planning checklist

Before writing the script, define:

- [ ] **Workflow title**  
- [ ] **Main script to run**  
- [ ] **Inputs**  
- [ ] **Outputs**  
- [ ] **CPU or GPU?**  
- [ ] **Modules / environment to load**  
- [ ] **How much time might it need?**  
- [ ] **What should go to the log file?**  
- [ ] **One likely failure point:**

## 

## 

## What the critical parts mean

### Job name

\#SBATCH \--job-name=my\_workflow

A short name so you can recognize the job.

### Log files

\#SBATCH \--output=logs/my\_workflow\_%j.out

\#SBATCH \--error=logs/my\_workflow\_%j.err

Saves normal output and errors for later review.

### Resources

\#SBATCH \--partition=cpu  
\#SBATCH \--cpus-per-task=4  
\#SBATCH \--mem=16G  
\#SBATCH \--time=02:00:00

Tells Slurm what the job needs:

- CPU or GPU  
- number of CPUs  
- memory  
- maximum run time

### Safer shell behavior

set \-euo pipefail

Helps the script stop when something important goes wrong.

### Environment setup

module purge

module load python3/3.12.9

source venv/bin/activate

Loads the right software and environment.

### Main workflow step

python scripts/run\_workflow.py

Runs the script you want Slurm to execute.

### **Example to test:**

1. ### **`In Jupyter Create hello_job.sbatch`**

   \#\!/bin/bash  
   \#SBATCH \--job-name=hello\_demo  
   \#SBATCH \--output=logs/hello\_%j.out  
   \#SBATCH \--error=logs/hello\_%j.err  
   \#SBATCH \--partition=cpu  
   \#SBATCH \--cpus-per-task=1  
   \#SBATCH \--mem=1G  
   \#SBATCH \--time=00:05:00  
     
   set \-euo pipefail  
     
   mkdir \-p logs  
   cd /path/to/project  
     
   module purge  
   module load python3/3.12.9  
     
   python hello.py

2. ### **`In Jupyter Create hello.py`**

   from datetime import datetime  
   import socket  
     
   print("Hello from a batch job.")  
   print("Time:", datetime.now())  
   print("Node:", socket.gethostname())  
   

3. ### **From a Jupyter terminal:**

   sbatch hello\_job.sbatch  
   squeue \-u $USER

4. ### Then open the log file in `logs/`

