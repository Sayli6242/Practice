"""
Sebi goes to school daily with his father. They cross a big highway in the car to reach to the school. Sebi sits in front seat beside his father at driving seat. 
To kill boredom, they play a game of guessing speed of other cars on the highway. 
Sebi makes a guess of other car's speed being SG kph, his father FG kph.
The highway is usually empty, so the drivers use cruise control, i.e. vehicles run at a constant speed. There are markers on the highway at a gap of 50 meters. 
Both father-son duo wants to check the accuracy of their guesses. 
For that, they start a timer at the instant at which their car and the other car (which speed they are guessing) 
are parallel to each other (they need not to be against some marker, they can be in between the markers too). 
After some T seconds, they observe that both the cars are next to some markers and the number of markers in 
between the markers of their car and the other car is D - 1 (excluding the markers next to both the cars). 
Also, they can observe these markers easily because the other car is faster than their. Speed of Sebi's father's car is S. 
Using this information, one can find the speed of the other car accurately.

An example situation when Sebi's father starts the timer. Notice that both the car's are parallel to each other.
Example situation after T seconds. The cars are next to the markers. Here the value of D is 1. The green car is Sebi's and the other car is of blue color.
Sebi's a child, he does not know how to find the check whose guess is close to the real speed of the car. 
He does not trust his father as he thinks that he might cheat. Can you help to resolve this issue between them by telling whose guess is closer. 
If Sebi's guess is better, output "SEBI". If his father's guess is better, output "FATHER". If both the guess are equally close, then output "DRAW".

Input:

The first line of the input contains an integer T denoting the number of test cases.
Each of the next T lines contain five space separated integers S, SG, FG, D, T corresponding to the Sebi's car speed, 
Sebi's guess, his father's guess, D as defined in the statement and the time at which both the cars at against the markers (in seconds), respectively.

Output:

Output description.
For each test case, output a single line containing "SEBI", 
"FATHER" or "DRAW" (without quotes) denoting whose guess is better.
"""
"""
1) get a speed of car and compare with fathers guess and sebis guess
2) if both are equal then print draw
3) speed of car is distance / time 
4) here is distance D - 1.
"""
T = int(input())
S , SG ,FG ,D ,T = input().split()
sebi_car_speed = int(S) 
sebis_guess = int(SG) 
his_father_guess = int(FG) 
num_of_markers = int(D) 
time_both_car_against_markers = int(T) 
