#!/usr/bin/env bash

#password=$(cat /var/log/mysql/error.log | grep "A temporary password is generated for" | tail -1 | sed -n 's/.*root@localhost: //p')
#MYPASSWD=$password
#mysql -uroot -p$password -Bse "ALTER USER 'root'@'localhost' IDENTIFIED BY '$MYPASSWD';"

#MYPASSWD=$RANDOM$RANDOM$RANDOM

#mysqladmin -u root password $MYPASSWD;

mysql -uroot -p$MYSQL_ROOT_PASSWORD -e "CREATE DATABASE IF NOT EXISTS vkparser DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;"


echo "Done"