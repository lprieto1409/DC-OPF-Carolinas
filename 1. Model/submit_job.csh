#!/bin/tcsh
#BSUB -J DC_OPF_normal
#BSUB -n 8
#BSUB -R "span[hosts=1]"
#BSUB -W 5760
#BSUB -o out.%J
#BSUB -e err.%J
#BSUB -q cnr

# activate environment
conda activate /usr/local/usrapps/infews/group_env
module load gurobi

# Set the folder that you want to check (Individual Runs)
set Portfolio = P3
set Scenario = Interim
set year = 1940

# Define the path to the Python scripts
set script_dir = "/share/infews/lprieto/Paper_2_DC_OPF/Model_future_fleets/Reanalysis_inputs/${Scenario}/${Portfolio}/${year}_DC_OPF_${Scenario}"
set python_script1 = "$script_dir/MTSDataSetup_${Scenario}_${Portfolio}_${year}.py"
set python_script2 = "$script_dir/wrapper_${Scenario}_${Portfolio}_${year}.py"

# Error handling
if (! -e $python_script1 || ! -e $python_script2) then
    echo "One or both Python scripts do not exist in $script_dir"
    exit 1
endif

# Run scripts
python $python_script1
if ($status == 0) then
    echo "MTSDataSetup.py ran successfully"
    python $python_script2
else
    echo "MTSDataSetup.py did not run successfully"
endif

conda deactivate
