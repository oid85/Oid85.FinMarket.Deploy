import time
import os

# sc create "Oid85 FinMarket Service" binPath="...exe"


def deploy():
    source_path = 'C:\Repository\Oid85.FinMarket\Oid85.FinMarket'
    deploy_path = 'C:\Deploy'
    deploy_directory = 'Oid85.FinMarket'
    #service_name = 'Oid85 FinMarket Service'
    service_name = 'tvnserver'

    # остановка и удаление службы
    os.system(f'sc stop """{service_name}"""')
    #os.system(f'sc delete """{service_name}"""')
"""
    # формируем директории
    if not os.path.exists(deploy_path):
        os.makedirs(deploy_path)

    if not os.path.exists(os.path.join(deploy_path, deploy_directory)):
        os.makedirs(os.path.join(deploy_path, deploy_directory))

    current_time = time.time()
    current_deploy_version = f"{current_time}"

    path = os.path.join(deploy_path, deploy_directory, current_deploy_version)

    if not os.path.exists(path):
        os.makedirs(path)

    # build
    os.system(f"cd {source_path} && dotnet build --configuration Release --output {path}")

    # установка и запуск службы
"""