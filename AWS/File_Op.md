# File Operation on AWS

## Setup
```
module load fairusers_aws
```

## Basic Usage
- Backup
```
fs3 backup /path/to/your/backup
```
- List backups
```
fs3 ls /path/of/your/backup
```
- Restore a file or a directory
```
fs3 restorefile /path/to/your/file
fs3 restoredir /path/to/your/dir/
```
- Delete a file or a directory
```
fs3 purge /path/to/your/file
fs3 purge -r /path/to/your/dir/
```

## Directory
- Personal (each user, replace user_name with your name): s3://fairusersglobal/users/user_name/

## Sync
- One-by-one sync (Slower)
```
fs3cmd put /local/file s3://dl.fbaipublicfiles.com/minecraft2dvision/
```
- Low-level sync (faster)
```
fs3cmd sync -p /local/folder s3://dl.fbaipublicfiles.com/minecraft2dvision/
```
Then your folder will be available at https://dl.fbaipublicfiles.com/minecraft2dvision/
- Low-level delete
```
fs3cmd del s3://fairusersglobal/users/maj/h1/checkpoint/maj/unneeded.txt
```