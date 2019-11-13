import subprocess


def run_cmd(cmd):
	subprocess.check_call(cmd, shell=True)


def get_cmd_output(cmd):
	cmd_output = subprocess.check_output(cmd ,shell=True)
	return cmd_output
