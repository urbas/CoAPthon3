from distutils.core import setup

setup(
    name='CoAPthon3',
    version='1.0.1',
    packages=['coapthon', 'coapthon.caching', 'coapthon.layers', 'coapthon.client', 'coapthon.server', 'coapthon.messages',
              'coapthon.forward_proxy', 'coapthon.resources', 'coapthon.reverse_proxy'],
    url='https://github.com/Tanganelli/CoAPthon3',
    license='MIT License',
    author='Giacomo Tanganelli',
    author_email='giacomo.tanganelli@for.unipi.it',
    download_url='https://github.com/Tanganelli/CoAPthon3/archive/1.0.1.tar.gz',
    description='CoAPthon is a python library to the CoAP protocol. ',
    entry_points={
        "console_scripts": [
            "coapclient = coapthon.coapclient:main",
            "coapcollectserver = coapthon.collectserver:main",
            "coapforwardproxy = coapthon.coapforwardproxy:main",
            "coapreverseproxy = coapthon.coapreverseproxy:main",
            "coapserver = coapthon.coapserver:main",
        ]
    },
    requires=['sphinx', 'cachetools']
)
