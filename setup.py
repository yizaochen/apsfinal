from setuptools import setup, find_packages

setup(name='apsfinal', 
      version='0.1',
      packages=find_packages(),
      url='https://github.com/yizaochen/apsfinal.git',
      author='Yizao Chen',
      author_email='yizaochen@gmail.com',
      license='MIT',
      install_requires=[
          'pandas',
          'numpy',
          'matplotlib',
          'tabulate',
          'scipy',
          'jupyter-book',
          'pyppeteer'
      ]
      )
