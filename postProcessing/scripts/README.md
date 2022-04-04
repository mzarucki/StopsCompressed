Scripts for Job Submission
==========================

Some scripts are provided, that allow controlled submission of jobs similar to
the submit script. The scripts are specific to the nanoaodPostProcessing



mysubmit
--------

The command reads the job definitions from a nanoaodPortProcessing bash script
and runs all commands in a sin=gle slurm task. A ArrayTaskThrottle is set to limit
the parallel execution not to overload the Vienna EOS. 

In addition th command checks the presence of the output ntuple and suppresses jobs
that have already successfully produced the result. Therefore it is necessary to
delete the ntuple, in case a job has to be rerun due to other reasons.

Usage
```bash
./scripts/mysubmit nanoPostProcessing_UL17.sh
```

This ArrayTaskThrottle be set at submission time using the ```--throttle``` option of tne command. During run time
it is possible to increase that value by
```bash
scontrol update ArrayTaskThrottle=20 JobId=...
```
It is recommended to start with low values (10 or 20) and increase the value slowly.
No clear guideline can be given what is the optimal value, as it depends on the
load of EOS

Submission of the job, its jobid and the script name are recorded in ```mysubmit.log```

mystatus
--------

Check the execution of the individual jobs in a task. Slurm DB is read to find the status and the corresponding
CPU and memory consumption. The sample and its splitting is as well shown. For sucecss jobs the output ntuple
is opened and the number of entries are read. In case of failure the path of the log files are shown.

Usage
```bash
./scripts/mystatus jobid
```

mysummary
---------

Check the presence of all results of jobs defined in a set on nanoaodPostProcesing bash scripts.


```
./scripts/mysummary
```