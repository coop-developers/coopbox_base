#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""Run a python program within a virtualenv constructed by installing any
packages specified under the requirements.txt file under the working directory.
"""
# Author: Yichen Zhao
# License: MIT Licensed
# Version: 0.1

import subprocess
import os
import argparse
import sys
import logging
import shutil

logging.basicConfig(format='%(message)s')
log = logging.getLogger('withenv')
logging.getLogger().setLevel(logging.INFO)

config = {
    'virtualenv_binary': 'virtualenv',
    'requirements_file': 'requirements.txt',
    'virtualenv_run_directory': '.virtualenv_run',
    'bin_dir': 'bin',
    'default_action': ['bash', '-c',
        'echo This is a virtualenv shell; bash --norc'],
}

platform_configs = {
    'win32': {
        'virtualenv_run_directory': '.virtualenv_run_win',
        'virtualenv_binary': '{sys.executable}/../Scripts/virtualenv',
        'bin_dir': 'Scripts',
        'default_action': ['cmd', '/c', 'echo You must run a command under windows'],
    }
}

def update_platform_config():
    platform_config = platform_configs.get(sys.platform, {})
    for key, value in platform_config.iteritems():
        if isinstance(value, basestring):
            platform_config[key] = value.format(**globals())

    config.update(platform_config)

class Inenv(object):

    def __init__(self, args):
        self.args = args

    def discover_requirements(self):
        if not os.path.isfile(config.get('requirements_file')):
            raise ValueError(config.get('requirements_file') +
                    ' is not present in the current folder')

        self.requirements_file = config.get('requirements_file')

    def setup_virtualenv(self):
        """Discover existing virtualenv and create one if non present"""
        create_virtualenv = False
        if not os.path.isdir(config.get('virtualenv_run_directory')):
            os.mkdir(config.get('virtualenv_run_directory'))
            create_virtualenv = True

        self.virtualenv_dir = config.get('virtualenv_run_directory')

        if create_virtualenv:
            log.info("Creating new virtualenv")
            try:
                arguments = [config.get('virtualenv_binary')]
                if not self.args.use_site_packages:
                    arguments.append('--no-site-packages')
                else:
                    arguments.append('--system-site-packages')
                arguments.append(self.virtualenv_dir)
                subprocess.check_call(arguments)
            except Exception:
                log.info('Destroying (potentially broken) virtualenv directory')
                shutil.rmtree(self.virtualenv_dir)
    
    def get_virtualenv_path(self, path):
        return os.path.join(self.virtualenv_dir, path)

    def get_virtualenv_bin(self, bin):
        return os.path.join(self.get_virtualenv_path(config['bin_dir']), bin)

    def install_requirements(self):
        requirements_sentinel = self.get_virtualenv_path(
                os.path.basename(self.requirements_file))
        requirements_new = False
        if not os.path.isfile(requirements_sentinel):
            requirements_new = True
        else:
            if (os.stat(requirements_sentinel).st_mtime <
                    os.stat(self.requirements_file).st_mtime):
                requirements_new = True
        
        if self.args.upgrade:
            log.info("Upgrading packages")
            subprocess.check_call([
                self.get_virtualenv_bin('pip'),
                'install',
                '--upgrade',
                '-r', self.requirements_file
            ])

        elif requirements_new:
            log.info("Installing new packages")
            subprocess.check_call([
                self.get_virtualenv_bin('pip'),
                'install',
                '-r', self.requirements_file
            ])
        else:
            return

        # Touch requirements_sentinel to mark the current time
        with open(requirements_sentinel, 'w'):
            pass

    def run_command(self):
        if self.args.command:
            os.environ['PATH'] = (
                os.path.abspath(self.get_virtualenv_path(config['bin_dir'])) + os.pathsep +
                os.path.join(os.path.dirname(os.path.abspath(sys.executable)), config['bin_dir']) + os.pathsep +
                    os.environ['PATH'])

            command_list = self.args.command
            binary = command_list[0]
            full_binary = os.path.abspath(self.get_virtualenv_bin(binary))
            if not full_binary.lower().endswith('.exe'):
                full_binary += '.exe'
            if os.path.isfile(full_binary):
                # force use virtualenv python.exe under windows
                proc = subprocess.Popen(self.args.command, executable=full_binary)
            else:
                proc = subprocess.Popen(self.args.command)
            while True:
                try:
                    proc.wait()
                    exit(proc.poll())
                except KeyboardInterrupt:
                    continue
        else:
            log.info("Done, nothing to run.")

    def run(self):
        self.discover_requirements()
        self.setup_virtualenv()
        self.install_requirements()
        self.run_command()

def main():
    update_platform_config()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-N', '--no-command', dest='no_command',
                        action='store_true', default=False,
                        help='run virtualenv and pip without a command')
    parser.add_argument('--upgrade', '-U', dest='upgrade', default=False,
                        action='store_true',
                        help='force run pip with --upgrade')
    parser.add_argument('-s', '--use-site-packages', dest='use_site_packages',
                        default=False,
                        action='store_true',
                        help='create virtualenv with --system-site-packages. '
                             'Does not work if virtualenv has already been '
                             'created')
    parser.add_argument('command', nargs=argparse.REMAINDER,
            default=config['default_action'])
    args = parser.parse_args()
    if args.no_command:
        args.command = []

    instance = Inenv(args)
    instance.run()

if __name__ == '__main__':
    main()
