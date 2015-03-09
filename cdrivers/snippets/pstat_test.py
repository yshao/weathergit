import cProfile
import re
cProfile.run('re.compile("foo|bar")', filename="pstat_test.pstats")

print "ABCD"


# import hotshot, hotshot.stats, test.pystone
# prof = hotshot.Profile("stones.prof")
# benchtime, stones = prof.runcall(test.pystone.pystones)
# prof.close()
# stats = hotshot.stats.load("stones.prof")
# stats.strip_dirs()
# stats.sort_stats('time', 'calls')
# stats.print_stats(20)

import timeit

print "TIMEIT"

print timeit.timeit('"-".join(map(str, range(100)))', number=10000)