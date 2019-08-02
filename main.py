from instapy_cli import client

username = ''
password = ''

image= 'foto_perfil.jpg'

text= 'test' + '#instapy-cli'

with client(username, password) as cli:
    cli.upload(image,text)