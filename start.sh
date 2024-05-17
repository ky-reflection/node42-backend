#!/bin/bash

# 设置日志文件路径
UWSGI_LOG="/home/ky/node42-backend/uwsgi/uwsgi.log"
UWSGI_PID="/home/ky/node42-backend/uwsgi/uwsgi.pid"

# 停止 uWSGI 服务
echo "Stopping uWSGI..."
if [ -f $UWSGI_PID ]; then
    uwsgi --stop $UWSGI_PID
    STOP_STATUS=$?
    if [ $STOP_STATUS -eq 0 ]; then
        echo "uWSGI stopped successfully."
    else
        echo "Failed to stop uWSGI. Exit status: $STOP_STATUS"
        # echo "Check uWSGI log for more details: $UWSGI_LOG"
        # cat $UWSGI_LOG
        # exit 1
    fi
else
    echo "uWSGI PID file not found. It might be already stopped."
fi

# 运行 Django 数据库迁移
echo "Running Django migrations..."
python3 manage.py makemigrations
MAKEMIGRATIONS_STATUS=$?
python3 manage.py migrate
MIGRATE_STATUS=$?

if [ $MAKEMIGRATIONS_STATUS -eq 0 ] && [ $MIGRATE_STATUS -eq 0 ]; then
    echo "Django migrations applied successfully."
else
    echo "Failed to apply Django migrations. makemigrations status: $MAKEMIGRATIONS_STATUS, migrate status: $MIGRATE_STATUS"
    exit 1
fi

# 收集静态文件
echo "Collecting static files..."
python3 manage.py collectstatic --noinput
COLLECTSTATIC_STATUS=$?

if [ $COLLECTSTATIC_STATUS -eq 0 ]; then
    echo "Static files collected successfully."
else
    echo "Failed to collect static files. Exit status: $COLLECTSTATIC_STATUS"
    exit 1
fi

# 启动 uWSGI 服务
echo "Starting uWSGI..."
uwsgi --ini uwsgi.ini &
START_STATUS=$?

if [ $START_STATUS -eq 0 ]; then
    echo "uWSGI started successfully."
else
    echo "Failed to start uWSGI. Exit status: $START_STATUS"
    echo "Check uWSGI log for more details: $UWSGI_LOG"
    cat $UWSGI_LOG
    exit 1
fi

echo "Deployment script completed."
