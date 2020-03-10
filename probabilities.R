setwd('/Users/acazar/Desktop/blog/projects/b1g_madness')
library(tidyverse)

scored_data <- read_csv('./data/b1g_ratings.csv') 

scored_data <- scored_data %>% 
  arrange(final_score) %>% 
  mutate(rank = row_number())


teams <- scored_data[['Team']]

grid <- expand.grid(teams,teams) 

names(grid) <-  c('home','away')

bracket <- grid %>% 
          filter(away != home) %>% 
          inner_join(., scored_data, by =c('home' = 'Team')) %>% 
          select(home, away, 'home_rank' = rank ) %>% 
          inner_join(., scored_data, by =c('away' = 'Team')) %>% 
          select(home, away,home_rank, 'away_rank' = rank ) %>% 
          mutate('rank_diff' = home_rank-away_rank)

transform_prob <- function(diff) {
  
  p = 1/(1+10^(-diff*(30.464/400)))
  return(p)
  
}


bracket$home_prob <- transform_prob(bracket$rank_diff)
bracket$away_prob <- 1- bracket$home_prob
