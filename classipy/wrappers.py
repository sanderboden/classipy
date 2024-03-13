from argparse import Namespace
from logging import getLogger
import os
from glob import glob
from subprocess import Popen, PIPE

class Wrappers():
    l = getLogger("Wrappers")


    def __init__(self, args: Namespace):
        self.l.debug("Creating instance")

        self.fq: str = os.path.join(os.path.abspath(args.fastq), '*.fastq')
        self.db: str = os.path.abspath(args.db)
        self.out: str = os.path.abspath(args.outdir)
        if not os.path.exists(self.out):
            os.mkdir(self.out)
        self.t: int = args.threads


    def kraken2(self):
        cmd = f"kraken2 --db {self.db} --threads {self.t} {self.fq}"
        self.l.info("Running Kraken2...")
        self.l.debug(cmd)
        run = Popen(
            cmd,
            stdout=PIPE,
            stderr=PIPE,
            shell=True,
        )

        stdout, stderr = run.communicate()
        if run.returncode == 0:
            with open(os.path.join(self.out, "kraken.txt"), 'w') as outfile:
                outfile.write(stdout.decode("utf-8"))
                self.krk_out: str = os.path.join(self.out, "kraken.txt")
        else:
            self.l.error(f"Error: {stderr.decode("utf-8")}")
        
                


