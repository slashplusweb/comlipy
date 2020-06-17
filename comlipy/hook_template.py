commit_msg_template = '''#!/usr/bin/env bash

# get the commit message
commit_msg=$(<"${{1:-}}")

comlipy {config}"$commit_msg"
'''
