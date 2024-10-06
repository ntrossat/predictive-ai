from setuptools import setup

setup(
    name="predictive_ai",
    description="Predictive AI Benchmark Tool",
    version="0.1.0",
    py_modules=["main"],
    install_requires=["Click", "SQLAlchemy"],
    entry_points={
        "console_scripts": [
            "predictive-ai = main:run",
        ],
    },
)
