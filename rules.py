from datetime import datetime, timezone


class ApplyRules(object):
    """
    ApplyRules class implements the following rules
    image_prefix
    label
    recent_start_time
    """
    ALLOWED_IMAGE_PREFIX = 'bitnami'

    def __init__(self):
        pass

    def __validate_image_prefix(self, images):
        """
        Returns True if all the images in the pod used the prefix
        defined in ALLOWED_IMAGE_PREFIX
        :param images:
        :return:
        """
        result = True
        for image in images:
            if image.split('/')[0] != ApplyRules.ALLOWED_IMAGE_PREFIX:
                return False
        return result

    def validate(self, pods):
        result = []
        for pod in pods:
            image_prefix_rule = self.__validate_image_prefix(
                images=pod.images)
            pod_result = {'pod': pod.name,'rule_evaluation': [{'name': 'image_prefix','valid': image_prefix_rule}]}
            result.append(pod_result)
        return result