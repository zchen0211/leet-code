# ssh Setup

## Setup Remote Connection
- Create a pair of keys (public, private)
```
ssh-keygen
```
to generate a pair of xx_id_rsa and xx_id_rsa.pub
- Save private at local client, and copy the public at remote server
```
ssh-copy-id xxx.pub user@remote
```
will copy to the authorized_keys file on the server side.
- Page local client side in .ssh/config:
```
Host devfair
     User zhuoyuan
     Hostname 100.97.67.4
     Port 22
     ProxyJump prn-fairjmp03

Host *
    AddKeysToAgent yes
    UseKeychain yes
    IdentityFile ~/.ssh/fb_id_rsa
```