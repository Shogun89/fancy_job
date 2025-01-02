# Daily Number Incrementer

A simple Python script that automatically increments a number in a text file and commits the change to git. Perfect for maintaining a daily commit streak or tracking sequential values.

---

## Why Use This Script?

1. **Daily GitHub Streaks**: Keep your GitHub profile active with consistent daily commits.
2. **Job Readiness**: Enhance your profile with a visually appealing streak that can impress recruiters.
3. **Customization**: Use this as a foundation to build more automated scripts for your projects.

---

## Setup

1. Clone this repository:

```bash
git clone https://github.com/Shogun89/fancy_job
cd fancy_job
```

2. Run the script:

```bash
python update_number.py
```

3. Setup a cron job to run the script daily:

```bash
crontab -e
```

Add the following line to the crontab file:

```bash
0 6 * * * cd /path/to/your/repo && python update_number.py
```

This will run the script at 6am every day.

## Usage

The script will increment the number in `number.txt` and commit the change to git. You can modify the script to increment by any value or use a different file to store the number.

By running this you will be able get a fancy streak on your github profile and get a job.

![How to get a job](get_a_job.jpg)
