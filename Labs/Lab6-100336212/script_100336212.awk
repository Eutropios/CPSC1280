BEGIN{
    printf "%-15s %-15s %-15s %12s\n", "First Name", "Last Name", "Gender", "Pet"

}
{
    gsub("\"", "")
    sub(" ", "", $5)
    petName = $4
    if($5 != ""){
        petName = petName ", " $5
    }
    printf "%-15s %-15s %-15s %-12s\n", $1, $2, $3, petName 
}