import oid85_finmarket
import oid85_finmarket_resource_store

if __name__ == '__main__':
    steps = [1, 2]

    if 1 in steps:
        oid85_finmarket.deploy()

    if 2 in steps:
        oid85_finmarket_resource_store.deploy()
