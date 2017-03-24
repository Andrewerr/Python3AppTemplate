import inspect
import datetime
import config
class logger:
      def __init__(self,filename):
          """filename--log filename"""
          self.logfile=open(filename,"w+") #open logfile
          self.logfile.write("Log started at "+str(datetime.datetime.now())+"\n")#logs when logging started
      def log(self,msg):
          """msg--log message string"""
          if config.debug:
              print("["+str(datetime.datetime.now())+"]:"+msg)
          self.logfile.write("["+str(datetime.datetime.now())+"]:"+msg+"\n") #write message to log with date time
      def write_stack(self):
          """wrtie full call stack"""
          stack=inspect.stack() #getting stack
          self.logfile.write("<STACK>:")
          for call in stack: #processing each call
              self.logfile.write(str(call[1])+"\n "+str(call[3])+":"+str(call[2]))
      def messagebox(self,title,msg):
          """write to log text styled messagebox
             title--title for messagebox
             msg--message inside the messagebox"""
          self.log("")
          stack=inspect.stack()
          self.logfile.write("+-------|%s"%title+"\n") #writing messagebox header
          for line in msg.split("\n"):
               self.logfile.write("|"+line+"\n")
          self.logfile.write("|at "+str(stack[1][1])+":"+str(stack[1][2])+"("+str(stack[1][3])+")\n")
          self.logfile.write("+-------"+"-"*len(title)+"\n")