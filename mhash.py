#!/usr/bin/env python3
import click
import base64
import sys

@click.command()
@click.argument('plaintext')
@click.option('-f', '--file', help='File to read from', default="")
@click.option('--length', '-l', default=32, help='Length of cipertext', show_default=True)
@click.option('--encoding', '-e', help='Output encoding', default=None)
@click.version_option(version='0.0.2')
@click.help_option('--help', '-h')

def hashing(plaintext, file, length=32, encoding=None):
    """Hash the PLAINTEXT with a given LENGTH"""

    if file != "":
        plaintext = file.read()

    seed = 0
    hash = []
    salt = 0
    random_length_num = 1
    text = "abcdefghjiklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ)(*&%$#@!<>?"

    for char in plaintext:
        random_length_num += ord(char) + random_length_num
        random_length_num += ~ len(plaintext)

    while salt <= length:
        seed += ord(plaintext[salt % len(plaintext)]) + salt * random_length_num
        hash.append(text[(seed**salt*random_length_num) % len(text)])
        salt += 1
        random_length_num += 1

    if encoding == None:
        click.echo("".join(hash))
    elif encoding == "base64":
        click.echo(base64.b64encode("".join(hash).encode()).decode())
    elif encoding == "hex":
        click.echo("".join(hash).encode().hex())

if __name__ == '__main__':
    hashing()