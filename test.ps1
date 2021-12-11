$SCRIPT_DIR=$PSScriptRoot
$VENV="pyenv38"
$required_packages="pyyaml", "pillow", "matplotlib"
$_update=$args[0]
$ErrorActionPreference = "Stop"

# Create the venv if it doesn't exist
if (!(Test-Path -Path "${SCRIPT_DIR}/${VENV}")) {
	Write-Output "Creating virtual Environment"
	py -3.8 -m venv "${VENV}"
	$_update="update"
}

if (Test-Path -Path "${SCRIPT_DIR}/${VENV}") {
    # Activate venv
    & "${SCRIPT_DIR}/${VENV}/Scripts/activate.ps1"

    # Update python packages if needed / requested
    if ($_update -eq "update") {
    	py -m pip install --upgrade pip
    	py -m pip install $required_packages
    }

    # run tests
    py test.py
}
