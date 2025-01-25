import time
import os
import shutil


def deploy():
    source_path = 'C:\\Repository\\Oid85.FinMarket\\Oid85.FinMarket'
    deploy_path = 'C:\\Deploy'
    deploy_directory = 'Oid85.FinMarket'
    exe_file_name = "Oid85.FinMarket.WebHost.exe"
    service_name = 'Oid85.FinMarket'
    app_settings_file = 'appsettings.json'

    # остановка и удаление службы
    cmd = f'sc stop {service_name}'
    print(cmd)
    res = os.system(cmd)
    print(res)

    cmd = f'sc delete {service_name}'
    print(cmd)
    res = os.system(cmd)
    print(res)

    # формируем директории
    if not os.path.exists(deploy_path):
        os.makedirs(deploy_path)

    if not os.path.exists(os.path.join(deploy_path, deploy_directory)):
        os.makedirs(os.path.join(deploy_path, deploy_directory))

    current_time = time.time()
    current_deploy_version = f"{current_time}"

    dest_path = os.path.join(deploy_path, deploy_directory, current_deploy_version)

    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    # build
    cmd = f'cd {source_path} && dotnet build --configuration Release --output {dest_path}'
    print(cmd)
    res = os.system(cmd)
    print(res)

    # копируем appsettings.json
    shutil.copy(app_settings_file, dest_path)

    exe_file_path = os.path.join(dest_path, exe_file_name)

    # установка и запуск службы
    cmd = f'sc create {service_name} binPath={exe_file_path}'
    print(cmd)
    # res = os.system(cmd)
    print(res)

    cmd = f'sc start {service_name}'
    print(cmd)
    # res = os.system(cmd)
    print(res)
