from setuptools import setup, find_packages

setup(
    name='CAVPP_Audio_Convert',
    version='0.1.1',
    packages=find_packages(),
    url='https://github.com/cavpp/audio_convert',
    install_requires=['OneSheet == 0.1.3.26'],
    license='GPL',
    author='Henry Borchers',
    author_email='hborcher@berkeley.edu',
    entry_points={'console_scripts' : ['makemp3 = audio_convert.scripts.audioConvert:installed_start']},
    description='Converts wav files into MP3 files according to CAVPP standards.'
)