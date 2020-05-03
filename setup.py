import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="down_all_images_in_web",
  version="0.0.0",
  author="Phuc Trinh",
  author_email="trinhcanhphuc@gmail.com",
  description="Get ALl Images in a Website",
  long_description="Get ALl Images in a Website base url. You can download files from one or many URL and save them into a destionation directory.",
  long_description_content_type="text/markdown",
  url="https://github.com/trinhcanhphuc/get-all-images-from-url.git",
  packages=setuptools.find_packages(),
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  python_requires='>=3.6',
)