from setuptools import setup, find_packages

setup(
    name="addrbook",  # Замінити на реальну назву
    version="0.1.0",
    packages=find_packages(where="addr_book"),
    package_dir={"": "addr_book"},
    py_modules=["main"],
    author="Anton Kalianov, Avramets Yurii, Rostyslav Rachynskyi, Bohdan Hulchuk",
    entry_points={
        "console_scripts": [
            "addrbook=main:main",  # заміни main_function на ім'я головної функції
        ],
    },
)
