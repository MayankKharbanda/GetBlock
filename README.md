# Buffer Management System

> Implement a model of how buffer cache works in a system,
and show how the kernel and other processes interact to
get the desired effect.

## Modules

+ **Config**  
&nbsp;&nbsp;&nbsp;
Stores the specification details set by the superuser.

+ **buffer_header**  
&nbsp;&nbsp;&nbsp;
Implements the structure of a buffer(including buffer header).

+ **hash_queue**  
&nbsp;&nbsp;&nbsp;
Implements the Hash Queue frame.

+ **free_queue**  
&nbsp;&nbsp;&nbsp;
Implements the Free Queue frame.

+ **buffer_cache**  
&nbsp;&nbsp;&nbsp;
Implements the buffer cache(including the free list header).

+ **get_block**  
&nbsp;&nbsp;&nbsp;
Implements the function to allocate a buffer for a disk block.

+ **Kernel**  
&nbsp;&nbsp;&nbsp;
Implements the kernel that interacts with the buffer cache
and various processes to service their needs.

+ **async_write**  
&nbsp;&nbsp;&nbsp;
Implements the function to handle asynchronous write to the disk. 

+ **brelease**  
&nbsp;&nbsp;&nbsp;
Implements the function to de-allocate a disk block from a buffer.

+ **request**  
&nbsp;&nbsp;&nbsp;
Contains the classes to handle threading queues.

## Module details

### BufferHeader

BufferHeader is essentially the entire Buffer, but because
of the existing *buffer* library in python we had to name it
*BufferHeader*.

| Variable | Type | Definition |
| :---: | :---: | --- | 
| block_number    | Number         |Block Number whose data is in the buffer|
| process_id      | Number         |Process ID of the process using the buffer|
| status          | String         |Status of the buffer which is a combination of the various status states defined below|
| data            | String         |Data of the Block stored in the buffer|
| next_hash_queue | BufferHeader   |Next buffer in the Hash Queue|
| prev_hash_queue | BufferHeader   |Previous buffer in the Hash Queue|
| next_free_list  | BufferHeader   |Next buffer in the Free List| 
| prev_free_list  | BufferHeader   |Previous buffer in the Free List|
| lock            | Threading Lock |Lock the buffer|

| Method | Definition |
| :---: | --- |
|get_status   |Returns the status of the buffer|
|set_status   |Sets the status of the buffer(keeping in mind that buffer status is a combination of the status states)|
|remove_status|Removes the status of the buffer|
  
&nbsp;&nbsp;
<hr>
&nbsp;&nbsp;

### Status of a buffer

These status states are defined in the Config file.

| State Symbol (String) | State Meaning |
| :---: | --- |
|0|Buffer is Busy(Locked)|
|1|Buffer is Free(Unlocked)|
|2|Buffer contains Valid data|
|3|Buffer has been marked delayed write|
|4|Some Process is reading or writing data from or to the disk|
|5|Some Process is waiting for the buffer to become free|
|6|Buffer is Old (already in free list)|
|7|Buffer is not Old (just entered in free list)|

&nbsp;&nbsp;
<hr>
&nbsp;&nbsp;

### HashQueue

| Variable | Type | Definition |
| :---: | :---: | --- | 
| head  | BufferHeader | Buffer at the start of the hash queue|
| tail  | BufferHeader | Buffer at the end of the hash queue|


| Method | Definition |
| :---: | --- |
| add | add the buffer to this particular hash queue|
| remove | remove the buffer from this particular hash queue|

&nbsp;&nbsp;
<hr>
&nbsp;&nbsp;

### FreeQueue

| Variable | Type | Definition |
| :---: | :---: | --- | 
| head  | BufferHeader | Buffer at the start of the free queue|
| tail  | BufferHeader | Buffer at the end of the free queue|


| Method | Definition |
| :---: | --- |
| add_to_tail | add the buffer to the tail of the free queue|
| add_to_head | add the buffer to the head of the free queue|
| is_empty | returns true if free list is empty|
| remove | remove the buffer from the free queue|
| remove_from_head | remove the buffer from the head of free queue|

&nbsp;&nbsp;
<hr>
&nbsp;&nbsp;

### BufferCache

| Variable | Type | Definition |
| :---: | :---: | --- | 
| free_list | FreeQueue | Free List(initially containing all the buffers)|
| hash_queue_headers | List of HashQueue | Hash Queues (all of them initially empty)|

| Method | Definition |
| :---: | --- |
|in_hash_queue| Returns True if block is in the corresponding HashQueue|
|assign_block | Returns the BufferHeader that contains the block (this function can only be called if in_hash_queue returns true)|

&nbsp;&nbsp;
<hr>
&nbsp;&nbsp;

### get_block

This function implements the system call *getblk*

&nbsp;&nbsp;
<hr>
&nbsp;&nbsp;


