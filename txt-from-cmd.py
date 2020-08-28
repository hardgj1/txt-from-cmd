
from nexmo import Sms
import click

@click.command()
@click.option('--msg')
@click.option('--key')
@click.option('--secret')
@click.option('--nfrom')
@click.option('--nto')
def api(msg, key, secret, nfrom, nto):
    #ctext = wikipedia.summary(cname, sentences=1)
    client = Sms(key=key, secret=secret)
    result = client.send_message({
        'from': nfrom,
        'to': nto,
        'text': msg,
    })
    print(f"Sent API message result: {result}")
    return result

if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    api()