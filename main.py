from kube import Pod
from rules import ApplyRules
import pprint




def main():
    pod = Pod()
    pods = pod.build_pod_details()
    rules = ApplyRules()
    result = rules.validate(
        pods=pods
    )
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(result)


if __name__ == '__main__':
    main()
