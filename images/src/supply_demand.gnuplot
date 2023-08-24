set terminal pngcairo size 800,300 enhanced
set output 'supply-demand.png'

set xlabel 'Quantity'
set ylabel 'Price'
#set title 'Traditional Supply and Demand Curves'

set xrange [0:120]
set yrange [0:120]

# Removing xtics and ytics
unset xtics
unset ytics

# Supply and demand curves
demand(x) = 0.005*x**2 + 20
supply(x) = -0.005*x**2 + 100

# Adding titles to the lines
set label 1 'Supply' at 5, supply(5) offset 0,1
set label 2 'Demand' at 5, demand(5) offset 0,-1

plot supply(x) title '' with lines lc rgb 'black' lw 4, \
     demand(x) title '' with lines lc rgb 'grey' lw 4

unset label 1
unset label 2

############

set output 'supply-demand-constant.png'

set xlabel 'Quantity'
set ylabel 'Price'
#set title 'Bitcoin Block Space Supply and Demand'

set xrange [0:120]
set yrange [0:120]

# Removing xtics and ytics
unset xtics
unset ytics

# Supply and demand curves
demand(x) = 0.005*x**2 + 20
supply(x) = 80

# Adding titles to the lines
set label 1 'Supply' at 5, supply(5) offset 0,1
set label 2 'Demand' at 5, demand(5) offset 0,-1

plot supply(x) title '' with lines lc rgb 'black' lw 4, \
     demand(x) title '' with lines lc rgb 'grey' lw 4

unset label 1
unset label 2

####################

set output 'fee-negative-feedback.png'

set xlabel "Time"
unset ylabel

#set title 'Negative Feedback Loop'

set xrange [0:20]
set yrange [-1:1]

# Removing xtics and ytics
unset xtics
unset ytics

# Price and demand functions
price(x) = exp(-x/10) * sin(x)
demand(x) = -exp(-x/10) * sin(x)

# Adding titles to the lines
set label 1 'Price (fees)' at 5, price(5) offset -1,0.75
set label 2 'Demand' at 5, demand(5) offset -1,-0.75
#set label 'Equilibrium' at 20,0 offset 2,0

# Equilibrium line
equilibrium(x) = 0

# Increasing the sample rate for smoother curves
set samples 1000

# Adding extra left margin
#set rmargin at screen .8

plot price(x) title '' with lines lc rgb 'black' lw 4, \
     demand(x) title '' with lines lc rgb 'grey' lw 4, \
     equilibrium(x) title 'Equilibrium' with lines lc rgb 'black' lw 2 dt "-"

#######################

set output 'fee-patience.png'

unset label 1
unset label 2

set label 3 "Transactions at different fee rates" at 0.9999,0 font "Arial-Italic"
set arrow 6 from 1,0.6 to 2.3,0.6 nohead lc rgb "black" dashtype 3 lw 2
set arrow 7 from 1,0.3 to 2.7,0.3 nohead lc rgb "black" dashtype 3 lw 2
#set arrow 8 from 1,-0.0 to 3.1,-0.0 nohead lc rgb "black" dashtype 3 lw 2
set arrow 9 from 1,-0.3 to 3.55,-0.3 nohead lc rgb "black" dashtype 3 lw 2
set arrow 10 from 1,-0.6 to 4.2,-0.6 nohead lc rgb "black" dashtype 3 lw 2

set xrange [0.8:6]

plot price(x) title 'Price (fees)' with lines lc rgb 'black' lw 4
     #demand(x) title '' with lines lc rgb 'grey' lw 4

#############################

set output 'equilibrium-change.png'

set xrange [0:20]
unset label 1
unset label 3
unset arrow 6
unset arrow 7
unset arrow 9
unset arrow 10

# Equilibrium line
equilibrium(x) = exp(-x/5) * -1 + 0.25

# Price and demand functions
price(x) = exp(-x/10) * sin(x) + equilibrium(x)
demand(x) = -exp(-x/10) * sin(x) + equilibrium(x)

set label 1 'Price (fees)' at 5, price(5) offset -1.1,1.3
set label 2 'Demand' at 5, demand(5) offset -1.1,-1.3

plot price(x) title '' with lines lc rgb 'black' lw 4, \
     demand(x) title '' with lines lc rgb 'grey' lw 4, \
     equilibrium(x) title 'Equilibrium' with lines lc rgb 'black' lw 2 dt "-"
