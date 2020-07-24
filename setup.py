import setuptools

setuptools.setup(
    name="smnsr",
    version="0.4.3",
    author="rciszek",
    author_email="rkciszek@gmail.com",
    description="SMNSR",
    long_description="SMNSR",
    long_description_content_type="text/markdown",
    url="https://github.com/rciszek/SMNSR/",
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    scripts=[("bin/smnsr_ts_folds"), ("bin/smnsr_cv"), ("bin/smnsr_merge")],
    data_files=[
        ("smnsr", ["smnsr/logging.yaml"]),
        ("modalities", ["modalities/modalities.yaml", "modalities/TADPOLE_D1_D2.csv"]),
    ],
)
