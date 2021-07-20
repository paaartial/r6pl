import util
from stage import Stage

# print(util.get_upcoming_matches(util.north_america_link))
nal_stage_2 = Stage(util.north_america_link)
brazil_stage_2 = Stage(util.brazil_link)
europe_stage_2 = Stage(util.europe_link)
apac_south_stage_2 = Stage(util.apac_south_link)
apac_north_stage_2 = Stage(util.apac_north_link)

print("NAl Stage 2: ")
nal_stage_2.run(10000)
nal_stage_2.display_stats()
print("\n")

print("Brazil Stage 2")
brazil_stage_2.run(10000)
brazil_stage_2.display_stats()
print("\n")

print("Europe Stage 2")
europe_stage_2.run(10000)
europe_stage_2.display_stats()
print("\n")

print("APAC North Stage 2")
apac_north_stage_2.run(10000)
apac_north_stage_2.display_stats()
print("\n")

print("APAC South Stage 2")
apac_south_stage_2.run(10000)
apac_south_stage_2.display_stats()
print("\n")
