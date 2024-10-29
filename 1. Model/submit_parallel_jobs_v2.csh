#!/bin/tcsh

# Set up conda and gurobi environment
conda activate /usr/local/usrapps/infews/group_env
module load gurobi

# Define the base directory (absolute path)
set baseDir = /share/infews/lprieto/Paper_2_DC_OPF/Model_future_fleets/Reanalysis_inputs
set folNameBase = Interim

# Loop through portfolios P1, P2, (and P3)
foreach portfolio (P1 P2)
    echo "Processing portfolio ${portfolio}"

    # First loop for MTSDataSetup
    foreach year (`seq 1940 2024`)
        # Directory name (using absolute path)
        set dirName = ${baseDir}/${folNameBase}/${portfolio}/${year}_DC_OPF_${folNameBase}
        
        # Check if the directory exists
        if (-d $dirName) then
            cd $dirName
        else
            echo "Directory $dirName does not exist"
            continue   # Skip to the next year if directory is missing
        endif

        # Error handling for Python script existence
        set python_script1 = "${dirName}/MTSDataSetup_${folNameBase}_${portfolio}_${year}.py"
        
        if (! -e $python_script1) then
            echo "Python script $python_script1 does not exist"
            continue   # Skip to the next year if script is missing
        endif

        # Run scripts
        #bsub -n 8 -R "span[hosts=1]" -R "rusage[mem=60GB]" -W 5760 -o out.%J -e err.%J "python MTSDataSetup_${folNameBase}_${portfolio}_${year}.py"
        bsub -n 8 -R "span[hosts=1]" -R "rusage[mem=60GB]" -W 5760 -o out.%J -e err.%J "python wrapper_${folNameBase}_${portfolio}_${year}.py" 
        
        cd ..
    end
end

conda deactivate

