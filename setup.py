import setuptools

if __name__ == "__main__":
    setuptools.setup(
        name='gen_commonpw',
        version='1.0.0',
        install_requires=[
            'sre_yield'
        ],
        packages=setuptools.find_packages(),
        py_modules=['gen_commonpw'],
        entry_points={
            'console_scripts': [
                'gen_commonpw = gen_commonpw:main',
            ],
        },
    )
