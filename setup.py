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
    install_requires=[
        'pandas >= 1.0.3',
        'matplotlib >= 3.2.2',
        'scipy >= 1.4.1',
        'xgboost >= 1.1.1',
        'psutil >= 5.7.0',
        'ray >= 0.8.4',
        'vaex_core >= 2.0.3',
        'pytictoc >= 1.5.0',
        'gdown >= 3.11.1',
        'numpy >= 1.18.4',
        'seaborn >= 0.10.1',
        'modin >= 0.7.3',
        'python_dateutil >= 2.8.1',
        'PyYAML >= 5.3.1',
        'scikit_learn >= 0.23.1',
        'vaex >= 3.0.0'
    ],
    data_files=[
        ("smnsr", ["smnsr/logging.yaml"]),
        ("modalities", ["modalities/modalities.yaml"]),
    ],
)
