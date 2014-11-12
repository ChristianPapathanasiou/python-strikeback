# Python Strikeback Module #

## Usage: ##
1. Ensure you have the following packages on Debian/Ubuntu:
	* python-pam 
	* libpam-python
	* python-libssh2

2. Put the module in `/lib/security/striker.py`

3. Configure PAM for SSHD to use the module

/etc/pam.d/sshd
`
auth       required     pam_python.so striker.py
`

/etc/ssh/sshd_config

`
UsePAM yes

`


## Notes: ##
* I don't use SSH on the box this is on, further configuration of /etc/pam.d/sshd would be required to actually use SSH properly
