from paths.paths import HOME
from paths.paths import MEM_USAGE_PATH

MEM_USAGE_CMD = r"free -m | awk '{{if(NR==2) print $3}}' >> {}".format(MEM_USAGE_PATH)
