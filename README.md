# Daily Number Incrementer

A Python script that automatically increments a number in a text file, commits the change to Git, and updates a cron job to run the script at a new random time daily. Perfect for maintaining a daily commit streak or tracking sequential values with a dynamic schedule.

## Setup

1. Clone this repository:

```bash
git clone https://github.com/Shogun89/fancy_job
cd fancy_job
```

2. Run the script manually for the first time to verify it works and to set the cron job:

```bash
python update_number.py
```

3. Optional: If you prefer to ensure the script runs at a fixed time initially, you can manually set up a cron job:

```bash
crontab -e
```

Add the following line to the crontab file:

```bash
0 6 * * * cd /path/to/your/repo && python update_number.py
```

This will initially run the script at 6am the next day.

## Usage

The script will increment the number in `number.txt` and commit the change to git. You can modify the script to increment by any value or use a different file to store the number.

By running this you will be able get a fancy streak on your github profile and get a job.

![How to get a job](get_a_job.jpg)
