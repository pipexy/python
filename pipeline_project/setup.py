from setuptools import setup, find_packages

setup(
    name="pipeline_project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "grpcio>=1.44.0,<2.0.0",
        "grpcio-tools>=1.44.0,<2.0.0",
        "opencv-python>=4.5.5.64",
        "numpy>=1.26.0",  # Updated for Python 3.12 compatibility
        "pytest>=7.1.1",
        "protobuf>=3.20.3,<5.0.0dev",  # Compatible with tensorflow and mediapipe
    ],
    python_requires=">=3.7",
    author="Tom Sapletta",
    author_email="info@softreck.dev",
    description="Video processing pipeline with gRPC services",
    keywords="video, processing, pipeline, grpc",
)
