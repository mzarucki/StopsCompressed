for mstop in 400 425 450 475 500 525 550 575 600
do 
    for dm in 10 20 30 40 50 60 70 80
    do
        python parseTxT.py --mstop ${mstop} --dm ${dm}
    
    done    
done