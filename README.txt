# Description

    This script will first extract sequence from FASTA file to a string,then calculate GC content according to the defined window size and step,
    finally,it plots GC content against position.Users will get a image which plot GC content over a sequence(like a genome).
	
# Usage
    python3 GCploter.py [-h] [-o output_file] input_fasta_file window_size step

    This program plot GC content over a fasta sequence.

    positional arguments:
      input_fasta_file
      window_size
      step

    optional arguments:
      -h, --help        show this help message and exit
      -o output_file
   
# Output files

    [input_fasta_file].png
    
    It's binary format, image viewer should be installed.
    
    example:
    [input_fasta_file].png PNG 640x480 640x480+0+0 8-bit sRGB 2.41KB 0.000u 0:00.000

    
# AUTHOR

    Lina Lu, 2020