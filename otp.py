def send_verification_code_sms(self, dst_number: str, message):
    """
    `send_verification_code` accepts destination number
    to which the message that has to be sent.

    The message text should contain a `__code__` construct
    in the message text which will be
    replaced by the code generated before sending the SMS.

    :param: dst_number
    :param: message
    :return: verification code
    """
    try:
        response = self.client.messages.create(
            src=self.app_number, dst=dst_number, text=message
        )
        print(response)
        return response
    except Exception as e:
        print(e)
        return "Error encountered", 400


