CHESS TOURNAMENT MANAGER -  SWISS PAIRING SYSTEM <br>
<br>
## OVERVIEW
Beta version of a chess tournament manager (Swiss system).
<br>
<br>
## REQUISITORIES <br>
<br>
Python3<br>
<br>

## INSTALLATION 
Start by closing the repository :
```
git clone https://github.com/pascaline841/tournament
```
- Start access the project folder
- Create a virtual environment
- Install the python dependencies on the virtual environment
```
pip install -r requirements
```
## Use FLAKE8
In order to generate a flake8 report, run the following command :
```
flake8 --format=html --htmldir=flake-report --exclude=env
```
Open the html file into the flake-report repertory to show the report.

## LAUNCH 
Run 
```
python main.py
```
1. Add 8 players. <br>
2. Create a new tournament. <br>
3. The computer generates pairs of players for the first round. <br>
4. When the round is finished, enter the results. <br>
5. Repeat steps 3 and 4 for subsequent rounds until 4 rounds are played, and the tournament is over. <br>

