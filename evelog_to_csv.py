from datetime import datetime
import json
import argparser

def timestamp(date):
    return int(time.mktime(datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f+0200").timetuple()))

def flows_eve_json_to_csv(inputfile,outputfile)
	file=inputfile
	csv=outputfile
	log_final=open(csv, 'w')
	with open(file) as log:
	    p = log.readlines()
	    log_final.write("date,src_ip,dst_ip,proto,src_port,dst_port,pkts,pktc,bytc,st,en,flgts,flgtc,flg,dur")
	    for i in p:
	        line=json.loads(i)

	        date = timestamp(line["timestamp"])
	        src_ip = line["src_ip"]
	        dst_ip = line["dest_ip"]
	        proto = line["proto"]
	
	        if "ICMP" in proto:
	            pass
	        else:
	            src_port = line["src_port"]
	            dst_port = line["dest_port"]
	            pkts = line["flow"]["pkts_toserver"]
	            pktc = line["flow"]["pkts_toclient"]
	            byts = line["flow"]["bytes_toserver"]
	            bytc = line["flow"]["bytes_toclient"]
	            st = timestamp(line["flow"]["start"])
	            en = timestamp(line["flow"]["end"])
	            dur = st-en
	            if proto == "TCP":
	                flgts = line["tcp"]["tcp_flags_ts"]
	                flgtc = line["tcp"]["tcp_flags_tc"]
	                flg = line["tcp"]["tcp_flags"]
	            else:
	                flgts = 0
	                flgtc = 0
	                flg = 0
	            
	        log_final.write("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13}".format(date,src_ip,dst_ip,proto,src_port,
	                                                                               dst_port,pkts,pktc,bytc,st,en,flgts,
	                                                                              flgtc,flg,dur))
if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", dest='inputfile', type=file)
	parser.add_argument("-o", dest='outputfile', type=file)
	args.parser.parse_args()
	flows_eve_json_to_csv(args.inputfile,args.outputfile)
