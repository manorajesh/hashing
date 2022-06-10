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

    plaintext = plaintext.encode('utf-8')
    ciphertext = 0
    H = [0x428a2f98d728ae22, 0x7137449123ef65cd, 0xb5c0fbcfec4d3b2f, 0xe9b5dba58189dbbc]

    sum = 0
    for i, v in enumerate(plaintext):
        sum += i ^ v
        
    for i in H:
        sum = sum ^ i
        sum = sum << length | sum >> length
        sum = sum ^ i
        sum = sum << length | sum >> length

    plaintext_length = len(plaintext)
    for i in range(length):
        ciphertext = ciphertext ^ plaintext[i % plaintext_length]
        ciphertext = ciphertext >> length | ciphertext << length
        ciphertext = ciphertext ^ sum >> plaintext[i % plaintext_length]
    
    click.echo(hex(ciphertext%10000000000000000000000000000000000000000000000000000001)[2:])

if __name__ == '__main__':
    hashing()