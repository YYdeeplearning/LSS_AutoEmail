#!/bin/tcsh
##
##	Job Script for PC Cluster, JAIST
##		created by mkjob.pl
##	** Revise the script as necessary **
#
#PBS -N LSS_Mail
#PBS -q SINGLE
#PBS -j oe 
#PBS -l select=4


setenv PATH /home/$USER/anaconda3/bin:${PATH}
setenv PYTHON_PATH /home/$USER/anaconda3/bin/python

cd ~/LSS_AutoEmail/
python main.py
