import os
import shutil


def deploy():
    source_path = 'C:\\Repository\\Oid85.FinMarket.ResourceStore\\store'
    deploy_path = 'C:\\Deploy'
    deploy_directory = 'Oid85.FinMarket.ResourceStore'

    # формируем директориЮ
    if not os.path.exists(deploy_path):
        os.makedirs(deploy_path)

    # удаляем папку
    if os.path.exists(os.path.join(deploy_path, deploy_directory)):
        shutil.rmtree(os.path.join(deploy_path, deploy_directory))

    dest_path = os.path.join(deploy_path, deploy_directory)

    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    # копируем код
    shutil.copytree(source_path, dest_path, dirs_exist_ok=True)

