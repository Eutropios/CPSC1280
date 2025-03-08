BEGIN{
    srand(void)
    printf "%-15s %-30s %-15s\n", "Last Name", "Pet", "Temp Password"
}
{
    separator = ", "
    gsub("\"", "")
    sub(" ", "", $5)
    petName = $4
    petNameLength = length($4)
    if($5 != ""){
        petName = petName separator $5
        petNameLength += length(separator) + length($5)
    }
    randomNumber = int(rand() * 199 + 1)
    tempPassword = substr($2, 1, 3) petNameLength "_" randomNumber
    printf "%-15s %-30s %-15s\n", $1, petName, tempPassword
}