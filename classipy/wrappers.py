from argparse import Namespace
from logging import getLogger
import os
from subprocess import Popen, PIPE

class Wrappers():
    l = getLogger("Wrappers")


    def __init__(self, args: Namespace):
        self.l.debug("Creating instance")

        self.fq: str = os.path.abspath(args.fastq)
        self.db: str = os.path.abspath(args.db)
        self.out: str = os.path.abspath(args.outdir)
        self.t: int = args.threads


