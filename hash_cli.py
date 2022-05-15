import click

@click.command()
@click.option('--length', '-l', default=32, help='Length of cipertext')
@click.argument('plaintext')

def hashing(plaintext, length):
    """Hash PLAINTEXT with a given LENGTH."""
    seed = 0
    hash = []
    salt = 0
    random_length_num = 1
    text = "abcdefghjiklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ)(*&%$#@!"

    for char in plaintext:
        random_length_num += ord(char)

    while salt <= length:
        seed += ord(plaintext[salt % len(plaintext)]) + salt * random_length_num
        hash.append(text[(seed**salt*random_length_num) % len(text)])
        salt += 1
    
    click.echo("".join(hash))

if __name__ == '__main__':
    hashing()