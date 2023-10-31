# Rosen, Discrete Mathematics and Its Applications, 7th Edition

Pages 1 - 888

Chapter 1 (1 - 115)
  20.10.23 -

## Exercise Formatting

(find opening comment)

### Cleaning

remove "- "-gaps
`(\w)- (\w)` -> `$1$2`

remove "**" and "*" from before numbers and put into parens
`^(∗{1,2}) ([\w\d]{1,2}[\.)])` -> `$2 ($1)`

remove leading, trailing and in-between whitespace from part-indexes
`^\s?(\w) ?\) ?` -> `($1) `

### Formatting

join lines
`[\r\n](?!^\(\w\)|\d{1,2}\. )` -> ` `

add line above intro
`^([\d]{1,2}[\.)])` -> `\n$1`

add bullets to part-indexes
`^(\(\w\) )` -> `- $1`
