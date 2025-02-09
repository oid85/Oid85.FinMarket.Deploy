import os
import shutil
import config


def deploy():
    # формируем директориЮ
    if not os.path.exists(config.deploy_path):
        os.makedirs(config.deploy_path)

    # удаляем папку
    if os.path.exists(os.path.join(config.deploy_path, config.finmarket_store_deploy_directory)):
        shutil.rmtree(os.path.join(config.deploy_path, config.finmarket_store_deploy_directory))

    dest_path = os.path.join(config.deploy_path, config.finmarket_store_deploy_directory)

    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    # копируем код
    shutil.copytree(config.finmarket_store_source_path, dest_path, dirs_exist_ok=True)

