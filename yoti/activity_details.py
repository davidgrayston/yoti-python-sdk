# -*- coding: utf-8 -*-
from yoti.protobuf.v1.protobuf import Protobuf


class ActivityDetails:
    def __init__(self, receipt, decrypted_profile):
        self.decrypted_profile = decrypted_profile
        self.user_profile = {}

        if hasattr(decrypted_profile, 'attributes'):
            for field in decrypted_profile.attributes:
                value = Protobuf().value_based_on_content_type(
                    field.value,
                    field.content_type
                )
                self.user_profile[field.name] = value

        self.user_id = receipt['remember_me_id']
        self.outcome = receipt['sharing_outcome']