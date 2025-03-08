#!/user/bin/awk -f

BEGIN{
    FS=","
}
NR > 1{
    for(i = 1; i <= 7; i++){
        countryData[NR][i] = $i
    }
    print(countryData[int(NR)])
}
END{
}