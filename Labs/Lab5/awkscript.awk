NR == 1, NR == 2 {
    total+=$6
} 

END {
    printf "%-6s %10d\n", "Total:", total
}