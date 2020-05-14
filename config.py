#!/usr/bin/env python3

#  dirs and files
BaseDir = '/Users/wbhawley/Research/Seismology/OOI-Seismic/'
ConfigDir = BaseDir+'config/' # where we keep setup files
DataDir = BaseDir+'data/'  # where the data will be saved
EventsDataDir = DataDir+'SAC_Events/' # event sac files - saved by EVENT/[dataFile]
NoiseDataDir = DataDir+'SAC_Noise/' # noise sac files - saved by NW_STNM/[datafile]
EventsFileName = ConfigDir+'EventFile.txt' # expected format 'YYYYMMDDHHMM/n'
DayFileName = ConfigDir+'NoiseFile.txt' # format same as above
Stafn = ConfigDir+'OO_stations.txt'  # station names separated by newline

# Time Params
tstart = '2016-09-01T00:00:00'
tend = '2016-09-30T23:00:00'

# Station Params
webservice = "IRIS"
network = "OO"  # X9 = Blanco / OO = OOI
inFile = open(Stafn)
StaList = []
for line in inFile:
    StaList.append(line.rstrip('\n'))
# channel list
ChanList = ['LHZ', 'LH1', 'LH2', 'BDH']

#  Event download
minMag = 6.5
isCMT_params = 1  # use GCMT parameters for SAC header; 0 = use IRIS
isCentroid = 1  # if isCMT_params = 1, use centroid; 0 = epicentral

#  Noise Download - option to download files from time window or just prior to events
isBeforeEvents = 0  # 1 to download a few days prior to seismic events in the EventsFileName
                    # 0 to download all data between tstart and tend
#  If isBeforeEvents = 1
noDays = 4  # number of days prior to event to use
isCalDay = 1  # 0 to start each day at 00:00; 0 to use 24h segments prior to eq
# If isBeforeEvents = 0


# All Trace Info
# downsample
isDownsamp = 1  # downsample option
srNew = 1  # new sample rate, samples/sec

# response removal
isRemoveResp = 1  # remove response option
RespOutput = "DISP" # 'DISP', 'VEL', or 'ACC'
ZeroMeanOpt = True # T/F
TaperOpt = True # T/F
TaperFraction = 0.05

# Frequency Limits for Response Removal
# Hi corner deternimed by Nyquist
# Lo corner defined by
LoFreq1 = 0.001
LoFreq2 = 0.005

# Event trace info
trLen = 6000  # len of traces (sec)

# Noise trace info
