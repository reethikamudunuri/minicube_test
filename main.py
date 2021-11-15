from kube import PodApi
from rules import ApplyRules
import pprint


def main():
    pod_api = PodApi()
    pods = pod_api.build_pod_details()
    rules = ApplyRules()
    result = rules.validate(
        pods=pods
    )
    print(result)


# start of projection execution
if __name__ == '__main__':
    main()