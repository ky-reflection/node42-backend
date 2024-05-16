#!/bin/bash
set +e
# 停止 uWSGI 服务
echo "Stopping uWSGI..."
uwsgi --stop /home/ky/node42-backend/uwsgi/uwsgi.pid|| true


# 运行 Django 数据库迁移
echo "Running Django migrations..."
if python3 manage.py makemigrations && python3 manage.py migrate; then
    echo "Django migrations applied successfully."
else
    echo "Failed to apply Django migrations. Please check the migration logs for more details."
    exit 1
fi

# 收集静态文件
echo "Collecting static files..."
if python3 manage.py collectstatic --noinput; then
    echo "Static files collected successfully."
else
    echo "Failed to collect static files. Please check the collectstatic logs for more details."
    exit 1
fi

# 启动 uWSGI 服务
echo "Starting uWSGI..."
if uwsgi --ini uwsgi.ini; then
    echo "uWSGI started successfully."
else
    echo "Failed to start uWSGI. Please check the uWSGI logs for more details."
    exit 1
fi

echo "Deployment script completed."
