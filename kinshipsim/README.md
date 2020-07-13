# KINSHIP SIMULATION<br>
### *version 2020.8*

---

1. The *kinshipsim* package
    - Install the kinshipsim package:<br>
    `$ pip install ~/PycharmProjects/kinshipsim/dist/kinshipsim-2020.6-py3-none-any.whl`

    - Uninstall the previous version of the *kinshipsim* package:<br>
    `$ pip uninstall kinshipsim`
    
    - See the location where the kinshipsim package has been installed:<br>
    `$ pip show kinshipsim`

2. Environment variables
    - Setup the environment variable to identify the location of the scripts:<br>
    `$ KINSHIP_SCRIPTS_DIR="/lib/.../site-packages/kinshipsim/scripts"`<br>
    `$ export KINSHIP_SCRIPTS_DIR`

    - Setup the environment variable to identify the location of the Linux shell scripts:<br>
    `$ KINSHIP_SHELL_DIR="/lib/.../site-packages/kinshipsim/shell"`<br>
    `$ export KINSHIP_SHELL_DIR`

    - Setup the environment variable to identify the location of *ngsRelate*:<br>
    `$ NGSRELATE_DIR="$HOME/ngsRelate"`<br>
    `$ export NGSRELATE_DIR`

3. Steps of the simulation
    - Insert into the *VCF* file the frequency values stored in the *FRQ* and *MAP* files.<br><br>
    Example:<br> `$ python $KINSHIP_SCRIPTS_DIR/run_maf2vcf.py --vcf_file input_file.vcf --maf_file freq_file.frq --map_file map_file.map`

    - Validate the *VCF* file, i.e., check the correct order of the position for each chromosome and check for duplicate entries - same (chromosome, position).<br>
    The script also offers to fix the *VCF* file if any inconsistencies are found.<br><br>
    Example:<br> `$ python $KINSHIP_SCRIPTS_DIR/run_validate_vcf.py --filename input_file.vcf`

    - Initialize a new set of pedigrees (autosome, x chromosome or both) starting from reference file(s) of unrelated individual.<br><br>
    Example:<br> `$ python $KINSHIP_SCRIPTS_DIR/run_init_pedigrees.py --atDNA_reference at_founders.vcf --xDNA_reference x_founders.vcf --n_pedigree 10 --output_folder pedigrees`
         
    - Initialize the X chromosomes of an already existing autosome-data pedigrees. It requires a reference file of unrelated individuals X chromosomes, the folder of the existing pedigrees along with the number of pedigrees to be updated.<br><br>
    Example:<br> `$ python $KINSHIP_SCRIPTS_DIR/run_init_x_chromosome.py --reference_file x_chr_file.vcf --working_folder pedigrees --n_pedigree 10`

    - Reduce the number of SNPs, for a single *VCF* file or for a group of pedigrees (autosome, X chromosome or both).<br><br>
    Examples:<br> `$ python $KINSHIP_SCRIPTS_DIR/run_reduce_snps.py --vcf_file samples.vcf --n_snps [50000,20000,10000,5000] --working_folder ./study`<br><br>
    `$ $KINSHIP_SHELL_DIR/run_reduce_snps.sh 1 10 [50000,20000,10000,5000] ./study 1 0 1`

    - Pseudo-haploidization (repeated *n* times) for a single *VCF* file.<br><br>
    Examples:<br> `$ python $KINSHIP_SCRIPTS_DIR/run_haploidize.py --vcf_file samples.vcf --n 10`<br><br>
    `$ $KINSHIP_SHELL_DIR/run_haploidize.sh 1 10 ./study 5 1 50000 20000 10000 5000`

    - Run the *ngsRelate* analysis for the pedigrees (autosome, X chromosome or both) considering also haploidized data (only for autosome) and for the different SNPs.<br><br>
    Example:<br> `$ $KINSHIP_SHELL_DIR/run_ngs.sh 1 10 ./study 1 1 10 1 50000 20000 5000`

    - Print out averaged results from *ngsRelate* analysis of the simulation and export all estimates in Excel sheets.<br><br>
    Example:<br> `$ python $KINSHIP_SCRIPTS_DIR/run_sim_results.py --working_folder study --info_type atDNA_deg --n_ped 10 --snps [50000,20000,5000]`
