#!/bin/sh

source Setup_FileLocation.sh

echo $Step1Output 

cat $Step1Output/*/*txt | ./RunMatchFiles > Files/MatchedFiles




