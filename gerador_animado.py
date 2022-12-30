from amzqr import amzqr

amzqr.run(
    'https://bit.ly/mapa-de-salas-ft',
    level='H',
    picture='ft.png',
    colorized=True,
    save_name='qrcode1.png',
    save_dir='./',

)