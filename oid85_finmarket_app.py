import time
import os
import shutil
import config


def deploy():
    # формируем директории
    if not os.path.exists(config.deploy_path):
        os.makedirs(config.deploy_path)

    if not os.path.exists(os.path.join(config.deploy_path, config.finmarket_app_deploy_directory)):
        os.makedirs(os.path.join(config.deploy_path, config.finmarket_app_deploy_directory))

    current_time = time.time()
    current_deploy_version = f"{current_time}"

    dest_path = os.path.join(config.deploy_path, config.finmarket_app_deploy_directory, current_deploy_version)

    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    # копируем код
    shutil.copytree(config.finmarket_app_source_path, dest_path, dirs_exist_ok=True)

    # запускаем сервер
    cmd = f'cd {dest_path} && npm start'
