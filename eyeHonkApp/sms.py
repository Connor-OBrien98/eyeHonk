from twilio.rest import Client

account_sid = "no"
auth_token = "no"

client = Client(account_sid, auth_token)


def food():
    client.messages.create(
        to="+1",
        from_="+12058903913",
        body="Connor wants food!"
    )


def water():
    client.messages.create(
        to="+1",
        from_="+12058903913",
        body="Connor wants water!"
    )


def bathroom():
    client.messages.create(
        to="+1",
        from_="+12058903913",
        body="Connor needs the bathroom!"
    )


def honk():
    client.messages.create(
        to="+1",
        from_="+12058903913",
        body="Connor needs assistance!"
    )


# food()
# water()
# bathroom()
# honk()

