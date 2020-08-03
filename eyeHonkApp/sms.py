from twilio.rest import Client

account_sid = "AC61f212c632286f324632d67bca197248"
auth_token = "a6af25f1b72756dc48b38b24a38a5fb0"

client = Client(account_sid, auth_token)


def food():
    client.messages.create(
        to="+353834442465",
        from_="+12058903913",
        body="Connor wants food!"
    )


def water():
    client.messages.create(
        to="+353834442465",
        from_="+12058903913",
        body="Connor wants water!"
    )


def bathroom():
    client.messages.create(
        to="+353834442465",
        from_="+12058903913",
        body="Connor needs the bathroom!"
    )


def honk():
    client.messages.create(
        to="+353834442465",
        from_="+12058903913",
        body="Connor needs assistance!"
    )


# food()
# water()
# bathroom()
# honk()

