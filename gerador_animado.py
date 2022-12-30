from amzqr import amzqr

amzqr.run(
    'https://bit.ly/mapa-de-salas-ft',
    level='H',
    picture='image.png',
    colorized=True,
    save_name='qrcode.png',
    save_dir='./',

)