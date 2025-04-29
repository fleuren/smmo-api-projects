# Fleuren's SimpleMMO API Projects
- if reused/referenced, please credit, thanks!
- may be referred to as "Complex Cat" (parody of Simple Wolf, thanks RacknRoll)
# Main Project
Guild-focused Companion App (smmocompanion.py)
- Tracks current season
- Can track specific guilds (input guild ID)
- Outputs data for guild members
- SGL can now be refreshed
- Can calculate the difference and needed actions between the host's guild and their target guild (from a snapshot, not live)
- Added a very basic PVP simulator (compares stats, does not consider hit chance / rng)

# Side Projects
Diamond Market Tracker (diamondmarket.py)
- Outputs the listing based on an inputted price.
- If no listings are available for that price, lists the cheapest listing available.
Known bugs (and attempts at fixing):
- Outputs from most expensive to least expensive, see lowest listing for the cheapest value.

Guild Inactivity Tracker (inactivity.py)
- Outputs the name, id, and the date and time of an inactive user's last activity, based on the given range (in days).

Guild Member Level Tracker (leveltracker.py)
- Tracks the levels of all guild members at a fixed point in time (start of script).
*may evolve into allowing to track other specific stats, such as total steps, pve/pvp kills, etc.*
  
# Planned Scripts:
- Orphanage Progress and Boosts display
- World boss timers (with windows notification)
- Other projects (TBA)
