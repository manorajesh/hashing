#!/usr/bin/env python3
import click
import base64
import sys

@click.command()
@click.argument('plaintext', type=click.File('r'), default=sys.stdin)
@click.option('--length', '-l', default=32, help='Length of cipertext', show_default=True)
@click.option('--encoding', '-e', help='Output encoding', default=None)
@click.version_option(version='0.0.2')
@click.help_option('--help', '-h')

def hashing(plaintext, length, encoding):
    """Hash the FILE, or if no FILE is given, read standard input, and print the hash to standard output."""

    if plaintext != "":
        plaintext = plaintext.read()

    cardamom = len(plaintext)
    hash = []
    salt = 0
    pepper = 0
    counter = 0
    text = "abcdefghjiklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ)(*&%$#@!<?"

    for char in plaintext:
        pepper += ord(char) + pepper
        pepper += ~ len(plaintext)

    while counter <= length:
        cardamom += pepper * cardamom & salt
        pepper += 2
        salt += ~ len(plaintext)
        counter += 1
    
    counter = 0
    plaintext = plaintext.encode()
    while counter <= length:
        cardamom = (salt << pepper) | (cardamom >> pepper)
        hash.append(text[(cardamom*salt*pepper) % len(text)])
        pepper += plaintext[counter % len(plaintext)]
        salt += 1
        counter += 1

    if encoding == None:
        click.echo("".join(hash))
    elif encoding == "base64":
        click.echo(base64.b64encode("".join(hash).encode()).decode())
    elif encoding == "hex":
        click.echo("".join(hash).encode().hex())

if __name__ == '__main__':
    hashing()