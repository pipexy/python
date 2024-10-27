from setuptools import setup, find_packages

setup(
    name="pipexy",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "grpcio>=1.44.0",
        "grpcio-tools>=1.44.0",
        "opencv-python>=4.5.5.64",
        "numpy>=1.22.3",
        "pytest>=7.1.1",
    ],
    python_requires=">=3.7",
    author="Your Name",
    author_email="your.email@example.com",
    description="Video processing pipeline with gRPC services",
    keywords="video, processing, pipeline, grpc",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
