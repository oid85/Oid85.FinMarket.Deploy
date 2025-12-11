import oid85_finmarket
import oid85_finmarket_resource_store

if __name__ == '__main__':
    steps = [3]

    if 1 in steps:
        oid85_finmarket.deploy()

    if 2 in steps:
        oid85_finmarket_resource_store.deploy()

    if 3 in steps:
        oid85_finmarket.deletet()
