__author__ = 'Ping'

import sys
import os
import ctypes
from utils import *
from best.commonsocketutils import *

sys.path.append(os.getcwd())


FLASH_APP_PATH='/FlashDisk'

SERVER_IP="127.0.0.1"
DAQ_USER='admin'
DAQ_PASSWD='best'

IP_ARCHIVAL="192.168.38.35"
IP_ENCODER="192.168.38.33"
IP_RAD1="192.168.38.31"
IP_RAD2="192.168.38.43"
PATH_ARCHIVAL="C:/SlowTest/arch/FlashDisk/DaqArchImu.exe"
PATH_ENCODER="C:/SlowTest/encoder/FlashDisk/DaqEnc.exe"
PATH_RAD1="C:/SlowTest/rad1/FlashDisk/DaqRad.exe"
PATH_RAD2="C:/SlowTest/rad2/FlashDisk/DaqRad.exe"
SLOWTEST_PATHS={PATH_ARCHIVAL,PATH_ENCODER,PATH_RAD1,PATH_RAD2}

CLIENT_DIR="C:/SlowTest/client"

CONFIG_FILE='config.xml'

EXPORT_PATH=""

import ftplib

# def sendExecFile(src_file,targ_addr,ip):
#     print "[INFO]","Connect to server"
#     session = ftplib.FTP(ip,USER, PASSWD)
#     session.cwd(targ_addr)
#     print(session.dir())
#     file = open(src_file,'rb')                  # file to send
#     try:
#         session.storbinary('STOR '+src_file, file)     # send the file
#     except ftplib.error_perm:
#         session.delete(src_file)
#         session.storbinary('STOR '+src_file, file)     # send the file
#     session.quit()
#     file.close()                                    # close file and FTP

import os
import shutil

script_name = re.sub('\..*','',os.path.basename(sys.argv[0]))
starting_dir = os.getcwd()
start_message="load software and run test"

gLogger=create_logger(script_name,start_message)



def copy_file(src_file,dst_root):
    print "[INFO]","Copy program files to FlashDisk"
    assert not os.path.isabs(src_file)
    dst_dir =  os.path.join(dst_root, src_file)
    # try:
    print src_file,"to",dst_dir
    # os.makedirs(dst_dir) # create all directories, raise an error if it already exists
    shutil.copy(src_file, dst_dir)
    # # except :
    #

def xml_read_config(ini_filename):
    print "[INFO]","Reading test config"
    from xml.etree.ElementTree import parse, Element
    input_xml = open(ini_filename,'r')
    tree = parse(input_xml)
    root = tree.getroot()

    for child in root:
       print child.tag, child.attrib

    for neighbor in root.iter('neighbor'):
       print neighbor.attrib

    for country in root.findall('country'):
       rank = country.find('rank').text
       name = country.get('name')
       print name, rank

    for rank in root.iter('rank'):
       new_rank = int(rank.text) + 1
       rank.text = str(new_rank)
       rank.set('updated', 'yes')


    tree.write('output.xml')


def xml_read_config2(ini_filename):
    print "[INFO]","Reading test config"
    from xml.etree.ElementTree import parse, Element
    input_xml = open(ini_filename,'r')
    tree = parse(input_xml)
    root = tree.getroot()

    for child in root:
       print child.tag, child.attrib

    for neighbor in root.iter('neighbor'):
       print neighbor.attrib

    for country in root.findall('country'):
       rank = country.find('rank').text
       name = country.get('name')
       print name, rank

    for rank in root.iter('rank'):
       new_rank = int(rank.text) + 1
       rank.text = str(new_rank)
       rank.set('updated', 'yes')


    tree.write('output.xml')


def main():

    ip_addr_dict=xml_read_config(CONFIG_FILE)

    srcfile = 'test.data'
    dstroot = 'c:/SlowTest/FlashDisk/Data'
    copy_file(srcfile,dstroot)
    countdown(5)
    # copyFile(srcfile,dstroot)


    # sendExecFile(srcfile,FLASH_APP_PATH,SERVER_IP)
    zipfile_unzip(EXPORT_PATH+"/BestDaq*.zip",EXPORT_PATH+"/unzipped")
    ftp_send(srcfile,FLASH_APP_PATH+"/"+srcfile,SERVER_IP,DAQ_USER,DAQ_PASSWD)


    # run_slowtest_daq_program()
    #
    # gLogger.debug("Getting device info")
    # socket_send_command(GETSYSINFO)
    #
    # gLogger.debug("Getting data")
    # socket_send_command(GETDATA)
    # gLogger.debug("Getting data")
    # socket_send_command(SENDCONFIG)


# def run_slowtest_daq_program():
#     while len(SLOWTEST_PATHS) != 0:
#         path = SLOWTEST_PATHS.pop()
#         cmd_path=""
#         cmd_list=" ".join(cmd_path,path)
#         sw_list=""
#         token_list=[""]
#         out_list=command_and_parse(cmd_list,sw_list,token_list)
#         msg= " ".join(cmd_list,"[OUTPUT] -",out_list)
#         logger.debug(msg)
#         print "[INFO]","Connecting: ", ip


def comm_with_archival_socket():
    print "[INFO]","Communicating with archival socket"


def sendCmd(cmd):
    print "send",cmd

def run_cmd(cmd_byte):


main()