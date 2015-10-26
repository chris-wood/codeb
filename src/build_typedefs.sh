#!/bin/bash

# grep the specified file for all typedefs, and extract their definition
grep -r 'typedef' $1
