from random import choice

import string


def parse_and_fill_mad_lib(mad_lib):
    
    tokens = mad_lib.split(" ")
    
    for idx, token in enumerate(tokens):
        
        exclude = set(string.punctuation)
        naked_token = ''.join(ch for ch in token[1:] if ch not in exclude)

        if len(token) == 0:
        	continue

        if token[0] == "!" and naked_token in term_map.keys():

            tokens[idx] = choice(term_map[naked_token])

    return " ".join(tokens)

term_map = {}

term_map["adverb"] = """not
also
very
often
then
however
too
usually
early
never
always
sometimes
together
likely
simply
generally
instead
actually
again
rather
almost
especially
ever
quickly
probably
already
below
directly
therefore
else
thus
easily
eventually
exactly
certainly
normally
currently
extremely
finally
constantly
properly
soon
specifically
ahead
daily
highly
immediately
relatively
slowly
fairly
primarily
completely
ultimately
widely
recently
seriously
frequently
fully
mostly
naturally
nearly
occasionally
carefully
clearly
essentially
possibly
slightly
somewhat
equally
greatly
necessarily
personally
rarely
regularly
similarly
basically
closely
effectively
initially
literally
mainly
merely
gently
hopefully
originally
roughly
significantly
totally
twice
elsewhere
everywhere
perfectly
physically
suddenly
truly
virtually
altogether
anyway
automatically
deeply
definitely
deliberately
hardly
readily
terribly
unfortunately
forth
briefly
moreover
strongly
honestly
previously""".split()

term_map["adjective"] = """different
used
important
every
large
available
popular
able
basic
known
various
difficult
several
united
historical
hot
useful
mental
scared
additional
emotional
old
political
similar
healthy
financial
medical
traditional
federal
entire
strong
actual
significant
successful
electrical
expensive
pregnant
intelligent
interesting
poor
happy
responsible
cute
helpful
recent
willing
nice
wonderful
impossible
serious
huge
rare
technical
typical
competitive
critical
electronic
immediate
whose
aware
educational
environmental
global
legal
relevant
accurate
capable
dangerous
dramatic
efficient
powerful
foreign
hungry
practical
psychological
severe
suitable
numerous
sufficient
unusual
consistent
cultural
existing
famous
pure
afraid
obvious
careful
latter
obviously
unhappy
acceptable
aggressive
distinct
eastern
logical
reasonable
strict
successfully
administrative
automatic
civil
former
massive
southern
unfair
visible
alive
angry
desperate
exciting
friendly
lucky
realistic
sorry
ugly
unlikely
anxious
comprehensive
curious
impressive
informal
inner
pleasant
sexual
sudden
terrible
unable
weak
wooden
asleep
confident
conscious
decent
embarrassed
guilty
lonely
mad
nervous
odd
remarkable
substantial
suspicious
tall
tiny
more
some
one
all
many
most
other
such
even
new
just
good
any
each
much
own
great
another
same
few
free
right
still
best
public
human
both
local
sure
better
general
specific
enough
long
small
less
high
certain
little
common
next
simple
hard
past
big
possible
particular
real
major
personal
current
left
national
least
natural
physical
short
last
single
individual
main
potential
professional
international
lower
open
according
alternative
special
working
true
whole
clear
dry
easy
cold
commercial
full
low
primary
worth
necessary
positive
present
close
creative
green
late
fit
glad
proper
complex
content
due
effective
middle
regular
fast
independent
original
wide
beautiful
complete
active
negative
safe
visual
wrong
ago
quick
ready
straight
white
direct
excellent
extra
junior
pretty
unique
classic
final
overall
private
separate
western
alone
familiar
official
perfect
bright
broad
comfortable
flat
rich
warm
young
heavy
valuable
correct
leading
slow
clean
fresh
normal
secret
tough
brown
cheap
deep
objective
secure
thin
chemical
cool
extreme
exact
fair
fine
formal
opposite
remote
total
vast
lost
smooth
dark
double
equal
firm
frequent
internal
sensitive
constant
minor
previous
raw
soft
solid
weird
amazing
annual
busy
dead
false
round
sharp
thick
wise
equivalent
initial
narrow
nearby
proud
spiritual
wild
adult
apart
brief
crazy
prior
rough
sad
sick
strange
external
illegal
loud
mobile
nasty
ordinary
royal
senior
super
tight
upper
yellow
dependent
funny
gross
ill
spare
sweet
upstairs
usual
brave
calm
dirty
downtown
grand
honest
loose
male
quiet
brilliant
dear
drunk
empty
female
inevitable
neat
ok
representative
silly
slight
smart
stupid
temporary
weekly
that
this
what
which
time
these
work
no
only
first
over
business
his
game
think
after
life
day
home
economy
away
either
fat
key
training
top
level
far
fun
house
kind
future
action
live
period
subject
mean
stock
chance
beginning
upset
chicken
head
material
salt
car
appropriate
inside
outside
standard
medium
choice
north
square
born
capital
shot
front
living
plastic
express
mood
feeling
otherwise
plus
saving
animal
budget
minute
character
maximum
novel
plenty
select
background
forward
glass
joint
master
red
vegetable
ideal
kitchen
mother
party
relative
signal
street
connect
minimum
sea
south
status
daughter
hour
trick
afternoon
gold
mission
agent
corner
east
neither
parking
routine
swimming
winter
airline
designer
dress
emergency
evening
extension
holiday
horror
mountain
patient
proof
west
wine
expert
native
opening
silver
waste
plane
leather
purple
specialist
bitter
incident
motor
pretend
prize
resident""".split()

term_map["verb"] = """accept
care
could
enjoy
happen
lead
open
reduce
settle
teach
account
carry
count
examine
hate
learn
order
refer
shake
tell
achieve
catch
cover
exist
have
leave
ought
reflect
shall
tend
act
cause
create
expect
head
lend
own
refuse
share
test
add
change
cross
experience
hear
let
pass
regard
shoot
thank
admit
charge
cry
explain
help
lie
pay
relate
should
think
affect
check
cut
express
hide
like
perform
release
shout
throw
afford
choose
damage
extend
hit
limit
pick
remain
show
touch
agree
claim
dance
face
hold
link
place
remember
shut
train
aim
clean
deal
fail
hope
listen
plan
remove
sing
travel
allow
clear
decide
fall
hurt
live
play
repeat
sit
treat
answer
climb
deliver
fasten
identify
look
point
replace
sleep
try
appear
close
demand
feed
imagine
lose
prefer
reply
smile
turn
apply
collect
deny
feel
improve
love
prepare
report
sort
understand
argue
come
depend
fight
include
make
present
represent
sound
use
arrange
commit
describe
fill
increase
manage
press
require
speak
used to
arrive
compare
design
find
indicate
mark
prevent
rest
stand
visit
ask
complain
destroy
finish
influence
matter
produce
result
start
vote
attack
complete
develop
fit
inform
may
promise
return
state
wait
avoid
concern
die
fly
intend
mean
protect
reveal
stay
walk
base
confirm
disappear
fold
introduce
measure
prove
ring
stick
want
be
connect
discover
follow
invite
meet
provide
rise
stop
warn
beat
consider
discuss
force
involve
mention
publish
roll
study
wash
become
consist
divide
forget
join
might
pull
run
succeed
watch
begin
contact
do
forgive
jump
mind
push
save
suffer
wear
believe
contain
draw
form
keep
miss
put
say
suggest
will
belong
continue
dress
found
kick
move
raise
see
suit
win
break
contribute
drink
gain
kill
must
reach
seem
supply
wish
build
control
drive
get
knock
need
read
sell
support
wonder
burn
cook
drop
give
know
notice
realize
send
suppose
work
buy
copy
eat
go
last
obtain
receive
separate
survive
worry
call
correct
enable
grow
laugh
occur
recognize
serve
take
would
can
cost
encourage
handle
lay
offer
record
set
talk
write        
end""".split()
 

term_map["noun"] = """people
history
way
art
money
world
information
map
two
family
government
health
system
computer
meat
year
thanks
music
person
reading
method
data
food
understanding
theory
law
bird
literature
problem
software
control
knowledge
power
ability
economics
love
internet
television
science
library
nature
fact
product
idea
temperature
investment
area
society
activity
story
industry
media
thing
oven
community
definition
safety
quality
development
language
management
player
variety
video
week
security
country
exam
movie
organization
equipment
physics
analysis
policy
series
thought
basis
boyfriend
direction
strategy
technology
army
camera
freedom
paper
environment
child
instance
month
truth
marketing
university
writing
article
department
difference
goal
news
audience
fishing
growth
income
marriage
user
combination
failure
meaning
medicine
philosophy
teacher
communication
night
chemistry
disease
disk
energy
nation
road
role
soup
advertising
location
success
addition
apartment
education
math
moment
painting
politics
attention
decision
event
property
shopping
student
wood
competition
distribution
entertainment
office
population
president
unit
category
cigarette
context
introduction
opportunity
performance
driver
flight
length
magazine
newspaper
relationship
teaching
cell
dealer
debate
finding
lake
member
message
phone
scene
appearance
association
concept
customer
death
discussion
housing
inflation
insurance
woman
advice
blood
effort
expression
importance
opinion
payment
reality
responsibility
situation
skill
statement
wealth
application
city
county
depth
estate
foundation
grandmother
heart
perspective
photo
recipe
studio
topic
collection
depression
imagination
passion
percentage
resource
setting
ad
agency
college
connection
criticism
debt
description
memory
patience
secretary
solution
administration
aspect
attitude
director
personality
psychology
recommendation
response
selection
storage
version
alcohol
argument
complaint
contract
emphasis
highway
loss
membership
possession
preparation
steak
union
agreement
cancer
currency
employment
engineering
entry
interaction
limit
mixture
preference
region
republic
seat
tradition
virus
actor
classroom
delivery
device
difficulty
drama
election
engine
football
guidance
hotel
match
owner
priority
protection
suggestion
tension
variation
anxiety
atmosphere
awareness
bread
climate
comparison
confusion
construction
elevator
emotion
employee
employer
guest
height
leadership
mall
manager
operation
recording
respect
sample
transportation
boring
charity
cousin
disaster
editor
efficiency
excitement
extent
feedback
guitar
homework
leader
mom
outcome
permission
presentation
promotion
reflection
refrigerator
resolution
revenue
session
singer
tennis
basket
bonus
cabinet
childhood
church
clothes
coffee
dinner
drawing
hair
hearing
initiative
judgment
lab
measurement
mode
mud
orange
poetry
police
possibility
procedure
queen
ratio
relation
restaurant
satisfaction
sector
signature
significance
song
tooth
town
vehicle
volume
wife
accident
airport
appointment
arrival
assumption
baseball
chapter
committee
conversation
database
enthusiasm
error
explanation
farmer
gate
girl
hall
historian
hospital
injury
instruction
maintenance
manufacturer
meal
perception
pie
poem
presence
proposal
reception
replacement
revolution
river
son
speech
tea
village
warning
winner
worker
writer
assistance
breath
buyer
chest
chocolate
conclusion
contribution
cookie
courage
dad
desk
drawer
establishment
examination
garbage
grocery
honey
impression
improvement
independence
insect
inspection
inspector
king
ladder
menu
penalty
piano
potato
profession
professor
quantity
reaction
requirement
salad
sister
supermarket
tongue
weakness
wedding
affair
ambition
analyst
apple
assignment
assistant
bathroom
bedroom
beer
birthday
celebration
championship
cheek
client
consequence
departure
diamond
dirt
ear
fortune
friendship
funeral
gene
girlfriend
hat
indication
intention
lady
midnight
negotiation
obligation
passenger
pizza
platform
poet
pollution
recognition
reputation
shirt
sir
speaker
stranger
surgery
sympathy
tale
throat
trainer
uncle
youth
time
work
film
water
example
while
business
study
game
life
form
air
day
place
number
part
field
fish
back
process
heat
hand
experience
job
book
end
point
type
home
economy
value
body
market
guide
interest
state
radio
course
company
price
size
card
list
mind
trade
line
care
group
risk
word
fat
force
key
light
training
name
school
top
amount
level
order
practice
research
sense
service
piece
web
boss
sport
fun
house
page
term
test
answer
sound
focus
matter
kind
soil
board
oil
picture
access
garden
range
rate
reason
future
site
demand
exercise
image
case
cause
coast
action
age
bad
boat
record
result
section
building
mouse
cash
class
nothing
period
plan
store
tax
side
subject
space
rule
stock
weather
chance
figure
man
model
source
beginning
earth
program
chicken
design
feature
head
material
purpose
question
rock
salt
act
birth
car
dog
object
scale
sun
note
profit
rent
speed
style
war
bank
craft
half
inside
outside
standard
bus
exchange
eye
fire
position
pressure
stress
advantage
benefit
box
frame
issue
step
cycle
face
item
metal
paint
review
room
screen
structure
view
account
ball
discipline
medium
share
balance
bit
black
bottom
choice
gift
impact
machine
shape
tool
wind
address
average
career
culture
morning
pot
sign
table
task
condition
contact
credit
egg
hope
ice
network
north
square
attempt
date
effect
link
post
star
voice
capital
challenge
friend
self
shot
brush
couple
exit
front
function
lack
living
plant
plastic
spot
summer
taste
theme
track
wing
brain
button
click
desire
foot
gas
influence
mood
notice
rain
wall
base
damage
distance
feeling
pair
saving
staff
sugar
target
text
animal
author
budget
discount
file
ground
lesson
minute
officer
phase
reference
register
sky
stage
stick
title
trouble
bowl
bridge
campaign
character
club
edge
evidence
fan
letter
lock
maximum
novel
option
pack
park
plenty
quarter
skin
sort
weight
baby
background
carry
dish
factor
fruit
glass
joint
master
muscle
red
strength
traffic
trip
vegetable
appeal
chart
gear
ideal
kitchen
land
log
mother
net
party
principle
relative
sale
season
signal
spirit
street
tree
wave
belt
bench
commission
copy
drop
minimum
path
progress
project
sea
south
status
stuff
ticket
tour
angle
blue
breakfast
confidence
daughter
degree
doctor
dot
dream
duty
essay
father
fee
finance
hour
juice
luck
milk
mouth
peace
pipe
stable
storm
substance
team
trick
afternoon
bat
beach
blank
catch
chain
consideration
cream
crew
detail
gold
interview
kid
mark
mission
pain
pleasure
score
screw
sex
shop
shower
suit
tone
window
agent
band
bath
block
bone
calendar
candidate
cap
coat
contest
corner
court
cup
district
door
east
finger
garage
guarantee
hole
hook
implement
layer
lecture
lie
manner
meeting
nose
parking
partner
profile
rice
routine
schedule
swimming
telephone
tip
winter
airline
bag
battle
bed
bill
bother
cake
code
curve
designer
dimension
dress
ease
emergency
evening
extension
farm
fight
gap
grade
holiday
horror
horse
host
husband
loan
mistake
mountain
nail
noise
occasion
package
patient
pause
phrase
proof
race
relief
sand
sentence
shoulder
smoke
stomach
string
tourist
towel
vacation
west
wheel
wine
arm
aside
associate
bet
blow
border
branch
breast
brother
buddy
bunch
chip
coach
cross
document
draft
dust
expert
floor
god
golf
habit
iron
judge
knife
landscape
league
mail
mess
native
opening
parent
pattern
pin
pool
pound
request
salary
shame
shelter
shoe
silver
tackle
tank
trust
assist
bake
bar
bell
bike
blame
boy
brick
chair
closet
clue
collar
comment
conference
devil
diet
fear
fuel
glove
jacket
lunch
monitor
mortgage
nurse
pace
panic
peak
plane
reward
row
sandwich
shock
spite
spray
surprise
till
transition
weekend
welcome
yard
alarm
bend
bicycle
bite
blind
bottle
cable
candle
clerk
cloud
concert
counter
flower
grandfather
harm
knee
lawyer
leather
load
mirror
neck
pension
plate
purple
ruin
ship
skirt
slice
snow
specialist
stroke
switch
trash
tune
zone
anger
award
bid
bitter
boot
bug
camp
candy
carpet
cat
champion
channel
clock
comfort
cow
crack
engineer
entrance
fault
grass
guy
hell
highlight
incident
island
joke
jury
leg
lip
mate
motor
nerve
passage
pen
pride
priest
prize
promise
resident
resort
ring
roof
rope
sail
scheme
script
sock
station
toe
tower
truck
witness
a
you
it
can
will
if
one
many
most
other
use
make
good
look
help
go
great
being
few
might
still
public
read
keep
start
give
human
local
general
she
specific
long
play
feel
high
tonight
put
common
set
change
simple
past
big
possible
particular
today
major
personal
current
national
cut
natural
physical
show
try
check
second
call
move
pay
let
increase
single
individual
turn
ask
buy
guard
hold
main
offer
potential
professional
international
travel
cook
alternative
following
special
working
whole
dance
excuse
cold
commercial
low
purchase
deal
primary
worth
fall
necessary
positive
produce
search
present
spend
talk
creative
tell
cost
drive
green
support
glad
remove
return
run
complex
due
effective
middle
regular
reserve
independent
leave
original
reach
rest
serve
watch
beautiful
charge
active
break
negative
safe
stay
visit
visual
affect
cover
report
rise
walk
white
beyond
junior
pick
unique
anything
classic
final
lift
mix
private
stop
teach
western
concern
familiar
fly
official
broad
comfortable
gain
maybe
rich
save
stand
young
heavy
hello
lead
listen
valuable
worry
handle
leading
meet
release
sell
finish
normal
press
ride
secret
spread
spring
tough
wait
brown
deep
display
flow
hit
objective
shoot
touch
cancel
chemical
cry
dump
extreme
push
conflict
eat
fill
formal
jump
kick
opposite
pass
pitch
remote
total
treat
vast
abuse
beat
burn
deposit
print
raise
sleep
somewhere
advance
anywhere
consist
dark
double
draw
equal
fix
hire
internal
join
kill
sensitive
tap
win
attack
claim
constant
drag
drink
guess
minor
pull
raw
soft
solid
wear
weird
wonder
annual
count
dead
doubt
feed
forever
impress
nobody
repeat
round
sing
slide
strip
whereas
wish
combine
command
dig
divide
equivalent
hang
hunt
initial
march
mention
spiritual
survey
tie
adult
brief
crazy
escape
gather
hate
prior
repair
rough
sad
scratch
sick
strike
employ
external
hurt
illegal
laugh
lay
mobile
nasty
ordinary
respond
royal
senior
split
strain
struggle
swim
train
upper
wash
yellow
convert
crash
dependent
fold
funny
grab
hide
miss
permit
quote
recover
resolve
roll
sink
slip
spare
suspect
sweet
swing
twist
upstairs
usual
abroad
brave
calm
concentrate
estimate
grand
male
mine
prompt
quiet
refuse
regret
reveal
rush
shake
shift
shine
steal
suck
surround
anybody
bear
brilliant
dare
dear
delay
drunk
female
hurry
inevitable
invite
kiss
neat
pop
punch
quit
reply
representative
resist
rip
rub
silly
smile
spell
stretch
stupid
tear
temporary
tomorrow
wake
wrap
yesterday""".split()