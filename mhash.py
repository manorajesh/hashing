#!/usr/bin/env python3
import click
import base64

@click.command()
@click.option('--length', '-l', default=32, help='Length of cipertext', show_default=True)
@click.option('-p', '--plaintext', help='Plaintext to be hashed')
@click.option('--file', '-f', help='Hash the input file', type=click.File('r'), default=None)
@click.version_option(version='0.0.2')
@click.help_option('--help', '-h')

def hashing(file, plaintext="", length=32):
    """Hash the PLAINTEXT with a given LENGTH"""
    if file != None:
        file.seek(0)
        plaintext = file.read()

    seed = 0
    hash = []
    salt = 0
    random_length_num = 1
    text = "abcdefghjiklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ)(*&%$#@!<>?"

    for char in plaintext:
        random_length_num += ord(char) + random_length_num
        random_length_num = ~ random_length_num + (random_length_num << 15)
        random_length_num += random_length_num >> random_length_num
        random_length_num += ~ len(plaintext)

    while salt <= length:
        seed += ord(plaintext[salt % len(plaintext)]) + salt * random_length_num
        hash.append(text[(seed**salt*random_length_num) % len(text)])
        salt += 1
        random_length_num += 1
    click.echo("".join(hash))

if __name__ == '__main__':
    hashing()