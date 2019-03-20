# Buffer Management System

> Implement a model of how buffer cache works in a system,
and show how the kernel and other processes interact to
get the desired effect.

## Modules

+ **Implementation data**  
&nbsp;&nbsp;&nbsp;
Stores the specification details set by the superuser.

+ **Buffer**  
&nbsp;&nbsp;&nbsp;
Implements the structure of a buffer(including buffer header).

+ **Buffer cache**  
&nbsp;&nbsp;&nbsp;
Implements the buffer cache(including the free list header)

+ **Kernel**  
&nbsp;&nbsp;&nbsp;
Implements the kernel that interacts with the buffer cache
and various processes to service their needs.

+ **Process**  
&nbsp;&nbsp;&nbsp;
Implements a process that requests a disk block or a free buffer.

+ **Runner**  
&nbsp;&nbsp;&nbsp;
Implements a runner process that spawns new processes and
displays the data logs produced by the kernel and the processes.



