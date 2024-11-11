from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'CLI Address book'
LONG_DESCRIPTION = 'CLI Address book for adding contacts with date of birthday and notes. Providing search by tags'

# Setting up
setup(
    python_requires='>=3.5',
    name="addr-book",
    version=VERSION,
    author="Anton",
    author_email="<youremail@email.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),  # Search for packages inside 'src'
    package_dir={"": "addr_book"},  # Map top-level package to src
    install_requires=['setuptools'],  # Additional dependencies if needed
    entry_points={
        "console_scripts": [
            "addr-book=addr_book.main:main",  # Ensure this references the correct location of your main function
        ],
    },
)
