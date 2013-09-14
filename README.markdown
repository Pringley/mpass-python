mPass
=====

mPass is a manageable way to maintain secure and unique passwords for the
dozens of web services we use every day. Instead of saving all your passwords
to your hard drive or trusting them to a third party, though, mPass uses the
mathematical concept of a one-way function to "remember" your passwords.

mPass is really more of a specification than an application. It takes a SHA-512
HMAC of a given domain (using a "master password" as the key) and outputs the
first ten digits in base 64.

This is a Python implementation of the specification.

## Installation

Simply run:

    pip install mpass

This may require administrative privileges.

## Usage

On the command line, run:

    mpass [DOMAIN]

You will see a prompt for your master password. Once you enter that, a
site-specific password for DOMAIN will be printed to standard output.

## License

Copyright 2013 Ben Pringle

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
