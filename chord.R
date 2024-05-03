
library(devtools)
library(chorddiag)
library(ggplot2)

library(RColorBrewer)


df<- read.csv("co_occurrence_matrix.csv")
m <- as.matrix(df[, -1])

issuenames <- c("Trauma", 'Anxiety', 'ADHD', 'Conduct', 'Delirium', 'Bipolar', 'Depression',
                                'ODD', 'PDD', 'Personality', 'Schizophrenia', 'Alcohol/Substance', 'Other Disorder')
dimnames(m) <- list(have = issuenames,
                    prefer = issuenames)
#just to check how many colors brewer have
#display.brewer.all()
brewer1 <- brewer.pal(5, "BuPu")
brewer2 <- brewer.pal(12, "Set3")
groupColors <- c( "#B3DE69","#FB8072","#C5C5C5", "#F2F2F2", "#EDEDED", "#CACACA",
                  "#8C96C6","#DEDEDE", "#E6E6E6", "#D9D9D9", "#D4D4D4", "#B4B4B4", "#A0A0A0"
)


p <- chorddiag(m, groupColors = groupColors, groupnamePadding = 15, groupnameFontsize = 8, showTicks=FALSE,  groupedgeColor = NULL,
               chordedgeColor = "#80808080",showTooltips = FALSE)


p

# save the widget
library(htmlwidgets)
saveWidget(p, file = "chord_diagram.html",selfcontained = TRUE)