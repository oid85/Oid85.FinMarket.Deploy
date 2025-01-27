import oid85_finmarket
import oid85_finmarket_app
import oid85_finmarket_resource_store

if __name__ == '__main__':
    switcher = 3

    if switcher == 1:
        oid85_finmarket.deploy()

    if switcher == 2:
        oid85_finmarket_app.deploy()

    if switcher == 3:
        oid85_finmarket_resource_store.deploy()
