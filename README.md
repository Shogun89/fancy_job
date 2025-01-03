# Daily Number Incrementer

A simple Python script that automatically increments a number in a text file and commits the change to git. Perfect for maintaining a daily commit streak or tracking sequential values.

## Setup

1. Clone this repository:

```bash
git clone https://github.com/Shogun89/fancy_job
cd fancy_job
```

2.  Run the script

The script can be run without dependencies besides the Python standard library,
simply by running

```bash
python update_number.py
```

However, if you wish to use LLM-based commit message generation, you need to
install [uv](https://docs.astral.sh/uv) to manage dependencies.
The first time you run it, it will download packages required for its execution
and also a large language model from Hugging Face

```bash
# Use LLM
FANCY_JOB_USE_LLM=true uv run python update_number.py
```

3. Setup a cron job to run the script daily:

```bash
crontab -e
```

Add the following line to the crontab file:

```bash
0 6 * * * cd /path/to/your/repo && python update_number.py
# or with LLM
0 6 * * * cd /path/to/your/repo && FANCY_JOB_USE_LLM=true uv run python update_number.py
```

This will run the script at 6am every day.

## Usage

The script will increment the number in `number.txt` and commit the change to git. You can modify the script to increment by any value or use a different file to store the number.

By running this you will be able get a fancy streak on your github profile and get a job.

![How to get a job](get_a_job.jpg)
