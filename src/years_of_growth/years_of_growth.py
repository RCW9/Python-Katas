
def years_of_growth(initial_population, target_population, growth_rate, net_migration):
  
  if initial_population > 0:
   year = 0
   population = initial_population
  else:
    year = 1
    population = net_migration
  while population < target_population:
    population = (population * growth_rate ) + net_migration
    year += 1
  return year
    
