#!/usr/bin/env python

### Author:
# Daisy Y. Kyu
# Nam Thi
# Victoria Lim (limvt@uci.edu)
# Caitlin C. Bannan (bannanc@uci.edu)

### Description: This Python script minimizes mol2 files in the
#     given directory with the specified force field. Minimizations
#     are completed with the ffld_server utility from Schrodinger.
#   For N input *.mol2 files, there should be N output
#     *.mol2 files, unless the input file is missing


### Example usuage:
# - python OPLS.py --input /input_directory/with/mol2s --optimizetype fftype > output.dat
# - python OPLS.py -i /input_directory/OPLS2005/with/mol2 -o OPLS2005  > output.dat

### Note:
# - Currently compatible with mol2 file types.
#   Call `$SCHRODINGER/utilities/ffld_server -hh` for more options.

### Supported force fields:
# - OPLS3
# - OPLS2005

import os

  # ---------------------------- Functions ------------------------- #

def OPLSMin(ifile,opttype, outdir):
    """
   
    Take one mol2 file and do the minimization, then output into
        a specific location.
    Note: the output directory is specified inside the command line.
        Refer to the help message in utilities for more information.
   
    Parameters
    ----------
    ifile: string, input file directory.
    opttype: string, force field type. Either 'OPLS3' or 'OPLS2005'.
    outdir: string, ouput directory

   
    """

    if opttype == 'OPLS3':  #specify which fftype to be run

        cmd = '$SCHRODINGER/utilities/ffld_server  -version 16 -charges_from_ct -virt \
               -no_cm1a_bcc -opt -BFGS -imol2 %s \ 
               -omol2 %s/%s'% (ifile, outdir, ifile.split('/')[-1])

        os.system(cmd)      #execute the command from the shell

    if opttype == 'OPLS2005':

        cmd = '$SCHRODINGER/utilities/ffld_server -version 14 -charges_from_ct -virt \
               -no_cm1a_bcc -opt -BFGS -imol2 %s \ 
               -omol2 %s/%s' % (ifile, outdir, ifile.split('/')[-1])

        os.system(cmd)

  # ------------------------- Parse Inputs ----------------------- #


if __name__ == '__main__':
    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option('-i','--input',
            help = "Path to directory containing all mol2 files to be minimized.",
            type = "string",
            dest = 'ifile')

    parser.add_option('-o','--optimizetype',
            help = "Name of the force field type to be used for minimization",
            type = "string",
            dest = 'opttype')
    
    parser.add_option('-d','--outdir',
            help = "Directory of the output location",
            type = "string",
            dest = 'outdir')
    (opt, args) = parser.parse_args()
    OPLSMin(opt.ifile,opt.opttype,opt.outdir)


