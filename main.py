import oid85_finmarket
import oid85_finmarket_app
import oid85_finmarket_resource_store

if __name__ == '__main__':
    steps = [1, 3]

    if 1 in steps:
        oid85_finmarket.deploy()

    if 2 in steps:
        oid85_finmarket_app.deploy()

    if 3 in steps:
        oid85_finmarket_resource_store.deploy()
