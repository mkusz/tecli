import setuptools

setuptools.setup(
    name="tecli",
    version="1.0.0",
    packages=setuptools.find_packages(),
    py_modules=['main', 'cli'],
    install_requires=[
        "Faker>=12.3.3",
        "requests>=2.27.1",
        "typer>=0.4.0",
        "pyperclip>=1.8.2",
    ],
    entry_points={
        "console_scripts": ["tecli=main:app"]
    }
)
